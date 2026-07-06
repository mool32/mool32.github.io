#!/usr/bin/env python3
"""Generate _data/publications.yml from papers.bib (the single source of truth).

papers.bib is hand-authored; _data/publications.yml is a committed build
artifact — DO NOT edit it by hand. After editing papers.bib, run:

    python3 scripts/gen_publications.py

CI (.github/workflows/validate.yml) re-runs this and fails if the committed
file is out of sync, so drift between the .bib and the site is impossible.
"""
import os

from bibparse import parse, short_authors

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BIB = os.path.join(ROOT, "papers.bib")
OUT = os.path.join(ROOT, "_data", "publications.yml")

# Fields emitted per publication, in this order. `pdf` is intentionally NOT
# surfaced (the al-folio PDF filenames in papers.bib are not served here).
STRING_FIELDS = ["title", "authors", "venue", "abbr", "arxiv", "doi",
                 "code", "demo", "abstract", "stage", "status"]

HEADER = """\
# GENERATED FILE — do not edit by hand.
# Source of truth: /papers.bib. Regenerate with:  python3 scripts/gen_publications.py
# Rendered on /publications/ (all) and / (where selected/headline is true).
# Ordering follows the `order` field in papers.bib.
"""


def yaml_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def record(entry):
    """Map a parsed bib entry to the publications.yml record (ordered dict)."""
    r = {"key": entry["_key"]}
    r["title"] = entry.get("title", "")
    r["authors"] = short_authors(entry.get("author", ""))
    r["year"] = int(entry["year"]) if entry.get("year", "").isdigit() else entry.get("year", "")
    r["venue"] = entry.get("venue") or entry.get("journal") or entry.get("howpublished", "")
    r["abbr"] = entry.get("abbr")

    url = entry.get("url", "")
    if "arxiv.org" in url:
        r["arxiv"] = url
    elif entry.get("archivePrefix", "").lower() == "arxiv" and entry.get("eprint"):
        r["arxiv"] = f"https://arxiv.org/abs/{entry['eprint']}"
    r["doi"] = entry.get("doi")
    r["code"] = entry.get("code")
    r["demo"] = entry.get("demo")
    # Card text: prefer the short `teaser`; fall back to the full `abstract`.
    r["abstract"] = entry.get("teaser") or entry.get("abstract", "")
    r["stage"] = entry.get("stage")
    r["status"] = entry.get("status")
    r["selected"] = entry.get("selected") == "true"
    r["headline"] = entry.get("headline") == "true"
    return r


def emit(r):
    lines = [f"- key: {r['key']}"]
    lines.append(f"  title: {yaml_quote(r['title'])}")
    lines.append(f"  authors: {yaml_quote(r['authors'])}")
    lines.append(f"  year: {r['year']}")
    for f in ["venue", "abbr", "arxiv", "doi", "code", "demo"]:
        if r.get(f):
            lines.append(f"  {f}: {yaml_quote(r[f])}")
    lines.append(f"  abstract: {yaml_quote(r['abstract'])}")
    if r.get("stage"):
        lines.append(f"  stage: {yaml_quote(r['stage'])}")
    if r.get("status"):
        lines.append(f"  status: {yaml_quote(r['status'])}")
    lines.append(f"  selected: {'true' if r['selected'] else 'false'}")
    if r["headline"]:
        lines.append("  headline: true")
    return "\n".join(lines)


def build():
    """Return the full text of _data/publications.yml (no side effects)."""
    entries = parse(BIB)
    entries.sort(key=lambda e: int(e.get("order", "999")))
    body = "\n\n".join(emit(record(e)) for e in entries)
    return HEADER + "\n" + body + "\n"


def main():
    text = build()
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {OUT} ({len(parse(BIB))} publications)")


if __name__ == "__main__":
    main()
