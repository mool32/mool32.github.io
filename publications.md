---
layout: default
title: Publications
description: Preprints, manuscripts, and reports by Theodor Spiro.
permalink: /publications/
---

# Publications

All entries below are preprints or manuscripts authored by Theodor Spiro
(ORCID [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346)).
Where applicable, links to PDF, code, and DOI are included.

The canonical BibTeX file is served at [`/papers.bib`]({{ '/papers.bib' | relative_url }})
and is the single source of truth for citation export.

<ul class="pub-list">
{% for p in site.data.publications %}
  <li class="pub">
    <div class="pub-title">{{ p.title }}</div>
    <div class="pub-meta">
      {% if p.abbr %}<span class="abbr">{{ p.abbr }}</span>{% endif %}
      {{ p.authors }} · {{ p.year }} · <em>{{ p.venue }}</em>
    </div>
    <div class="pub-abstract">{{ p.abstract }}</div>
    <div class="pub-links">
      {% if p.arxiv %}<a href="{{ p.arxiv }}">arXiv</a>{% endif %}
      {% if p.doi %}<a href="https://doi.org/{{ p.doi }}">DOI {{ p.doi }}</a>{% endif %}
      {% if p.code %}<a href="{{ p.code }}">code</a>{% endif %}
      {% if p.pdf %}<a href="{{ p.pdf }}">PDF</a>{% endif %}
      {% if p.demo %}<a href="{{ p.demo }}">live demo</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
