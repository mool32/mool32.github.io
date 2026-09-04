---
layout: default
title: "Theodor Spiro — cellular perception, aging biomarkers, learning systems"
description: "Independent computational researcher (Vaika Inc., Tel Aviv). Cancers of all lineages converge on the placental cytotrophoblast; aging biomarkers across ECG, EEG and transcriptome. Pre-registered, with code and a DOI behind every claim."
---

<section class="hero">
  <h1 class="name">Theodor Spiro</h1>
  <div class="id-line">
    Independent researcher · Vaika Inc. (aging-research nonprofit) · Based in Tel Aviv, Israel ·
    <a href="https://orcid.org/0009-0004-5382-9346">ORCID 0009-0004-5382-9346</a> ·
    <a href="mailto:tspiro@vaika.org">tspiro@vaika.org</a>
  </div>
  <div class="id-line id-line-grant">
    Emergent Ventures grant recipient (2026)
  </div>

  <p class="positioning">
    I build coordinate systems for cellular state, then test what they predict —
    predictions locked before the data, failures published next to the wins.
    The current result: <strong>the malignant cells of 25 cancers, from every major
    lineage, converge on one normal human cell type — the placental
    cytotrophoblast</strong> — a state that malignancy deepens about sixfold inside
    a patient's own tissue.
  </p>
</section>

<figure>
  <img src="{{ '/assets/img/cancer/convergence-eigenspace.png' | relative_url }}"
       alt="154 normal human cell types plotted in the perceptome eigenspace (PC1 × PC4), with the placental cytotrophoblast marked as the anchor that 25 cancers converge on and the megakaryocyte as a secondary">
  <figcaption>
    A map of 154 normal human cell types, built from 44 signaling modules using
    <strong>no cancer data at all</strong>. Project 25 quality-controlled cancer datasets into
    it afterwards and the malignant cells land in one small region — anchored by the
    placental cytotrophoblast, the normal cell that already invades tissue, proliferates,
    and evades immunity.
    <a href="https://doi.org/10.5281/zenodo.20542130">Preprint · DOI</a>
  </figcaption>
</figure>

## Two directions

**1 · Cellular perception — what a cell can sense, and where cancer takes it.**
[perceptome](https://github.com/mool32/perceptome) treats 44 signaling pathways as a
cell's perceptual repertoire and places any cell on one 9-dimensional map (Python
toolkit, Zenodo DOI, 74/74 tests). The
[cancer-convergence result](https://doi.org/10.5281/zenodo.20542130) above is what
that map was built to test. A related strand asks whether the same architecture holds
in neurons: proteostasis modules
[causally enable memory consolidation](/memory-consolidation/) — shown by a knockout
that removes one arm of the machinery and the memory with it.

**2 · Aging biomarkers, replicated across substrates.**
The same question — what degrades measurably with age — asked on three unrelated
signals, each with cross-population replication as the default bar:
the [twelve-lead ECG](https://doi.org/10.5281/zenodo.19945065) (412,730 recordings,
three continents), [EEG waveform shape](https://doi.org/10.5281/zenodo.19912202)
(823 adults, two cohorts, 5-year follow-up), and the
[transcriptome](https://doi.org/10.5281/zenodo.19944444) (GTEx plus three species).

Everything else — the comparative biology of neural networks, cognition instruments,
cross-substrate methods — lives on [Projects →]({{ '/projects/' | relative_url }}).

## Every claim here is checkable

That is the point of the setup, not a footnote:

- **Predictions are locked before the analysis.** Hypotheses, metrics and pass/fail
  thresholds go into a hash-stamped pre-registration first; verdicts cite the locked file.
- **The failures are published too.** A refuted founding hypothesis in
  [oscillatory perception](/oscillatory-perception/), a
  [pre-registered negative](/nn-as-sensor/) where the method loses to a linear baseline,
  and an [EEG non-replication](https://github.com/mool32/eeg-connectivity-contrast)
  across five datasets — all written up in full rather than dropped.
- **Every result carries its code and a DOI.** Nothing here rests on a claim you cannot
  re-run.
- **This site is itself validated.** Publications are generated from a single BibTeX
  source and checked in CI, so the record cannot quietly drift out of sync.

[How the work is validated →]({{ '/methodology/' | relative_url }})

## Selected work

<ul class="pub-list pub-list-headline">
{% assign headline = site.data.publications | where: "headline", true %}
{% for p in headline %}
  <li class="pub pub-headline">
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

## News

<div class="news">
<ul>
{% for item in site.data.news limit: 5 %}
  <li>
    <span class="news-date">{{ item.date }}</span>
    <span class="news-text">{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</span>
  </li>
{% endfor %}
</ul>
</div>

## About

I'm an independent computational researcher based in Tel Aviv. My background is in
biophysics (Lomonosov Moscow State University, Faculty of Physics), where my early
work was computational modeling of cellular signaling — the thread that runs directly
into the cellular-perception work anchoring the portfolio today. I am a 2026
[Emergent Ventures](https://www.mercatus.org/emergent-ventures) grant recipient.

The independent research program runs from **2020**. Since **2024** I have been
affiliated with **Vaika Inc.**, a not-for-profit aging-research organization, where my
aging manuscripts are developed and reviewed.

I publish under one canonical name everywhere: Theodor Spiro
(ORCID [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346)). Manuscripts and
code are released at [github.com/mool32](https://github.com/mool32) and on Zenodo / arXiv.

[Projects by theme →]({{ '/projects/' | relative_url }}) · [Curriculum vitae →]({{ '/cv/' | relative_url }})
