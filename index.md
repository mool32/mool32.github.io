---
layout: default
title: About
description: Theodor Spiro — independent researcher at Vaika Inc.
---

<section class="hero">
  <h1 class="name">Theodor Spiro</h1>
  <div class="id-line">
    Independent researcher · Vaika Inc., East Aurora, NY ·
    <a href="https://orcid.org/0009-0004-5382-9346">ORCID 0009-0004-5382-9346</a> ·
    <a href="mailto:tspiro@vaika.org">tspiro@vaika.org</a>
  </div>

  <p class="positioning">
    Currently centered on <strong><a href="https://github.com/mool32/perceptome">perceptome</a></strong>
    — a framework treating cellular signaling pathways as a perceptual repertoire,
    with a Python toolkit (44 modules, 9-PC eigenspace, cancer attractor reference).
    Alongside: aging biomarkers across substrates (EEG, ECG, transcriptome),
    the comparative biology of neural networks (DFE and epistasis applied to LLM
    training), and a developing framework for doing science in active collaboration
    with AI.
  </p>
</section>

## About

I'm an independent researcher (Vaika Inc., East Aurora, NY) with a biophysics
background. The portfolio organizes into six directions:

1. **Cellular perception** — [perceptome](https://github.com/mool32/perceptome) (toolkit + framework + a growing family of papers) and related work on oscillatory signaling and cancer
2. **Comparative biology of neural networks** — DFE, epistasis, and population-genetics tools applied to trained transformers
3. **Aging research / biomarkers** — cross-population replications on cardiac, transcriptomic, and EEG substrates
4. **Cognition, education, experiments, social projects** — instruments and studies of human cognition
5. **Methods & cross-substrate work** — bridges, methodological contributions, and honest negative results
6. **AI-collaborative research methodology** — the framework behind all of the above, applied as worked examples

I publish under one canonical name everywhere: Theodor Spiro
(ORCID [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346)).
Manuscripts and code are released on GitHub at
[github.com/mool32](https://github.com/mool32) and on Zenodo / arXiv.

## Currently

[perceptome v0.3](https://github.com/mool32/perceptome) is the active center
of the work — a Python toolkit for cellular perception analysis with a 9-PC
eigenspace, capacity-floor predictor, validity scorecard, and an 8-cell cancer
attractor reference. A family of papers around the framework is in
preparation. In parallel:
[functional-differentiation DFE](https://github.com/mool32/functional-differentiation-dfe)
manuscript writeup, the
[epistasis](https://github.com/mool32/epistasis-transformer-heads) Tier-2
extension on Pythia 410M / OLMo-2 1B, and the
[clonal-crystallization cross-substrate bridge](https://github.com/mool32/clonal-crystallization-aging)
preparing for submission.

## News

<div class="news">
<ul>
{% for item in site.data.news %}
  <li>
    <span class="news-date">{{ item.date }}</span>
    <span class="news-text">{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</span>
  </li>
{% endfor %}
</ul>
</div>

## Selected work

<ul class="pub-list">
{% assign selected = site.data.publications | where: "selected", true %}
{% for p in selected %}
  <li class="pub">
    <div class="pub-title">{{ p.title }}</div>
    <div class="pub-meta">
      {% if p.abbr %}<span class="abbr">{{ p.abbr }}</span>{% endif %}
      {{ p.authors }} · {{ p.year }} · <em>{{ p.venue }}</em>
    </div>
    <div class="pub-abstract">{{ p.abstract }}</div>
    <div class="pub-links">
      {% if p.arxiv %}<a href="{{ p.arxiv }}">arXiv</a>{% endif %}
      {% if p.doi %}<a href="https://doi.org/{{ p.doi }}">DOI</a>{% endif %}
      {% if p.code %}<a href="{{ p.code }}">code</a>{% endif %}
      {% if p.demo %}<a href="{{ p.demo }}">live demo</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>

[Full publication list →]({{ '/publications/' | relative_url }})

[Projects organized by theme →]({{ '/projects/' | relative_url }})

[AI-collaborative research methodology →]({{ '/methodology/' | relative_url }})
