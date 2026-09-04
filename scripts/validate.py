#!/usr/bin/env python3
"""Validate the portfolio's data layer before it ships.

Run locally before committing, and in CI (.github/workflows/validate.yml):

    python3 scripts/validate.py

ERRORS fail the build; WARNINGS are advisory (printed, exit 0 unless an error
also fired). Checks:

  * _data/publications.yml is in sync with papers.bib (regenerate if not)
  * every `stage` (publications + projects) is in the controlled vocabulary
  * news dates are well-formed and sorted newest-first
  * headline publications are a subset of selected
  * arxiv / doi fields are well-formed
  * internal links resolve to a real page (warn)
  * venue/status roughly agree with stage (warn)
  * the private gmail address never leaks into shipped content
  * every publication stage has a section on /publications (else the
    entry would silently vanish from the page)
  * identity is consistent across the pages that state it: canonical name
    and surname, ORCID, public email, and — the checkable one — that the
    independent programme (2020) is never conflated with the Vaika
    affiliation (2024)
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_publications as gen  # noqa: E402
from bibparse import parse  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

errors, warnings = [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


# ---- controlled vocabulary --------------------------------------------------
VOCAB = set(load("_data/statuses.yml").keys())

# ---- 1. publications.yml is in sync with papers.bib -------------------------
if gen.build() != read("_data/publications.yml"):
    err("_data/publications.yml is out of sync with papers.bib — "
        "run: python3 scripts/gen_publications.py")

pubs = load("_data/publications.yml")
bib_keys = {e["_key"] for e in parse(os.path.join(ROOT, "papers.bib"))}
if {p["key"] for p in pubs} != bib_keys:
    err("publications.yml key set does not match papers.bib")

# ---- 2. publications: stage vocab, headline subset, link formats ------------
ARXIV_RE = re.compile(r"^https://arxiv\.org/abs/\d{4}\.\d{4,5}$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
for p in pubs:
    k = p["key"]
    if p.get("stage") not in VOCAB:
        err(f"publication {k}: stage {p.get('stage')!r} not in vocabulary")
    if p.get("headline") and not p.get("selected"):
        err(f"publication {k}: headline=true but selected is not true")
    if p.get("arxiv") and not ARXIV_RE.match(p["arxiv"]):
        err(f"publication {k}: arxiv {p['arxiv']!r} is not a canonical arXiv abs URL")
    if p.get("doi") and not DOI_RE.match(p["doi"]):
        err(f"publication {k}: doi {p['doi']!r} is not a bare DOI (10.x/...)")

# ---- 2b. every publication stage is rendered on /publications ---------------
# /publications groups entries by `stage`. A stage with no section would drop
# those publications off the page silently — catch that here.
rendered_stages = set(re.findall(r'where:\s*"stage",\s*"([^"]+)"', read("publications.md")))
for p in pubs:
    st = p.get("stage")
    if st and st not in rendered_stages:
        err(f"publication {p['key']}: stage {st!r} has no section on /publications — "
            "the entry would silently vanish from the page")

# ---- 3. projects: required fields + stage vocab -----------------------------
internal_targets = []
projects = load("_data/projects.yml")
for section in projects:
    if not section.get("category"):
        err("projects.yml: a section is missing `category`")
    for pr in section.get("projects", []):
        title = pr.get("title", "<untitled>")
        for f in ("title", "url", "summary", "status"):
            if not pr.get(f):
                err(f"project {title!r}: missing `{f}`")
        st = pr.get("stage")
        if st is None:
            warn(f"project {title!r}: no `stage` (add one from the vocabulary)")
        elif st not in VOCAB:
            err(f"project {title!r}: stage {st!r} not in vocabulary")
        internal_targets.append(pr.get("url", ""))

# ---- 4. news: date format + descending order + link harvest -----------------
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
DATE_RE = re.compile(r"^([A-Z][a-z]{2}) (\d{4})$")
news = load("_data/news.yml")
prev = None
for i, item in enumerate(news):
    d = item.get("date", "")
    m = DATE_RE.match(d)
    if not m:
        err(f"news[{i}]: date {d!r} not 'Mon YYYY' (e.g. 'Jun 2026')")
        continue
    key = (int(m.group(2)), MONTHS[m.group(1)])
    if prev is not None and key > prev:
        err(f"news[{i}]: date {d!r} is newer than the item above it — keep newest first")
    prev = key
    if not item.get("text"):
        err(f"news[{i}]: missing `text`")

# ---- 5. internal-link resolution (warn) -------------------------------------
# Valid internal pages served by THIS repo: root *.md permalinks + static files.
def permalink_of(md):
    fm = re.match(r"^---\n(.*?)\n---", read(md), re.DOTALL)
    if fm:
        pm = re.search(r"^permalink:\s*(\S+)", fm.group(1), re.MULTILINE)
        if pm:
            return pm.group(1)
    base = os.path.basename(md)[:-3]
    return "/" if base == "index" else f"/{base}/"

pages = {permalink_of(f) for f in os.listdir(ROOT) if f.endswith(".md")}
pages |= {"/papers.bib", "/llms.txt", "/robots.txt", "/feed.xml",
          "/sitemap.xml", "/cv.pdf"}
# Sibling project sites live at mool32.github.io/<repo>/ (separate repos) — allow.
SIBLING_SITES = {"dat-ru", "you-are-not-random", "game_theory_models", "assets"}

LINK_RE = re.compile(r"\]\((/[^)\s]+)\)")
def harvest(text):
    return LINK_RE.findall(text or "")

link_sources = ([n.get("text", "") for n in news]
                + [pr.get("summary", "") + " " + pr.get("url", "")
                   for s in projects for pr in s.get("projects", [])])
for text in link_sources:
    for target in harvest(text):  # only real markdown links [..](/path/)
        clean = target.split("#")[0].rstrip()
        if clean in pages:
            continue
        first = clean.strip("/").split("/")[0]
        if first in SIBLING_SITES:
            continue
        warn(f"internal link {clean!r} does not match any known page/permalink")

# ---- 6. stage vs free-text status agreement (warn) --------------------------
STATUS_HINTS = {
    "in-preparation": "in preparation",
    "under-review": "under review",
    "submission-ready": "ready",
    "software-release": "release",
    "preprint": "preprint",
}
for p in pubs:
    hint = STATUS_HINTS.get(p.get("stage"))
    if hint and hint not in (p.get("status") or "").lower():
        warn(f"publication {p['key']}: status {p.get('status')!r} doesn't mention "
             f"the stage ({p.get('stage')})")

# ---- 7. private email must never leak into shipped content ------------------
# The address may legitimately appear as a documented "do NOT use this" example
# (e.g. the methodology checklist) — only flag lines that present it as contact.
GMAIL = "theospirin" + "@gmail.com"
for dirpath, _dirs, files in os.walk(ROOT):
    if os.sep + ".git" in dirpath:
        continue
    for f in files:
        if f.rsplit(".", 1)[-1] not in ("yml", "yaml", "md", "html", "txt", "bib"):
            continue
        path = os.path.join(dirpath, f)
        for ln, line in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
            if GMAIL in line and "not" not in line.lower():
                err(f"{os.path.relpath(path, ROOT)}:{ln}: leaks the private gmail "
                    "address as contact (public contact must be tspiro@vaika.org)")

# ---- 8. identity + date consistency ----------------------------------------
# The facts a reader can check in 30 seconds — name, ORCID, public email, and
# which year attaches to which claim — must not disagree between the pages that
# state them. This is the class of bug that quietly costs credibility.
IDENT = {
    "name":              "Theodor Spiro",
    "orcid":             "0009-0004-5382-9346",
    "email":             "tspiro@vaika.org",
    "program_since":     "2020",   # the independent research programme
    "affiliation_since": "2024",   # the Vaika Inc. affiliation
}
IDENT_FILES = ["index.md", "cv.md", "llms.txt", "_config.yml",
               "_includes/head.html", "publications.md", "projects.md",
               "methodology.md"]
NAME_VARIANTS = ["Teo Spiro", "Teo Spirin", "T. Spirin"]

for rel in IDENT_FILES:
    if not os.path.exists(os.path.join(ROOT, rel)):
        continue
    text = read(rel)

    # every ORCID-shaped string must be the canonical one (catches typos)
    for found in set(re.findall(r"\b\d{4}-\d{4}-\d{4}-\d{3}[\dX]\b", text)):
        if found != IDENT["orcid"]:
            err(f"{rel}: ORCID {found} does not match the canonical {IDENT['orcid']}")

    # every mailto must be the public address
    for addr in set(re.findall(r"mailto:([^\"'\s>)\]]+)", text)):
        if addr != IDENT["email"]:
            err(f"{rel}: mailto:{addr} is not the canonical public email {IDENT['email']}")

    # non-canonical spellings of the author name
    for ln, line in enumerate(text.split("\n"), 1):
        for bad in NAME_VARIANTS:
            if bad in line:
                err(f"{rel}:{ln}: non-canonical author name {bad!r} — use {IDENT['name']!r}")
        if re.search(r"\bSpirin\b", line):
            err(f"{rel}:{ln}: surname typo 'Spirin' — the canonical surname is 'Spiro'")

    # 'Serbanescu' is allowed only where the historical name-note is documented
    if "Serbanescu" in text and rel not in ("llms.txt", "methodology.md"):
        err(f"{rel}: 'Serbanescu' appears outside the documented name-note")

    # The affiliation must never be dated to the programme's start year.
    # Work sentence-by-sentence on whitespace-collapsed text: the claim is often
    # split across a line break, and either word order occurs ("affiliated since
    # 2020" / "Since 2020 ... affiliated"). A sentence that names BOTH years is
    # disambiguating on purpose (llms.txt does this) and is left alone.
    _prog, _affil = IDENT["program_since"], IDENT["affiliation_since"]
    _flat = re.sub(r"\s+", " ", text)
    for _sent in re.split(r"(?<=[.;])\s+", _flat):
        if _affil in _sent:
            continue
        _dated_prog = re.search(
            r"(?i)(since\s+\*{0,2}" + _prog + r"\b|\b" + _prog + r"\s*[–-]\s*present)", _sent)
        if _dated_prog and re.search(r"(?i)affiliat|vaika", _sent):
            err(f"{rel}: the Vaika affiliation is dated to {_prog} — the independent "
                f"programme runs from {_prog}, the affiliation from {_affil}")
            break

    # "· YYYY – present" lines must carry the right year for what they describe
    for ln, line in enumerate(text.split("\n"), 1):
        m = re.search(r"·\s*(20\d\d)\s*[–-]\s*present", line)
        if not m:
            continue
        yr = m.group(1)
        if "Vaika" in line and yr != IDENT["affiliation_since"]:
            err(f"{rel}:{ln}: Vaika affiliation dated {yr}, canonical is {IDENT['affiliation_since']}")
        if re.search(r"(?i)\bindependent\b", line) and yr != IDENT["program_since"]:
            err(f"{rel}:{ln}: independent programme dated {yr}, canonical is {IDENT['program_since']}")

# ---- report -----------------------------------------------------------------
for w in warnings:
    print(f"  WARN  {w}")
for e in errors:
    print(f"  FAIL  {e}")
n_pub = len(pubs)
print(f"\n{n_pub} publications, {sum(len(s.get('projects', [])) for s in projects)} projects, "
      f"{len(news)} news items · {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
