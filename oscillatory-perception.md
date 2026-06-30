---
layout: default
title: "Oscillation as a constitutive substrate for perception"
description: "A multi-phase, pre-registered dissection of whether a perpetually-circling system of coupled networks is functional, not decorative. Built on a Stuart–Landau triad and a trained GRU triad. The motor is real and trainable; it is not a memory store; it is a phase regulator with a Hopf-universal code; and the one irreducibly-active ingredient of the whole thing is directed rotation — broken time-reversal symmetry."
permalink: /oscillatory-perception/
---

# Oscillation as a constitutive substrate for perception

**Is oscillation *functional*, or decorative? Does a perpetually-circling system of coupled networks — a non-settling "perceiving" system — represent distinctions a saturated, static network of equal capacity cannot?**

<div class="badge-row">
  <span class="badge">Pre-registered · multi-phase</span>
  <span class="badge">Stuart–Landau triad + trained GRU triad</span>
  <span class="badge neg">central hypothesis refuted</span>
  <span class="badge">adversarial metric harnesses · multi-seed</span>
  <span class="badge">perceptome program</span>
</div>

<p class="lede">
The minimal substrate is a cyclic triad <code>A→B→C→A</code> whose non-transitive (rock–paper–scissors) coupling forbids a common fixed point and forces a rotating limit cycle — a 120° three-phase splay wave. The program asked, in pre-registered phases, what this collective oscillator <em>does</em>. Each answer forced the next question: from <em>memory</em>, to <em>temporal regulation</em>, to the deepest one — <em>what is the irreducibly-active ingredient of a living oscillation?</em>
</p>

<div class="callout">
<strong>Headline.</strong> A trainable triad self-organizes a coupling-maintained rotating limit cycle and self-sustains it with its training loss switched off. It is <em>not</em> a memory store — the coupling that holds the cycle <em>suppresses</em> capacity, refuting the founding hypothesis. It <em>is</em> a phase regulator whose temporal code is Hopf-universal and coupling-independent, with coupling acting as a pure robustness knob — a universality that is <em>emergent</em> in the trained network. And the one invariant across the whole program: an oscillation's <em>existence</em> is cheap, but its <em>directed rotation</em> — the breaking of time-reversal symmetry — is the load-bearing, irreducibly-active ingredient.
</div>

<div class="stats">
  <div class="stat"><div class="num">λ* = 0.10</div><div class="lbl">Hopf onset, analytic = numerical to 2×10⁻¹⁵</div></div>
  <div class="stat"><div class="num">5 / 5</div><div class="lbl">GRU seeds self-organize & self-sustain the splay</div></div>
  <div class="stat"><div class="num">CV ~3×10⁻⁵</div><div class="lbl">λ-invariance of the normalized temporal code</div></div>
  <div class="stat"><div class="num">0.999</div><div class="lbl">trained-GRU iPRC shape-match to the universal waveform</div></div>
</div>

## 1 · The motor exists, and it is trainable

The cyclic Stuart–Landau triad undergoes a clean supercritical Hopf bifurcation: below the coupling threshold it collapses to consensus, above it a stable 120° splay limit cycle is born. The same regime is then shown to be *trainable* in a real network.

