---
layout: default
title: "Proteostasis modules causally enable memory consolidation"
description: "A pre-registered, cross-dataset dissection of memory consolidation in the perceptome framework. Consolidation resolves into a three-layer architecture — a perception layer that senses encoding, a sentinel that senses proteostatic load, and a constructive layer that builds the machinery — with region-specific implementations and direct causal evidence from TLR9 knockout."
permalink: /memory-consolidation/
---

# Proteostasis modules causally enable memory consolidation

**When a neuron converts a fleeting experience into a lasting memory, which of its cellular subsystems switch on — and in what order?** Scored across seven transcriptomic datasets with the predictions fixed in advance, consolidation resolves into a clean, layered cellular program — and one arm of it is shown to be *causally* required.

<div class="badge-row">
  <span class="badge">Pre-registered · 26 predictions</span>
  <span class="badge">7 datasets + 2 replication</span>
  <span class="badge">Causal · TLR9 knockout</span>
  <span class="badge">32 literature experiments · 0 contradictions</span>
</div>

<p class="lede">
Memory consolidation is usually studied as two separate literatures — the signaling/immediate-early-gene story (CREB, ERK) and the proteostasis story (chaperones, the unfolded protein response, autophagy) — that rarely meet. Read through one common vocabulary of 44 cellular sensing modules, they turn out to be halves of a single, temporally-ordered architecture.
</p>

<div class="callout">
<strong>Headline.</strong> Consolidation engages a <strong>three-layer architecture</strong>: a <strong>perception layer</strong> (cAMP/CREB, ERK/FOS, NFAT, NPAS4) that senses the encoding trigger — transient, post-translational; a <strong>sentinel sub-layer</strong> (UPR-ATF6, ATF4, PERK) that senses accumulated proteostatic load — persistent; and a <strong>constructive sub-layer</strong> (HSF1, NRF2, autophagy, IRE1) that actively builds new proteostatic machinery. The three separate cleanly in time, mechanism, and cell-biological role — and TLR9 knockout selectively removes one arm, with a matching memory deficit.
</div>

<div class="stats">
  <div class="stat"><div class="num">26</div><div class="lbl">predictions registered before analysis</div></div>
  <div class="stat"><div class="num">d = +1.40</div><div class="lbl">HSF1 (build machinery) at 24 h — larger than CREB</div></div>
  <div class="stat"><div class="num">60–75%</div><div class="lbl">of ER-chaperone induction lost in TLR9 knockout</div></div>
  <div class="stat"><div class="num">28 / 32</div><div class="lbl">published perturbations predicted correctly · 0 contradictions</div></div>
</div>

## The three layers, and how they separate

Every module is read two ways: **readiness** (are the components transcribed?) and **activity** (are the target genes actually induced?). That distinction is what resolves the architecture — several key modules activate post-translationally, invisible to component-only scoring.

- **Perception** — cAMP/CREB, ERK/FOS, NFAT, and NPAS4 sense the encoding event. Activation is **transient** and post-translational: CREB target activity is *d* = +0.80 in dentate gyrus at 24 h and back to *d* = −0.19 by 96 h.
- **Sentinel** — the UPR-ATF6 / ATF4 / PERK axis senses accumulated protein-folding load. It **persists**: UPR-ATF6 is still climbing at *d* = +1.04 at 96 h, when perception has fully relaxed — and the elevation is enriched in engram-like neurons, not a uniform tissue-wide stress response.
- **Constructive** — HSF1, NRF2, autophagy, and IRE1 **build** the folding and quality-control machinery. This is the largest signal in the whole perceptome during active consolidation (HSF1 *d* = +1.40, exceeding CREB by 75%), and it re-engages at recall.

The layers dissociate along a temporal axis (transient vs persistent), a regulatory axis (post-translational vs transcriptional), and a functional axis (sense the trigger → sense the load → build the machinery).

## Same architecture, region-specific implementation

Four amygdala predictions — that hippocampal architecture would simply generalize — were **pre-registered and all failed**, in a structured way that is the point rather than a disappointment.

- **Hippocampus (dentate gyrus)** induces *both* ER and cytoplasmic chaperones plus autophagy — the signature of **building new synapses**.
- **Amygdala** induces ER chaperones but *suppresses* cytoplasmic chaperones and autophagy, against a **1.8-fold higher baseline chaperone reserve** — the signature of **swapping receptors in existing synapses**. It already has the capacity; it reallocates rather than builds.

Two opposite transcriptional solutions to the same constraint, against different starting reserves.

## The causal test

Correlations across timepoints establish the architecture; one genetic manipulation makes it causal. In *Tlr9*⁻ᐟ⁻ mice (Jovasevic et al., 2024), **ER-chaperone induction is selectively blunted by 60–75%** across hippocampal subfields while cytoplasmic chaperones are preserved — a clean, arm-specific lesion of the infrastructure — **and those mice show impaired contextual fear memory**. Remove one branch of the constructive layer, lose the memory.

## It agrees with three decades of perturbations

The model was checked against **32 published proteostasis-manipulation experiments** — HSP90 inhibitors, HSP70, chemical chaperones, XBP1, ISRIB, PERK, autophagy, mTOR, NRF2, HSF1 knockouts — spanning mouse, rat, and fly. It predicted the correct memory direction in **28 (full match), 4 partial, and zero contradictions**. It even resolves a standing paradox: HSP90 inhibitors are anti-cancer drugs that *enhance* memory — because inhibiting HSP90 releases HSF1 and turns the constructive layer **up**.

## A method that travels

The **readiness vs activity** distinction — scoring a module by its target-gene output, not just component abundance — is a general refinement. It captured post-translational activation that component scoring misses, and it validates cleanly out of domain: **zero sign reversals** in Alzheimer's neurons (0/8) and a **9.4%** reversal rate across four aging tissues. NPAS4 is proposed as the 44th canonical [perceptome](https://github.com/mool32/perceptome) module — the first tissue-restricted one.

The framework yields a falsifiable therapeutic prediction: **chemical chaperones** (4-PBA, TUDCA) should rescue memory deficits in TLR9-deficient and aging-impaired contexts.

---

<p class="lede">
Built on the <a href="https://github.com/mool32/perceptome">perceptome</a> framework · sole-author manuscript, submission-ready · pre-registration and code archive to accompany the preprint. Contact <a href="mailto:tspiro@vaika.org">tspiro@vaika.org</a>.
</p>
