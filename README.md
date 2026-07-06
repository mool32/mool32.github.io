# mool32.github.io

Source for [Theodor Spiro's researcher landing page](https://mool32.github.io/).

Built as a minimal custom Jekyll site (no theme dependency, native GitHub Pages
build). Content lives in a small data layer:

- **`papers.bib` is the single source of truth for publications.**
  `_data/publications.yml` is **generated** from it — never hand-edit it.
- `_data/projects.yml` — projects grouped by category.
- `_data/news.yml` — the news feed on the homepage.
- `_data/statuses.yml` — the controlled `stage` vocabulary both of the above use.

`scripts/validate.py` guards the whole layer (run before every commit; CI
enforces it). Page-level prose lives in `index.md`, `publications.md`,
`projects.md`, `methodology.md`; styling in `assets/css/style.css`.

## File map

```
├── _config.yml                 # Jekyll site config + nav + social links
├── _layouts/default.html       # Single layout used by every page
├── _includes/                  # head / header / footer partials (+ JSON-LD)
├── _data/
│   ├── publications.yml        # GENERATED from papers.bib — do not edit
│   ├── projects.yml            # Projects grouped by category (/projects/)
│   ├── news.yml                # News items (rendered on /)
│   └── statuses.yml            # Controlled vocabulary for the `stage` field
├── papers.bib                  # SOURCE OF TRUTH: publications (served at /papers.bib)
├── scripts/
│   ├── bibparse.py             # Minimal BibTeX reader (house style)
│   ├── gen_publications.py     # papers.bib -> _data/publications.yml
│   └── validate.py             # Cross-file consistency checks
├── .github/workflows/validate.yml  # Runs generate + validate on push / PR
├── llms.txt                    # AI-agent navigation summary (llmstxt.org)
├── robots.txt                  # Explicit allow for AI/search crawlers
├── assets/css/style.css        # All site styling
├── index.md                    # / (about + selected work + news)
├── publications.md             # /publications/
└── projects.md                 # /projects/
```

## Adding or updating content

Always finish with `python3 scripts/validate.py` returning **0 errors**.

### A new publication

1. Add one BibTeX entry to `papers.bib` (house style: one `field = {value}`
   per line, single-line brace-balanced values, ASCII). Beyond the standard
   citation fields, set the site fields:

   ```bibtex
   @misc{spiro2026yourkey,
     abbr     = {preprint},
     title    = {Your title, plain ASCII (beta not β, NF-kB not NF-κB)},
     author   = {Spiro, Theodor},
     year     = {2026},
     howpublished = {Manuscript, in preparation},
     code     = {https://github.com/mool32/your-repo},
     abstract = {One-paragraph abstract on a single line.},
     bibtex_show = {true},
     order    = {15},                       % display order on /publications
     venue    = {Manuscript, in preparation},% shown next to the title
     stage    = {in-preparation},           % key from _data/statuses.yml
     selected = {true},                     % surface on the homepage
     headline = {true},                     % top "Selected work" block (implies selected)
     status   = {manuscript in preparation} % free-text detail
   }
   ```

2. Regenerate the site data and validate:

   ```bash
   python3 scripts/gen_publications.py
   python3 scripts/validate.py
   ```

   Commit `papers.bib` **and** the regenerated `_data/publications.yml`.

### A new project

Add an entry under the right category in `_data/projects.yml`:

```yaml
    - title: "Human-readable project title"
      url: "https://github.com/mool32/your-repo"
      stage: "in-progress"          # key from _data/statuses.yml
      summary: "1–3 sentences on what it is and the headline result."
      status: "free-text detail shown on /projects (kept rich on purpose)"
```

### A news item

Prepend to `_data/news.yml` (newest first):

```yaml
- date: "Jul 2026"
  text: "One sentence, markdown links allowed. Link internal pages as [text](/page/)."
```

## Controlled vocabulary (`stage`)

`scaffolding · pilot · in-progress · in-preparation · submission-ready ·
report · submitted · under-review · preprint · software-release · live ·
published` — defined with labels in `_data/statuses.yml`. `validate.py` fails
the build on any `stage` outside this set.

## Local preview

Optional — native GitHub Pages builds on push without local setup.

```bash
bundle init && bundle add jekyll
bundle exec jekyll serve   # http://127.0.0.1:4000
```
