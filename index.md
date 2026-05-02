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
    My work is at the intersection of biomarkers of biological aging and
    statistical signatures of neural-network training. Recent papers span
    cardiac conduction, transcriptomic noise, EEG aging, oscillatory
    cancer signaling, and AI-architecture evolution.
  </p>
</section>

## About

I'm an independent researcher (Vaika Inc., East Aurora, NY) with a biophysics
background. I work primarily on two threads: aging biomarkers across substrates
(EEG, ECG, bulk and single-cell transcriptome) and substrate-independent
statistical signatures of differentiation that connect biological aging to
neural-network training.

Recent work includes a [cross-population replication of an ECG conduction-anatomy
biomarker across 412,730 recordings](https://github.com/mool32/ecg-spectral-exponents),
a [variance-decomposition analysis of transcriptomic
aging](https://github.com/mool32/pi-tissue-aging) that adjudicates between
systemic-noise and selective-accumulation models, and [an arXiv paper showing
that the distribution of fitness effects of architectural modifications matches
biological DFEs](https://arxiv.org/abs/2604.10571) across 935 ablation experiments.

I publish under one canonical name everywhere: Theodor Spiro
(ORCID [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346)).
Manuscripts and code are released on GitHub at
[github.com/mool32](https://github.com/mool32) and on Zenodo / arXiv.

## Currently

Writing up [Paper 2 (LLM track)](https://github.com/mool32/functional-differentiation-dfe)
on functional differentiation in transformer training, with a second-order
[epistasis](https://github.com/mool32/epistasis-transformer-heads) extension
running on Pythia 410M and OLMo-2 1B. In parallel, finalizing the
[clonal-crystallization cross-domain bridge](https://github.com/mool32/clonal-crystallization-aging)
for submission.

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

[How I organize research projects (methodology + repository conventions) →]({{ '/methodology/' | relative_url }})
