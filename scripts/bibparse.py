"""Tiny, zero-dependency BibTeX reader for this repo's papers.bib.

Deliberately not a general BibTeX parser. It relies on the house style used
throughout papers.bib (enforced by scripts/validate.py):

  * one entry per @type{key, ... } block, closing brace on its own line;
  * every field is `name = {value}` on a SINGLE line, brace-balanced,
    with no nested braces inside the value.

parse() -> list of dicts, each with '_type', '_key', and the raw string
fields. Order of the returned list follows file order.
"""
import re

_ENTRY_RE = re.compile(r"^@(\w+)\s*\{\s*([^,]+),\s*$")
_FIELD_RE = re.compile(r"^\s*([A-Za-z_]+)\s*=\s*\{(.*)\}\s*,?\s*$")


def parse(path):
    entries = []
    cur = None
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("%"):
                continue
            m = _ENTRY_RE.match(line)
            if m:
                if cur is not None:
                    raise ValueError(f"{path}:{lineno}: new entry before previous one closed")
                cur = {"_type": m.group(1), "_key": m.group(2).strip()}
                continue
            if stripped == "}":
                if cur is None:
                    raise ValueError(f"{path}:{lineno}: stray closing brace")
                entries.append(cur)
                cur = None
                continue
            if cur is None:
                raise ValueError(f"{path}:{lineno}: field outside an entry: {stripped!r}")
            fm = _FIELD_RE.match(line)
            if not fm:
                raise ValueError(
                    f"{path}:{lineno}: field not single-line/brace-balanced "
                    f"(house style): {stripped!r}"
                )
            name, value = fm.group(1), fm.group(2)
            if name in cur:
                raise ValueError(f"{path}:{lineno}: duplicate field {name!r} in {cur['_key']}")
            cur[name] = value
    if cur is not None:
        raise ValueError(f"{path}: unexpected EOF inside entry {cur['_key']}")
    return entries


def short_authors(author_field):
    """'Spiro, Theodor and Doe, Jane Q' -> 'Spiro, T., Doe, J. Q.'"""
    out = []
    for person in author_field.split(" and "):
        person = person.strip()
        if "," in person:
            last, firsts = person.split(",", 1)
            initials = " ".join(w[0] + "." for w in firsts.split() if w)
            out.append(f"{last.strip()}, {initials}".strip().rstrip(","))
        else:
            out.append(person)
    return ", ".join(out)
