---
layout: default
title: "Neural-network fitting as a structure sensor"
description: "A pre-registered test of whether an autoencoder's fitting process can sense hidden structure in single-cell data, calibrated on immune aging (GSE233321) and cross-checked against the perceptome eigenspace. An honest negative result with a precise scope condition."
permalink: /nn-as-sensor/
---

# Neural-network fitting as a structure sensor

**Can the *fitting process* of a plain autoencoder act as a sensor for hidden structure in single-cell data — recovering a biological axis it was never shown?**

<div class="badge-row">
  <span class="badge neg">Honest negative result</span>
  <span class="badge">Pre-registered · A∧B∧C∧D</span>
  <span class="badge">GSE233321 · immune lifespan</span>
  <span class="badge">prototype, confirmed 2 seeds × d{16,32}</span>
</div>

<p class="lede">
An undercomplete autoencoder is trained only to reconstruct gene expression — it never sees donor age. If age nonetheless surfaces in its compressed code, the fit itself would be a usable sensor. Calibrated on the age axis as ground truth, the method <strong>fails its own pre-committed bar</strong> — and the way it fails is informative.
</p>

<div class="callout">
<strong>Headline.</strong> The autoencoder never beats a linear baseline (PCA) at recovering age, across two seeds and both latent dimensions. Worse, <em>training erodes</em> the signal: age is most decodable at initialisation and declines over 100 epochs. A synthetic positive control shows the instrument <em>can</em> beat linear methods — but only in a geometric regime that single-cell data does not occupy. The negative is a property of the data geometry, not a fluke or a biased test.
</div>

<div class="stats">
  <div class="stat"><div class="num">167</div><div class="lbl">donors (effective n) · CD4 T cells</div></div>
  <div class="stat"><div class="num">0 / 2</div><div class="lbl">configs where the latent beats matched PCA</div></div>
  <div class="stat"><div class="num">p = 0.001</div><div class="lbl">latent ↔ perceptome eigenspace (CCA)</div></div>
  <div class="stat"><div class="num">3</div><div class="lbl">pre-registered amendments, decided before looking</div></div>
</div>

## The design

One autoencoder architecture, three matched data conditions, and a pre-committed pass/fail rule fixed *before* any result was seen.