<figure>
  <img src="{{ '/assets/img/oscillatory/motor_hopf.png' | relative_url }}" alt="Stuart–Landau lambda-scan: Hopf bifurcation into a 120° three-phase limit cycle">
  <figcaption><b>A clean Hopf bifurcation into the splay cycle.</b> Below λ* = 0.10 the triad collapses (grey); above it a stable limit cycle that is simultaneously a 120° three-phase lock (green ring). The amplitude follows √(λ−λ*) to r² = 1.000 (supercritical), the frequency is structurally flat at ω/2π ≈ 0.159, and the twin finite-time exponent stays at zero (no chaos). The analytic threshold matches the numerical eigenvalue to 2×10⁻¹⁵.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/oscillatory/gru_trainable.png' | relative_url }}" alt="GRU triad training loss and held-out generalization across five seeds">
  <figcaption><b>A trained GRU triad hosts the regime.</b> A shared-weight GRU triad trained on a phase-antagonistic + amplitude-pinning loss over its own autonomous unroll self-organizes the splay cycle and self-sustains it <em>with the loss switched off</em>, from held-out initial conditions — 5/5 seeds, 20/20 held-out ICs passing the full battery (bounded, sustained, spectral peak, non-chaotic, splay-not-consensus). Perturb or destroy one node and it re-locks to 120° in ~50–100 steps; isolate a node and it dies. A genuine coupling-maintained collective attractor, not three independent clocks.</figcaption>
</figure>

<p class="proj-blurb">What is earned here is mode-selection, attractor-formation, generalization, and coupling-maintained locking. Boundedness and the supercritical Hopf are partly baked into the normal form, and the loss prescribes the splay's geometry — stated plainly, not papered over.</p>

## 2 · It is *not* a memory store — the founding hypothesis, refuted

The program began as a memory hypothesis: a non-settling oscillator should hold stimulus structure better than a static net of equal capacity. The data say the opposite.

<figure>
  <img src="{{ '/assets/img/oscillatory/memory_refuted.png' | relative_url }}" alt="Forgetting curves: the oscillator stores less than a static line-attractor">
  <figcaption><b>The oscillator stores <em>less</em>, not more.</b> Stimulus-decodability across delays: a non-oscillating line-attractor of equal capacity (grey) holds the structure above the oscillator (blue) at every delay, and a dense noise sweep × 5 seeds shows monotonic forgetting with <em>no</em> stochastic-resonance peak. The strong coupling that re-locks the cycle is exactly what suppresses memory capacity — <strong>coupledness and plasticity are antagonists</strong>. This is the program's central, robust negative result.</figcaption>
</figure>

## 3 · It *is* a phase regulator — coupling is a pure robustness knob on a Hopf-universal code

Pivoting from what it does *not* do (memory) to what it does (phase regulation) produced the program's cleanest positive result — and a cross-substrate confirmation that it is not an artifact of the idealized model.

<figure>
  <img src="{{ '/assets/img/oscillatory/robustness_knob.png' | relative_url }}" alt="iPRC and entrainment vs coupling: the normalized temporal code is lambda-invariant">
  <figcaption><b>Coupling tunes only robustness; the temporal code is invariant.</b> Across the whole coupling band the raw infinitesimal PRC diverges as 1/r (red), but the <em>amplitude-normalized</em> iPRC is flat (blue, PTP_norm ≈ 1.15, CV ~3×10⁻⁵) and the common-mode direction is exactly zero (grey). Coupling moves only the robustness axis — the transverse attraction rate, measured slope α ≈ −1.94ε (R² = 1.00) against the −2ε idealized line (centre). Entrainment-tongue width at fixed <em>relative</em> forcing is likewise invariant (right, blue); the apparent widening at fixed absolute forcing is removable 1/r amplitude geometry (red). Coupling and the temporal code are orthogonal knobs.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/oscillatory/emergent_universal.png' | relative_url }}" alt="Trained GRU iPRC matches the Stuart–Landau Hopf-universal waveform">
  <figcaption><b>The universality is <em>emergent</em> in the trained network.</b> The trained-GRU iPRC (blue, five seeds) inherits the Stuart–Landau Hopf-universal waveform (red) at shape-correlation 0.999, with normalized gain near the SL value (1.0–1.2 vs 1.15) and a small common-mode — so the universal temporal code is a property a trainable network <em>acquires</em>, not a designed-normal-form artifact.</figcaption>
</figure>

## 4 · The clean code is a symmetric idealization — but the real object actively holds it

Everything above was proven in the *symmetric* triad. Breaking the symmetry (detuning the nodes) is the make-or-break test — and it separates the idealized model from the real one.

