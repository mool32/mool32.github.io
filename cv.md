---
layout: default
title: CV
description: Curriculum vitae — Theodor Spiro, independent researcher (cellular perception, aging biomarkers, comparative biology of neural networks).
permalink: /cv/
---

<div class="cv" markdown="1">

<header class="cv-header" markdown="0">
  <h1 class="cv-name">Theodor Spiro</h1>
  <div class="cv-tagline">Independent Researcher — cellular perception, aging biomarkers, and the comparative biology of learning systems</div>
  <div class="cv-contact">
    Vaika Inc. (aging-research nonprofit, Gudkov lab), East Aurora, NY · Based in Tel Aviv, Israel · <a href="mailto:tspiro@vaika.org">tspiro@vaika.org</a><br>
    <a href="https://orcid.org/0009-0004-5382-9346">ORCID 0009-0004-5382-9346</a> ·
    <a href="https://github.com/mool32">github.com/mool32</a> ·
    <a href="https://mool32.github.io/">mool32.github.io</a> ·
    <a href="https://www.linkedin.com/in/theodorspiro">linkedin.com/in/theodorspiro</a>
  </div>
  <div class="cv-grant">Emergent Ventures grant recipient (2026)</div>
  <div class="cv-download"><a href="{{ '/cv.pdf' | relative_url }}">Download PDF →</a></div>
</header>

## Profile

Independent computational researcher; biophysics training (Lomonosov Moscow
State University). Eight 2026 preprints / manuscripts across cellular signaling,
aging biomarkers (412,730 ECG recordings; 823 EEG subjects across two cohorts;
263 GTEx donors plus four species), and the statistical structure of trained
transformers (arXiv:2604.10571; 1,584 controlled ablations on Pythia 410M).
Author and maintainer of **perceptome**, a Python toolkit for cellular
perception analysis (Zenodo DOI; 73/73 tests). 2026 Emergent Ventures
recipient. Methodology inherited from experimental physics: preregistration,
bitwise-reproducible pipelines, bootstrap uncertainty quantification, honest
negative results — formalized as an AI-collaborative research methodology
framework applied across all of the above.

## Software & tools