- **Ground truth.** Donor age is a *donor-level* variable, so every probe uses **leave-donors-out** cross-validation (effective n = 167 donors, not cells). A cell-level split would measure donor leakage, not an age law.
- **Three conditions.** `REAL` (untouched) · `GENE-PERMUTED` (co-expression destroyed, marginals kept — an artifact floor) · age-shuffled (a within-source permutation null for the probe).
- **Verdict A∧B∧C∧D**, locked in advance: **A** age beats the within-source null · **B** the effect does not reproduce on gene-permuted data · **C** the latent beats a *matched* linear PCA · **D** the signal survives a data-source (batch) control.
- **Independent cross-check** against the [perceptome](https://github.com/mool32/perceptome) 9-PC eigenspace — a biology-curated coordinate system built from 154 cell types.

## What the fit reveals

The sensor signal is not the reconstruction loss. It is read three ways, each against a matched null.

<figure>
  <img src="{{ '/assets/img/paper9/fig_effdim.png' | relative_url }}" alt="Effective dimensionality: REAL vs gene-permuted">
  <figcaption><b>Structure is present.</b> Participation ratio of the latent covariance is far lower for real data than for the gene-permuted floor (6.2 vs 14.4 at d=16) — the autoencoder is compressing genuine co-expression, not noise. So the question is not <em>whether</em> there is structure, but whether the fit exposes <em>age</em> better than a linear method.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/paper9/fig_age_recovery.png' | relative_url }}" alt="Age recovery: autoencoder latent vs matched linear baselines">
  <figcaption><b>The autoencoder loses to linear PCA (criterion C fails).</b> Leave-donors-out age recovery for the latent vs matched PCA-d, PCA-50, raw HVG, and the shuffled-age null. The latent (0.85) sits <em>below</em> every linear baseline on the lifespan axis, and below them again on the harder adult-aging axis. A from-scratch neural compression adds nothing over ordinary linear statistics — the lesson the Arc Virtual Cell Challenge taught at scale, reproduced here.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/paper9/fig_learning_order.png' | relative_url }}" alt="Learning order: age and cell-type decodability decline over training">
  <figcaption><b>Training erodes the signal.</b> Both age (blue, leave-donors-out) and cell type (pink) are maximally decodable at epoch 1 — when the untrained network is essentially a random projection that preserves linear structure — and decline monotonically as the bottleneck specialises for reconstruction. The fit moves <em>away</em> from the target it was hoped to expose. Confirmed across two seeds and both latent dimensions.</figcaption>
</figure>

## The instrument is sound — but narrowly

Could a linear probe be hiding a nonlinear success? A synthetic positive control settles it.

<figure>
  <img src="{{ '/assets/img/paper9/fig_nonlinear_control.png' | relative_url }}" alt="Nonlinear positive control across three synthetic regimes">
  <figcaption><b>The autoencoder beats matched PCA only in one regime.</b> Three synthetic targets through the same pipeline. On a high-linear-rank, low-intrinsic-dimension manifold (CURVE), the d=2 autoencoder beats matched PCA-2 (criterion C <em>can</em> fire — the test is fair). On a linear target or a low-rank manifold (ROLL), it cannot. And in every case, giving PCA a few more components ties or wins. Real scRNA-seq has low effective rank (≈50 PCs) and a linearly-dominated age axis — outside the firing window.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/paper9/fig_objective_experiment.png' | relative_url }}" alt="Objective-function experiment: MSE vs negative-binomial vs information-bottleneck">
  <figcaption><b>The objective explains the erosion — but not the failure.</b> Holding everything fixed and varying only the training loss: a count-appropriate negative-binomial likelihood (unsupervised) <em>removes</em> the learning-order decay (slope flips negative → positive), confirming that MSE-on-counts was eroding the signal. But it only reaches parity with PCA, never a decisive win. An aligned objective fixes the dynamics; the data geometry still caps the utility.</figcaption>
</figure>

## The independent cross-check

<figure>
  <img src="{{ '/assets/img/paper9/fig_perceptome.png' | relative_url }}" alt="Perceptome cross-check: CCA and inflammaging alignment">
  <figcaption><b>The latent re-derives the perceptome eigenspace, but not its aging axis.</b> Cross-validated CCA between the autoencoder latent and the 9-PC perceptome coordinates gives three significant shared axes (0.95 / 0.56 / 0.74, all permutation p = 0.001) — the data-driven factorisation independently recovers the biology-curated one. Yet the latent's age direction is <em>orthogonal</em> to the reference inflammaging direction (cosine −0.78 / −0.50, not significant), consistent with the prior that perceptome axes are pathology-specific, not healthy-aging.</figcaption>
</figure>

## What was found

1. **(Negative.)** The autoencoder does **not** beat matched linear PCA at recovering age — 0/2 across seeds × dims (lifespan latent 0.86–0.89 vs PCA 0.90–0.93; adult 0.35–0.40 vs 0.44–0.48). More capacity (d=32) does not rescue it, so the bottleneck is the *data geometry*, not the network size.
2. **Training erodes the signal under MSE.** Age decodability is highest at initialisation (≈ random projection) and declines over 100 epochs; the unsupervised fit specialises for reconstruction and overwrites the linearly-accessible age axis.
3. **Naive adult-aging recovery is partly a batch artifact.** The latent predicts dataset-of-origin at 0.94 balanced accuracy (chance 0.33); within a single source the adult signal collapses to ρ ≈ 0.14 (n.s.). The pre-registered source control (D) catches exactly this.
4. **The latent independently re-derives the perceptome eigenspace** (CCA 0.95 / 0.56 / 0.74, p = 0.001) but **not its aging axis** (cosine to inflammaging −0.78 / −0.50, n.s.) — perceptome axes look pathology-specific.
5. **The instrument is sound but the regime is wrong.** A positive control confirms the autoencoder *can* beat matched PCA — only when intrinsic-dim < bottleneck < linear-rank. Single-cell data (low effective rank, linear age) is outside that window; no objective changes that.

<table>
<thead><tr><th>Target</th><th>A · beats null</th><th>B · not on permuted</th><th>C · beats PCA</th><th>D · source-robust</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Lifespan (167 donors)</td><td>✅</td><td>✅</td><td><span class="fail">❌</span></td><td>✅</td><td><span class="fail">FAIL</span></td></tr>
<tr><td>Adult-aging (85 donors)</td><td>✅</td><td>✅</td><td><span class="fail">❌</span></td><td><span class="fail">❌</span></td><td><span class="fail">FAIL</span></td></tr>
</tbody>
</table>

## What this means

The result is a clean, mechanistically dissected negative. Autoencoder-fitting-as-a-sensor beats linear baselines **only** on data whose structure is nonlinearly entangled — high linear rank, low intrinsic dimension. Standard single-cell expression, after the usual preprocessing, is well-approximated by ~50 linear components and carries a *linearly-dominated* age axis; there is simply no nonlinear advantage for the bottleneck to find that a generous linear method does not already capture. The training objective controls whether the fit *erodes* the signal (it does under MSE; a count-appropriate loss does not), but it cannot manufacture an advantage the geometry does not offer.

A positive by-product: the unsupervised latent independently re-derives the hand-built [perceptome](https://github.com/mool32/perceptome) eigenspace — evidence that the curated coordinate system is real structure in the data — while declining to align with its aging direction, exactly as a pathology-specific framework should.

The honest conclusion for the method: it needs a nonlinearly-encoded target to be worth the machinery. Immune age is the wrong target — and now we know precisely why.

## Reproducibility

The full pipeline is pre-registered (three locked amendments), leave-donors-out throughout, fixed seeds, and packaged as a one-click notebook (data download → QC → train ×{real, gene-permuted} → A∧B∧C∧D verdict → learning-order → perceptome cross-check → figures). Every headline number is reported with its matched control and with variance across seeds and folds. **Dataset:** [GSE233321](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE233321) (healthy human immune system across the lifespan, 167 donors). Code, pre-registration, and the full report — *repository in preparation* under [github.com/mool32](https://github.com/mool32).

<p style="font-family: var(--sans); font-size: 13px; color: var(--fg-soft); margin-top: 2em;">
Part of the <a href="https://github.com/mool32/perceptome">perceptome</a> program · methodological negative result · pre-registration discipline per the <a href="{{ '/methodology/' | relative_url }}">AI-collaborative research methodology</a>. Theodor Spiro · ORCID <a href="https://orcid.org/0009-0004-5382-9346">0009-0004-5382-9346</a> · tspiro@vaika.org
</p>