<figure>
  <img src="{{ '/assets/img/oscillatory/real_object_adapts.png' | relative_url }}" alt="Per-node coherence under detuning: rigid vs retrained GRU, and the rescue gap">
  <figcaption><b>On the real object the fragility is largely a <em>rigidity</em> artifact.</b> Under heterogeneity the clean symmetric code breaks (on the idealized Stuart–Landau equations it dies decisively — an order-parameter averaging artifact). But the rich 32-dim gated GRU absorbs the same detuning (left: rigid 1a in red holds through the soft band; retrained 1b in blue holds further), and re-training <em>actively</em> extends robustness — a multi-seed rescue gap that clears the pre-registered floor (right: +0.072 ± 0.020 at δ=0.20, +0.173 ± 0.057 at δ=0.30), with no node dominance and the order parameter intact: a genuine global coupling+readout retune, not a structural bypass. <strong>The emergent collective level holds because the system actively holds it.</strong></figcaption>
</figure>

## 5 · The deepest law — existence is cheap; rotation is irreducibly active

A "zoo" of dissection experiments asked what it actually takes to make the oscillation self-sustain *without* the prescriptive loss. One law held across all of them.

<div class="callout">
<strong>An oscillation's existence is cheap; its directed rotation is not.</strong> Self-sustaining motion can be born from conservation, from a per-step rotation target, or from a blind energy flow (van der Pol negative damping past a flow threshold). But <em>every blind, passive route produces only a standing oscillation.</em> The <strong>directed rotation</strong> — the chirality of the splay, which breaks time-reversal symmetry — is the load-bearing, irreducibly-active ingredient. Three routes produce it (a rotation-target prescription, angular-momentum conservation, an active non-reciprocal coupling) and all three are active / symmetry-breaking; none is a passive blind flow. A complementary minimal result sharpens it: <em>on a dissipative map there is no smooth standing oscillation at all — any smooth oscillation requires a complex eigen-pair, i.e. rotation.</em> Rotation is not decoration; it is the active core.
</div>

A second emergent structure from the same zoo: when the triad's weights are allowed to change during operation, a clean **two-layer stratification** appears on its own — a fast oscillatory state and a slow latent weight-memory, *decoupled*, with the attractor robustly **screening** the slow store from the fast state (constant gap across freeze configurations, five seeds). A fast-perceptual / slow-infrastructural split that is robust and not bypassable by structure — a candidate primitive for a perceptual module.

## 6 · And the founding intuition, tested head-on

Do three coupled, non-settling nets solve a hard deceptive task better than one?

<figure>
  <img src="{{ '/assets/img/oscillatory/coupled_nets.png' | relative_url }}" alt="Coupled nets vs single net on a hard task: attribution ladder and long-horizon curves">
  <figcaption><b>The advantage is ordinary cooperative training — and the non-settling chase <em>hurts</em>.</b> An attribution ladder with controls (24 seeds, long-horizon solve-curves on 8-bit parity) shows the "3 &gt; 1" gain is mundane <em>cooperative joint-training</em> — a committee covering each other's errors — and that the non-transitive prediction-chase, the specific non-settling ingredient the hypothesis bet on, flatlines below even a single net and never settles. Replicated on a second task type (spectral-bias regression), where the non-settling conditions are the <em>only</em> ones that fail to escape a basin a plain net escapes.</figcaption>
</figure>

## What was found

