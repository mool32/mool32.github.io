---
layout: default
title: Methodology
description: How research projects are organized, preregistered, and released — the conventions used across the mool32 portfolio.
permalink: /methodology/
---

# Research methodology and repository conventions

This document is the canonical reference for how I organize, preregister, and
release research projects. It exists so that:

- I do not re-derive structural decisions for each new project
- Collaborators (and AI agents) reading any one repository can locate the
  underlying conventions in a single place
- The discipline of the work — preregistration, sign conventions, locked-vs-
  working artifacts, reproducibility — is itself part of the public record

The running examples throughout are the **epistasis pair**:
[epistasis-transformer-heads](https://github.com/mool32/epistasis-transformer-heads)
(ML side, in progress) and
[developmental-epistasis-scrna](https://github.com/mool32/developmental-epistasis-scrna)
(biology side, pilot stage). Together they exhibit every principle below.

---

## 1. Project lifecycle

Every project moves through three stages, in this order. **Skipping a stage
or running them out of order is the single most common cause of wasted work
and post-hoc rationalization.**

### Stage A — Scaffolding

- Exploratory analyses, design notes, sign-convention definitions
- No preregistration locked yet
- README is honest about the stage: status badge says "Scaffolding"
- No claims of biological/empirical findings; only methodological scoping

Example: `developmental-epistasis-scrna`'s
[`methodology/observational_epistasis_limits.md`](https://github.com/mool32/developmental-epistasis-scrna/blob/main/methodology/observational_epistasis_limits.md)
asks whether scRNA-seq alone can yield ε reliably *before* any biology pilot
is run.

### Stage B — Pilot

- Calibration runs against a small sample
- Preregistration drafted but not yet locked
- Goal is to verify the apparatus measures *something stronger than noise*
  before claiming to measure a biological / ML signal
- A machine-readable verdict file gates the transition to Stage C

Example: `developmental-epistasis-scrna/pilot/pilot_calibration_verdict.json`
is the gate. Until it passes, no preregistration is locked and no
decision-defining analysis is run.

### Stage C — Full run under locked preregistration

- Preregistration locked (see §2)
- Full analysis runs
- All numerical results bootstrap-quantified (see §6)
- Verdicts computed against the *locked* preregistration, never the working
  draft

**Do not** run "exploratory" analyses on the full data and then write a
preregistration that matches what you found. The point of preregistration is
to separate the question from the answer.

---

## 2. Preregistration discipline

### Locked vs working drafts

Two files exist for every preregistered analysis:

- `analyses/tier1_preregistration_v1_pythia_410m.md` — working draft, edited freely
- `analyses/tier1_preregistration_v1_pythia_410m.LOCKED.md` — frozen, never edited

Both committed. `LOCKED` is the contract; the working draft is for thinking.

The lock event is a git commit with a clear message
("Lock Tier 1 preregistration v1 for Pythia 410M") and is referenceable by
SHA. Any verdict computation must cite the LOCKED file path and the commit
SHA in its output.

### What goes in a preregistration

Every preregistration contains:

1. **Hypotheses** — primary, secondary, and alternative, each with a
   pre-specified statistical test
2. **Pass criteria** — concrete numerical thresholds (effect size, *p*
   threshold, agreement-with-witness ratio, bootstrap CI exclusion)
3. **Failure modes named in advance** — what would refute the hypothesis,
   not just what would support it
4. **Order of operations** — exactly which step runs first, what its output
   is, and how that output gates the next step
5. **Sample / data scope** — exactly which checkpoints, which subjects,
   which subsets of the data, locked at the time of the lock

Versioning: when the preregistration changes substantively, a new version
is created (`v2_multicheckpoint`, `v3_olmo2_1b`) rather than editing the
prior LOCKED file. The history is preserved.

Example: `epistasis-transformer-heads/analyses/` has v1 (Pythia 410M), v2
(multi-checkpoint), v3 (OLMo-2 1B), each as both `.md` and `.LOCKED.md`.
Six files for three preregistrations — the doubling is the point.

### Lottery-ticket trap

If preliminary results look promising, the preregistration must be locked
*before* the full analysis runs against the unseen data. If the lock
happens after the analyst has seen the result, the preregistration is
post-hoc rationalization — and worth nothing.

---

## 3. Sign conventions and units

A surprising amount of error in interaction studies comes from inconsistent
sign conventions across loss space, fitness space, and the published
literature. **Every project locks its sign convention at the top of
`design_notes.md` §1, before any analysis script imports a metric.**

### Pattern (epistasis example)

The first section of
[`developmental-epistasis-scrna/design_notes.md`](https://github.com/mool32/developmental-epistasis-scrna/blob/main/design_notes.md)
is captioned **"§1 Sign convention (READ FIRST. Locked.)"** and contains:

- The empirical formula in the convention used in this project (loss space,
  additive null: `ε_loss = Δ_AB − Δ_A − Δ_B`)
- The same formula in the *other* convention used in the literature
  (fitness space, multiplicative null: `ε_fitness = f_AB − f_A · f_B`)
- A truth table aligning the two: `ε_loss > 0 ↔ ε_fitness < 0 ↔
  synthetic-lethal/redundancy`; `ε_loss < 0 ↔ ε_fitness > 0 ↔
  suppression/buffering`

This convention is then cited by name throughout the codebase: every
analysis script and every verdict report references "the convention locked
in design_notes.md §1". An analyst (or AI agent) who is uncertain about a
sign reads §1 once and is settled.

### What this prevents

In the sister ML project, an inconsistent sign convention propagated
through preregistrations v1 / v2 / v3 before being caught. The biology
project added the locked §1 explicitly to prevent the same error from
propagating across substrates. **The cost of this section is one paragraph;
the saved cost is several rounds of confused interpretation.**

---

## 4. Repository structure

Every research repo follows the same skeleton. Specifics adapt to whether
the work uses scripts, notebooks, or both.

```
<repo>/
├── README.md                       # Standardized template (see §5)
├── LICENSE                         # MIT (code) + CC-BY-4.0 (data/manuscript)
├── .gitignore                      # Standardized exclusions (see below)
│
├── paper/                          # Manuscript and final-form artifacts
│   ├── manuscript.md   or main.tex # Source
│   ├── main.pdf        or *.docx   # Compiled
│   └── figures/                    # Embedded figures
│
├── src/   or scripts at root       # Analysis code
├── notebooks/                      # Colab / Jupyter notebooks (parametric where applicable)
├── analyses/                       # Preregistrations (locked + working) and per-analysis writeups
├── methodology/                    # Method-scoping notes (observational vs experimental, etc.)
├── tests/                          # Unit tests for any non-trivial primitive
├── data/                           # Intermediate CSVs / JSONs (committed; reproduces every paper number)
├── figures/                        # Publication figures (PDF + PNG, 300 DPI)
├── supplementary/                  # Supplementary tables (CSV)
└── config/                         # YAML configs (per-model, per-dataset)
```

### Standard `.gitignore`

Every project gitignores the same baseline:

```
# Python
__pycache__/
*.py[cod]
.Python
.pytest_cache/
.mypy_cache/
.ipynb_checkpoints/

# OS / Editors
.DS_Store
.vscode/
.idea/
*.swp

# Claude Code session metadata
.claude/

# Build artifacts
paper/*.aux
paper/*.log
paper/*.out

# Secrets — never commit
.env
*.env
secrets.json
```

**Always** include `.claude/` (Claude Code session metadata) and `*.env`
(secret env files) — these are the two most common accidental commits and
both are sensitive.

### Numbered execution-order scripts

When a pipeline has more than two steps, scripts are numbered in execution
order: `step01_loop_components.py`, `step02_kegg_loop_extraction.py`, …
Each script is self-contained: reads from `data/` (or upstream public
datasets), writes to `data/` and `figures/`. Side-effects are explicit;
ordering is unambiguous.

For pipelines with branching versions (alternate methodologies tested),
suffixes preserve provenance: `step02_kegg_loop_extraction.py`,
`step02_kegg_loop_extraction_v2.py`, `step02_kegg_loop_extraction_v3.py`.
The `_v3` is canonical (the README says so); the older versions are kept
for reproducibility of intermediate decisions.

### Notebook builders

When the same notebook needs to run with parameter variations (e.g., one
notebook per model checkpoint), use a Python builder:

- `build_phase1_notebook.py` is committed
- `notebooks/01_phase1_validation.ipynb` is regenerated by the builder

This keeps notebook diffs small and parametric, and lets agents read the
intent from the builder rather than the rendered notebook.

---

## 5. README template

Every research repo's README has seven blocks in this order. The full
template is in
[`_landing_work/README_TEMPLATE.md`](https://github.com/mool32/mool32.github.io/blob/main/_landing_work/README_TEMPLATE.md);
the short summary is here.

### A. Top matter — badges + title + author

- Badges in fixed order: **DOI → License → Preprint** (omit individually if
  the artifact does not exist yet)
- Full paper title (not a short label)
- Optional bold subtitle that functions as a TL;DR
- Canonical author block:
  ```
  Theodor Spiro | ORCID 0009-0004-5382-9346 | tspiro@vaika.org
  ```
- Direct links: preprint PDF, main analysis script, Zenodo DOI

### B. Brief Summary

- 4–6 numbered findings, each with a bolded headline phrase + one sentence
  with the key statistic
- Always include an honest-null / limitation finding when one exists
- No editorial language ("excitingly", "remarkably") — let numbers carry weight

### C. Datasets / Inputs

- One-row-per-dataset table; never prose
- Always link the source (PhysioNet, Zenodo, GEO, dbGaP, HuggingFace, …)
- Include access date or version where it matters

### D. Repository structure

- Tree limited to one level + one nested level for `paper/` and `data/`
- Each top-level item gets a one-line comment if its purpose is non-obvious

### E. Reproducing the analysis

- Runnable end-to-end, copy-pasteable
- Realistic runtime estimates next to long steps
- Never use `git clone https://github.com/YOUR_USERNAME/...` placeholders
- If reproduction needs GPU / large data, say so up front

### F. Citation

- BibTeX format, with `note = {...}` for in-prep papers

### G. Contact / License

- Email is `tspiro@vaika.org` (always)
- Dual MIT + CC-BY-4.0 license block (see §12)

---

## 6. Code discipline

### Determinism

- All random seeds are fixed and named (`seed = 42`, or seed-derivation
  functions like `42000 + i` for distributed-noise perturbations)
- Output is reproducible to float32 precision; a 500-cycle drift
  verification is part of the Tier 1 replication suite where applicable

### Numerical hygiene

- Float32 storage, TF32 matmul where applicable. **Float16 noise floor
  destroys early-checkpoint signal in transformer ablations** — discovered
  the hard way; do not switch to fp16 to save memory in spectral analyses.
- SHA-256 bitwise verification of save/restore on every checkpoint
- Per-batch losses persisted as `.npz` sidecars so SE estimation is purely
  post-hoc

### Statistics

- **Bootstrap CIs on every Δ and ε. No point estimates.** Bootstrap is the
  default; if you cite a single number without a CI you have either lost
  resolution or skipped the calibration check.
- Multiple-comparison correction is named (BH-FDR, Bonferroni) and
  performed in the script that produces the result, not in a downstream
  notebook
- Permutation tests for direction-validity claims (random shuffle of the
  label, recompute statistic, p as fraction of permutations exceeding
  observed)

### Witness comparisons

When extending a prior analysis, the new code reproduces the prior result
as a witness check before computing anything new. The pass criterion is
"agreement within 2·SE of the prior point estimate". Failures here mean
the new pipeline diverges from the prior pipeline; fix that before
producing new findings.

Example: `epistasis-transformer-heads/notebooks/01_phase1_validation.ipynb`
reproduces the [Paper 2 (functional-differentiation-dfe)](https://github.com/mool32/functional-differentiation-dfe)
single-ablation Δ on Pythia 410M step 143000 as a witness, with explicit
pass/fail criteria for SHA-256 round-trip, self-pair guard, pair
commutativity, and idempotency.

---

## 7. Manuscript discipline

### Source format

- **Markdown** preferred for manuscripts that don't need LaTeX-specific
  features (most of the portfolio). Compiled to PDF via a builder script
  (e.g., `scripts/15_build_pdf.py` in clonal-crystallization-aging) using
  `fpdf2` with embedded figures.
- **LaTeX** when targeting a specific venue (NeurIPS, journals with strict
  templates). Sections split into per-section markdown files
  (`sections/1_introduction.md`, …) for readable diffs.
- **Word (.docx)** when collaborators or reviewers need to make tracked
  changes; treated as a derived artifact, not the source of truth.

### Sections and figure captions

- Sections in dedicated files for LaTeX projects: `sections/1_introduction.md`,
  `sections/3.5_l8h9.md`, etc. Single-file markdown for shorter manuscripts.
- Figure captions in a single `figure_captions.md` to enforce consistency
  across `paper/` and `README.md` and presentation versions

### References

- `references.bib` in BibTeX form, alongside the manuscript source
- The site-level canonical bib is at
  [`https://mool32.github.io/papers.bib`](https://mool32.github.io/papers.bib)
  — manuscripts cite to this format

### Acknowledgements

**Per the [pi-tissue-aging post-review precedent](https://github.com/mool32/pi-tissue-aging),
Acknowledgements that name LLMs as a "thinking and implementation partner"
are NOT included in published manuscripts.** Computational tools (compilers,
editors, statistical packages, LLMs) are not declared in Acknowledgements,
consistent with standard practice.

Hardware and runtime details (e.g., "Google Colab Pro A100, 82 minutes")
remain in `submission_checklist.md` and in the README's reproduction block,
where they belong.

---

## 8. Identity and contact discipline

One canonical identity, applied uniformly across every artifact:

| Field | Canonical value |
|---|---|
| Name | **Theodor Spiro** (no other spelling, ever) |
| Affiliation | **Vaika Inc., East Aurora, NY, USA** |
| Role | Independent Researcher |
| ORCID | [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346) |
| Public email | tspiro@vaika.org |
| GitHub | [mool32](https://github.com/mool32) |
| Site | [mool32.github.io](https://mool32.github.io/) |

### Where this matters

Every README, every manuscript author block, every Zenodo deposit, every
arXiv submission, every Google Scholar entry uses these exact values.
Inconsistency anywhere creates citation graph fragmentation: a paper
deposited as "Theodor S." may not be linked to "Theodor Spiro" by Scholar.

The historical typo "Serbanescu" appeared in one repo's LaTeX source and
was corrected in
[commit 031d008 of ai-evolution-universal-signatures](https://github.com/mool32/ai-evolution-universal-signatures/commit/031d008)
— that correction also appears in
[`/llms.txt`](https://mool32.github.io/llms.txt) so AI agents that
encounter the stale metadata in cached snapshots have an authoritative
correction.

### When publishing under a prior name (not applicable here, but documented)

If a researcher *does* have a prior legal name, the recommended approach
is: (a) keep historical record under the prior name, (b) add an explicit
name-change note on `/about` and on the relevant repo, (c) use
`sameAs` in JSON-LD to link both identities.

---

## 9. Honest negative results

Negative results — non-replications, failed validations, refuted
hypotheses — are **first-class outputs**, not failures hidden away.

### Pattern

- The repo gets a status badge "Honest Negative Result" in the README header
- The README's Brief Summary lists the negative finding as item #1, with
  the same numerical specificity as a positive finding
- The full report is committed (e.g., `REPORT_FINAL.md` in
  [`eeg-connectivity-contrast`](https://github.com/mool32/eeg-connectivity-contrast))
  so subsequent researchers can audit the reasoning, not just the verdict
- The interpretation section explains *what was learned from the failure*
  (what generalization claim is now refuted, what alternative designs
  remain viable)

### Example

[`eeg-connectivity-contrast`](https://github.com/mool32/eeg-connectivity-contrast)
documents a five-dataset non-replication of the Connectivity Contrast Index
across 18 metrics × 126 subjects. The honest framing — "no metric
replicates across datasets; the strongest within-subject signal reverses
direction across paradigms" — is exactly the framing the agent test in §15
described as "unusual in this space" and "a sign of intellectual maturity".

This is not branding. It is the only correct way to record an outcome that
is real but disagrees with the initial hypothesis.

---

## 10. Process documentation

`HANDOFF.md`, `RESUME_HERE.md`, `SESSION_STATE_*.md`,
`PROJECT_MASTER_INDEX.md` are kept **publicly visible** when they reflect
the genuine process by which the work unfolded.

### When to keep them

- The work is multi-session and the process documentation explains why
  certain branches were tried and abandoned
- Future-you (or a collaborator) needs to reconstruct context to continue
- The documents reveal *how* a result was arrived at, which is itself
  scientific information

### When to remove them

- They contain placeholder author info, fake or test author names, or
  draft framings that contradict the final manuscript
- They are session metadata generated by tooling (e.g., `.claude/` is
  always gitignored)
- They expose secrets or pre-publication results that should not be public
  yet

The default in this portfolio is **keep**. See
[`functional-differentiation-dfe`](https://github.com/mool32/functional-differentiation-dfe)
for the canonical example: HANDOFF.md, RESUME_HERE.md, SESSION_STATE_*.md,
and PROJECT_MASTER_INDEX.md are all public and explicitly described in
the README structure tree as *"kept deliberately as a record of how the
work unfolded session by session"*.

---

## 11. AI / LLM use in the work

### In the work itself

LLMs are used as analysis assistants, code-generation partners, and
manuscript-editing collaborators. This use is treated like any other
computational tool (compilers, statistical packages, editors): not
declared in Acknowledgements (see §7), but present in process
documentation (§10) when relevant for reproducibility.

### In the workflow tooling

The `research-pipeline/` private workspace contains the prompts and
gating structure that govern how LLMs participate in idea generation,
literature search, and analysis planning. The principle is:
**automate the transport, not the judgment.** Wide funnel → hard filter
→ precise execution. Human gates at every decision-defining step.

### Disclosure norms

For ML/CS venues (NeurIPS, ICLR, arXiv): no Acknowledgements naming LLMs.
For biology / biomedical venues (bioRxiv, journal submissions following
ICMJE-style guidance): same — bioRxiv screener feedback on
pi-tissue-aging v4 confirmed that naming computational tools as
Acknowledgements is non-standard.

If a venue's submission guidelines explicitly require AI-use disclosure,
the disclosure goes in the field they specify (cover letter, ethics
statement) — not the manuscript Acknowledgements.

---

## 12. License pattern

Every research repo uses a **dual-license** model:

- **MIT** for code (every `*.py`, `*.ipynb`, `*.sh`, `*.yaml` config)
- **CC-BY-4.0** for data, manuscripts, figures, supplementary materials,
  preregistrations

Single `LICENSE` file at repo root contains both blocks. Canonical template:
[`mool32/heart/LICENSE`](https://github.com/mool32/ecg-spectral-exponents/blob/main/LICENSE)
(MIT only) and the dual form used by
[`pi-tissue-aging/LICENSE`](https://github.com/mool32/pi-tissue-aging/blob/main/LICENSE)
(MIT + CC-BY-4.0). The dual form is preferred for any repo that contains
the manuscript itself.

The README's License section names the split explicitly:

```markdown
- Code (`scripts/`, `*.ipynb`): MIT
- Data (`data/*.csv`): CC-BY 4.0
- Figures (`figures/*`): CC-BY 4.0
- Manuscript (`paper/*`): CC-BY 4.0
```

Upstream data sources retain their own copyrights; this is named in the
data section ("with KEGG / GTEx / TMS / etc. attribution requirements
honored per their respective licences").

---

## 13. Repository metadata

Every public research repo has GitHub metadata set, not just READMEs.
Without metadata, search and discoverability are broken even when the
content is excellent.

### Three required fields

```bash
gh repo edit mool32/<repo> \
  --description "<full paper title or one-sentence TL;DR>" \
  --homepage "<preprint PDF raw URL or DOI URL>" \
  --add-topic <topic> --add-topic <topic> ...
```

- **`description`**: full paper title (preferred) or a TL;DR with the
  headline statistic. Visible on the user's repo list and on every
  search result.
- **`homepage`**: the canonical product of the repo. PDF on GitHub raw,
  Zenodo DOI URL, or a live demo URL. Must not 404.
- **`topics`**: 5–8 from the controlled vocabulary below.

### Controlled topic vocabulary

| Bucket | Topics |
|---|---|
| Domain | `aging-research`, `neuroscience`, `cancer-genomics`, `transcriptomics`, `eeg`, `ecg`, `cognition`, `creativity` |
| Method | `mechanistic-interpretability`, `signal-processing`, `population-genetics`, `dfe`, `epistasis`, `oscillatory-dynamics`, `network-analysis`, `functional-differentiation` |
| Object | `pythia`, `transformer`, `gtex`, `tabula-muris-senis`, `kegg`, `metaculus` |
| Cross | `cross-domain`, `negative-result`, `in-progress`, `independent-research`, `reproducible-research`, `biomarkers` |

Always include `independent-research` and `reproducible-research`. Pick 2–4
domain/method tags. Pick 0–2 object tags. Use `cross-domain` only when
the work substantively bridges substrates (LLM ↔ biology, biology ↔
physics, etc.) — not when it merely mentions an analogy.

---

## 14. Cross-project linking

Companion papers and sister projects are explicitly cross-linked in both
README and manuscript.

### README pattern

The header block of every project links to its companion(s):

```markdown
🧬 **Companion paper:** [Title of companion](https://github.com/mool32/<companion-repo>)
   — one-line description of how it relates
🧪 **Sister project:** [Title](https://github.com/mool32/<sister-repo>)
```

Example: `epistasis-transformer-heads`'s README header links to both
`functional-differentiation-dfe` (predecessor) and the arXiv:2604.10571
preprint (broader framework). `developmental-epistasis-scrna` links to
`epistasis-transformer-heads` as the source of the testable hypothesis.

### Why this matters

A reader (or AI agent) arriving at any node of a multi-paper program can
navigate to every other node without leaving the GitHub ecosystem. This
is also how single citation events propagate: cite one of the papers,
the reader discovers the others via the README links.

---

## 15. AI-friendly publishing

Documented in detail in
[`/llms.txt`](https://mool32.github.io/llms.txt) and in the head of
[every page on the landing site](https://github.com/mool32/mool32.github.io/blob/main/_includes/head.html).
Summary:

- **`llms.txt`** at site root: identity + canonical-name note + research
  themes with TL;DR per project + canonical URL list + framing notes
  to pre-empt predictable hallucinations
- **`robots.txt`** at site root: explicit Allow for GPTBot, ClaudeBot,
  PerplexityBot, OAI-SearchBot, Google-Extended, and other AI crawlers
- **JSON-LD `Person`** in `<head>` of every page: name, jobTitle,
  affiliation, identifier (ORCID), sameAs (GitHub, arXiv author page),
  knowsAbout (10 expertise tags)
- **`sitemap.xml`** auto-generated by `jekyll-sitemap`
- **`papers.bib`** served at site root (not buried in `_bibliography/`,
  which Jekyll excludes from the build)
- **Open Graph** and **Twitter Card** meta via `jekyll-seo-tag`
- **Canonical URLs** on every page via `jekyll-seo-tag`

Cold-fetch agent test of the live site (commit `92f1255`, 2026-05-01)
verified that an AI agent with no prior context correctly extracted name,
affiliation, ORCID, all five themes, six recent papers with concrete
findings, and the cross-domain unique-angle framing. The agent identified
`/llms.txt` as the primary navigation aid and described the site as
"gold standard from an agent's perspective". One real bug (DAT-RU link
badge mismatch) was found and fixed in the same session.

This is the bar. New repos and pages should be designed so that a cold
agent can answer "tell me about this work" correctly without the user
intervening.

---

## 16. Reference exemplar: the epistasis pair

The two epistasis repos jointly demonstrate every principle in this
document. Use them as the running template when starting a new project.

### ML side: [`epistasis-transformer-heads`](https://github.com/mool32/epistasis-transformer-heads)

- **§1 Lifecycle:** in Stage C, multi-phase (Phase 1 validation → Phase 2
  calibration → Phase 2 main → Phase 3 multi-checkpoint → Phase 4 OLMo
  cross-architecture → Phase 5 synthesis). README status badge is
  "In Progress".
- **§2 Preregistration:** `analyses/` contains v1 (Pythia 410M), v2
  (multi-checkpoint), v3 (OLMo-2 1B), each as both `.md` and
  `.LOCKED.md`.
- **§3 Sign convention:** locked in `methodological_findings.md` §1 and
  cited throughout.
- **§4 Repo structure:** `src/` (ablation, eval, stats, io, selection),
  `config/` (yaml per model), `notebooks/` (phase notebooks + builders),
  `analyses/` (preregs), `data/` (with frozen Paper 2 witness CSV
  shipped), `tests/` (unit tests for ablation + stats), `paper/outline.md`.
- **§5 README template:** badges (License + License-Data + Status +
  Companion arXiv), canonical author block, preliminary findings
  framed as "subject to revision under the locked preregistrations".
- **§6 Code discipline:** float32 + TF32, SHA-256 bitwise verification,
  bootstrap CIs, per-batch losses as `.npz` sidecars, fixed eval sample
  reused across models.
- **§14 Cross-linking:** companion to `functional-differentiation-dfe`
  (predecessor) and arXiv:2604.10571 (framework).

### Biology side: [`developmental-epistasis-scrna`](https://github.com/mool32/developmental-epistasis-scrna)

- **§1 Lifecycle:** in Stage B (pilot calibration); README status badge
  is "Scaffolding + Pilot".
- **§2 Preregistration:** explicit "no pre-reg lock until pilot sanity
  checks pass" — the gating discipline made textual.
- **§3 Sign convention:** locked at top of
  [`design_notes.md` §1](https://github.com/mool32/developmental-epistasis-scrna/blob/main/design_notes.md),
  with the truth table for `ε_loss` ↔ `ε_fitness` translation.
- **§4 Repo structure:** `methodology/` (observational vs perturbational
  scoping), `pilot/` (multiple iterations: schiebinger d8,
  paul15 iter3, synth_null iter4, norman iter5),
  `pilot_calibration_verdict.json` as the machine-readable gate.
- **§5 README template:** Status badge "Scaffolding + Pilot", honest
  citation block ("there is no preprint to cite at the pilot stage"),
  cross-link to ML side.
- **§14 Cross-linking:** sister to `epistasis-transformer-heads`,
  positioned as the second half of the broader DFE-universality
  program.

### Pair-level pattern

The two repos illustrate the key claim: **two substrates, one apparatus.**
Same sign convention (with translation), same statistical machinery
(epistasis = non-additivity of pairwise perturbation effects), same
preregistration discipline. The substrates differ; the methodology
generalizes.

---

## 17. Quick checklist for a new project

Before pushing the first commit:

- [ ] Decide the project lifecycle stage (A / B / C); status badge in
      README matches
- [ ] If Stage B or C, draft the preregistration and lock the sign
      convention in `design_notes.md` §1
- [ ] Author block uses the canonical identity (Theodor Spiro, ORCID,
      Vaika Inc., tspiro@vaika.org)
- [ ] README follows the seven-block template
- [ ] LICENSE present (dual MIT + CC-BY-4.0 if the repo contains the
      manuscript)
- [ ] `.gitignore` includes `__pycache__/`, `.DS_Store`, `.claude/`,
      `*.env`, build artifacts
- [ ] No hardcoded API keys (all via `os.environ.get(...)`)
- [ ] No `YOUR_USERNAME` placeholders in code blocks
- [ ] Companion-paper cross-links in README header
- [ ] Repo metadata set: description, homepage, 5–8 topics from the
      controlled vocabulary
- [ ] Add bib entry to [`mool32.github.io/papers.bib`](https://github.com/mool32/mool32.github.io/blob/main/papers.bib)
      and to `_data/publications.yml` (mirrors)
- [ ] Add project entry to
      [`mool32.github.io/_data/projects.yml`](https://github.com/mool32/mool32.github.io/blob/main/_data/projects.yml)
      under the appropriate category
- [ ] Verify the repo is reachable, the homepage URL does not 404, and
      the description renders correctly on the user's repo list

After preregistration locks:

- [ ] Verdicts cite the LOCKED file path and commit SHA
- [ ] Bootstrap CIs accompany every Δ and ε
- [ ] Witness check passes (if extending prior work)
- [ ] Per-batch losses persisted as `.npz` sidecars
- [ ] All scripts deterministic to float32

Before public release:

- [ ] Email everywhere is `tspiro@vaika.org` (not `theospirin@gmail.com`)
- [ ] Affiliation everywhere is "Vaika Inc., East Aurora, NY, USA"
      (not "Independent researcher" alone, which omits the institutional
      anchor)
- [ ] No Acknowledgements section naming Claude / Anthropic / GPT in the
      manuscript
- [ ] Process documentation (HANDOFF, RESUME_HERE, SESSION_STATE_*) is
      either kept deliberately or removed deliberately — not left as a
      default

---

## Document version

This methodology document is versioned with the rest of the site repo;
substantive changes are recorded in the git history of
[`mool32.github.io/methodology.md`](https://github.com/mool32/mool32.github.io/blob/main/methodology.md).
The principles here reflect the conventions in use across the portfolio
as of 2026-05-02; future revisions will add new principles, deprecate
outdated ones, and cite the precedent for each change.