**perceptome** (2026) — Python toolkit for cellular perception analysis.
44 signaling modules; 9-PC eigenspace built from 154 Human Protein Atlas cell
types; capacity-floor predictor; validity scorecard with three null controls;
8-cell cancer-attractor reference (11 cancers from 11 organ systems converge
toward it during transformation, independently replicated on an external HCC
cohort). Zenodo [10.5281/zenodo.20113468](https://doi.org/10.5281/zenodo.20113468) · 73/73 tests passing.

## Publications & preprints

**Preprints (public, arXiv / bioRxiv / Zenodo):**

- **Universal statistical signatures of evolution in artificial intelligence architectures.** arXiv:2604.10571, 2026. 935 ablation experiments across 161 publications; substrate-independent heavy-tailed DFE.
- **Spectral exponents of the twelve-lead ECG reveal the anatomy of cardiac conduction disorders and a bifurcation between aging and disease.** bioRxiv (submitted), 2026. 412,730 recordings across three continents; CLBBB vs CRBBB AUC ≈ 0.98 cross-population. Zenodo 10.5281/zenodo.19945065.
- **Transcriptomic noise accumulates within tissue identity across human aging.** bioRxiv (post-review v4), 2026. GTEx v8 + Tabula Muris Senis + Calico rat + macaque atlas; aging as systemic noise, not selective accumulation. Zenodo 10.5281/zenodo.19944444.

**Under review:**

- **Waveform asymmetry as a biomarker of neural aging.** *Frontiers in Aging Neuroscience*, 2026. LEMON (N=215) + Dortmund Vital Study (N=608) + 208-subject 5-year longitudinal. Zenodo 10.5281/zenodo.19912202.

**Manuscripts (submission-ready / in preparation):**

- **Functional differentiation generates universal fitness-effect distributions in neural networks.** Submission-ready; target NeurIPS 2026 / ICML Mechanistic Interpretability Workshop. Pythia 410M, 1,584 controlled ablations across 8 checkpoints.
- **Clonal crystallization as a shared signature of bone-marrow aging and neural-network training.** Cross-substrate (Gini, eff_N) framework; caloric restriction rescues 64% of the aging drift in rat bone marrow.
- **Temporal architecture of signaling oscillations predicts cancer gene function across pathways.** Rise/recovery temporal classification; OR = 27.5, p = 3.6 × 10⁻⁹ across 14 pathways.
- **Negative feedback loop architecture as a modular predictor of cancer vulnerability.** 128 NFLs from KEGG; 59-fold CGC enrichment (p = 9 × 10⁻⁴⁴); Irreversible Authority metric (ρ = 0.83).
- **The Oracle's Fingerprint: correlated AI forecasting errors and the limits of bias transmission.** GPT-4o / Claude / Gemini error correlation r = 0.78 on 568 Metaculus forecasts.
- **21,000 attempts to think differently: a Russian adaptation of the Divergent Association Task.** N = 21,159; Cronbach's α = 0.899; live instrument deployed.

**Technical reports:**

- **EEG-based comprehension detection: a multi-dataset non-replication.** Honest negative result; 18 metrics, 5 datasets, 126 subjects.

## Ongoing pilots

- **Self-specific representations localize in emergent attention heads.** Pilot study (Pythia 410M): 29 active meta-heads, all Δ_self > Δ_cross (binomial p < 10⁻⁸). Scaling and cross-model replication in progress before write-up.
- **Epistasis mapping in transformer attention heads.** Cross-model pairwise head-ablation interactions (Pythia 410M, OLMo-2 1B); pre-registered, multi-phase.
- **Developmental epistasis in single-cell RNA-seq.** Biology-side test of the ML epistasis signature on Schiebinger 2019 reprogramming; pilot calibration.
- **Epistemic Fitness Pilot.** Pre-registered (hash-locked) test of whether an LLM can discriminate scientific ideas by future impact.

## Research experience

**Independent computational researcher** · 2020 – present
Independent research program across cellular perception, aging biomarkers,
comparative biology of neural networks, and AI-collaborative research
methodology. Recent concentration on the perceptome framework and single-cell /
transcriptomic analysis; earlier work in computational neuroscience (EEG) and
systems biology. All inferential projects preregistered; full code and data
released on GitHub and Zenodo.

**Affiliated with Vaika Inc.** · 2024 – present
Vaika Inc. is a not-for-profit aging-research organization associated with the
laboratory of Andrei Gudkov (Roswell Park Comprehensive Cancer Center). Aging
manuscripts developed in this affiliation (e.g. pi-tissue-aging) were revised
under Gudkov review.

**B.Sc. / M.Sc. research — Moscow State University, Faculty of Physics** · 2018 – 2022
Supervisor: Prof. L. Yakovenko. Agent-based / cellular-automata modeling of the
cellular response to pro-inflammatory stimuli (TLR4/TLR6 → NF-κB → TNF →
apoptosis), identifying key parameters of the innate-immunity signaling pathway.

## Research methodology

Developer of an **AI-collaborative research methodology framework**
([mool32.github.io/methodology](https://mool32.github.io/methodology/)) —
preregistration discipline, sign-convention locks, locked-vs-working artifacts,
reproducibility standards, and AI-friendly publishing — applied as worked
examples across the portfolio.

## Education

**M.Sc. Biophysics (coursework completed)** — Lomonosov Moscow State University, Faculty of Physics · 2021 – 2022
Computer simulation in biology; physics of biopolymers; physicochemical
kinetics; magnetic radio-spectroscopy in biology and medicine. Thesis defense
not completed due to relocation from Russia in 2022.

**B.Sc. Biophysics** — Lomonosov Moscow State University, Faculty of Physics · 2014 – 2021

**Lyceum 1525, Physics & Mathematics** — Moscow · 2010 – 2014

## Teaching

Eleven years teaching mathematics and physics (ages 11–25), including curriculum
design at Le Sallay Academy (selective international gifted program, 2025–2026),
co-founder and lead teacher of BrainyBara (Israel, 2022–present), and prior
roles at Foxford Online School (Moscow, 2015–2018) and Moscow State University
(Instructor, Advanced Mathematics, 2018–2020). Full teaching record available on
request.

## Professional development

- Evidence-Based Teaching Practices — Harvard University BOK Center · 2022 – 2024
- Psychology of Development and Learning — MSUPE, Moscow · 2020
- Learning to Teach Online — University of New South Wales · 2020

## Grants & honors

- **Emergent Ventures grant** — Mercatus Center · 2026
- **Lomonosov Scientific Conference** — presentation, Moscow · 2021

## Technical skills

- **Programming:** Python (NumPy, Pandas, SciPy, scikit-learn, matplotlib, PyTorch), Git, Bash, LaTeX, SQL basics
- **Methods:** preregistered experimental design, bootstrap uncertainty quantification, distribution fitting with AIC comparison, dimensionality reduction, time-series and signal analysis, agent-based modeling
- **Data domains:** single-cell & bulk RNA-seq, EEG / ECG signals, neural-network interpretability, large-scale forecasting data
- **AI-assisted research:** LLM-integrated analysis pipelines under an explicit preregistration / reproducibility framework

## Languages

Russian (native) · English (C1; all research published in English) · Hebrew (B1)

</div>
