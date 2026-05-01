# mool32.github.io

Source for [Theodor Spiro's researcher landing page](https://mool32.github.io/).

Built as a minimal custom Jekyll site (no theme dependency, native GitHub Pages
build). Edit `_data/*.yml` to add publications, projects, and news; edit
`index.md`, `publications.md`, `projects.md` for page-level content; edit
`assets/css/style.css` for styling.

## File map

```
├── _config.yml                 # Jekyll site config + nav + social links
├── _layouts/default.html       # Single layout used by every page
├── _includes/
│   ├── head.html               # <head> (title, description, CSS link)
│   ├── header.html             # Top nav (renders site.nav from _config.yml)
│   └── footer.html             # Footer (contact + social links)
├── _data/
│   ├── publications.yml        # All publications (rendered on /publications/)
│   ├── projects.yml            # Projects grouped by category (rendered on /projects/)
│   └── news.yml                # Last few news items (rendered on /)
├── _bibliography/papers.bib    # Canonical BibTeX (linked from /publications)
├── assets/css/style.css        # All site styling
├── index.md                    # / (about + selected work + news)
├── publications.md             # /publications/
└── projects.md                 # /projects/
```

## Local preview

Optional. Native GitHub Pages will build on push without local setup. For
local iteration:

```bash
bundle init
bundle add jekyll
bundle exec jekyll serve
# open http://127.0.0.1:4000
```