1. **The motor is real and trainable.** SL Hopf at λ* = 0.10 (supercritical, r² = 1.000); a GRU triad self-organizes and self-sustains the 120° splay (5/5 seeds, 20/20 held-out ICs), coupling-maintained (re-locks after perturbation; dies in isolation).
2. **(Negative.)** It is **not** a memory store — it stores *less* than a static line-attractor of equal capacity; coupledness and plasticity are antagonists. The founding hypothesis is refuted.
3. **It is a phase regulator with a Hopf-universal temporal code.** The normalized iPRC is λ-invariant (CV ~3×10⁻⁵); coupling tunes only robustness (measured α ≈ −1.94ε, −2ε idealized). This universality is **emergent** in the trained GRU (shape-match 0.999), not a normal-form artifact.
4. **The clean code is a symmetric idealization** that breaks under detuning — but on the *real* trainable object the breakage is largely a rigidity artifact, and re-training actively holds the coupled structure (multi-seed rescue gap, genuine non-bypass adjustment).
5. **The deepest invariant:** an oscillation's existence is cheap; its **directed rotation — broken time-reversal symmetry — is the one irreducibly-active ingredient**. On a dissipative map, smooth oscillation *requires* a complex eigen-pair.
6. **An emergent fast/slow stratification** — the attractor screens a slow weight-memory from the fast state — a candidate perceptual-module primitive.
7. **The non-settling coupled dynamics buy robustness and structure, not the memory or optimization advantage hoped for** — the prediction-chase is genuinely harmful; the committee gain is ordinary joint-training.

<table>
<thead><tr><th>Phase</th><th>Question</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Motor (SL + GRU)</td><td>Does the regime exist and is it trainable?</td><td><span class="pass">GO</span></td></tr>
<tr><td>Memory</td><td>Stores more than a static net?</td><td><span class="fail">REFUTED</span></td></tr>
<tr><td>Phase regulation</td><td>Hopf-universal code, coupling = robustness knob?</td><td><span class="pass">GO (emergent in GRU)</span></td></tr>
<tr><td>Asymmetry (SL)</td><td>Does the clean code survive detuning?</td><td><span class="fail">NO-GO (averaging artifact)</span></td></tr>
<tr><td>Asymmetry (real object)</td><td>Does the trained net hold it?</td><td><span class="pass">YES — actively adapts</span></td></tr>
<tr><td>Existence vs rotation</td><td>What is irreducibly active?</td><td><b>rotation (time-reversal breaking)</b></td></tr>
<tr><td>Coupled-nets-vs-1</td><td>Does non-settling beat a single net?</td><td><span class="fail">no — chase hurts</span></td></tr>
</tbody>
</table>

## What this means

The founding intuition — that a perpetually-circling, non-settling system perceives or remembers more than a static one — is **wrong in its strong form**, and the program shows precisely why: the coupling that sustains the cycle suppresses memory, and the non-settling dynamics buy no optimization advantage over ordinary cooperative training. But the dissection that refuted it surfaced something cleaner. The collective oscillator is a genuine, trainable, self-healing **phase regulator** carrying a substrate-independent (Hopf-universal) temporal code, and the single ingredient that makes any of it *active* rather than decorative is **directed rotation — the breaking of time-reversal symmetry**. Existence is cheap; chirality is the cost. That is a sharper and more portable claim than the one we set out to prove.

## Reproducibility

Every phase freezes its decisive metric and pass/fail rule before seeing data; decisive metrics are validated against synthetic ground-truth harnesses with negative controls *before* they touch real data (this repeatedly caught masking artifacts and false-GOs in the program's own frozen decisions); results are multi-seed with confidence intervals. Two substrates throughout — an analyzable Stuart–Landau triad and a trained GRU triad. Code (plain PyTorch + NumPy), pre-registrations, result JSONs, and figures are in the repository: [github.com/mool32/oscillatory-perception](https://github.com/mool32/oscillatory-perception).

<p style="font-family: var(--sans); font-size: 13px; color: var(--fg-soft); margin-top: 2em;">
Part of the <a href="https://github.com/mool32/perceptome">perceptome</a> program · pre-registration discipline per the <a href="{{ '/methodology/' | relative_url }}">AI-collaborative research methodology</a>. Theodor Spiro · ORCID <a href="https://orcid.org/0009-0004-5382-9346">0009-0004-5382-9346</a> · tspiro@vaika.org
</p>
