# November 9–10, 2026 — Active eyes, asymmetric memory, and Fable's crystal worlds

**[Live Genealogy chapter](https://anttiluode.github.io/Genealogy/#nov9-10-new-branches)** · [Curated machine-readable pass](../../data/passes/november-9-10-active-eyes-private-memory-fable-worlds.json) · [Fable's ECG follow-up](2026-11-10-ecg-refractory-phase-and-lenses.md).

## Inventory versus interpretation

The repository inventory already lists **610 distinct repos**, with the five covered here previously marked `unread`. This pass changes **five existing inventory records to reviewed** and adds **five curated nodes**, **six typed links** and **three motifs**. It does **not** claim 610 new discoveries or duplicate the previously curated November 8 railways. User-provided activity totals are historical commit snapshots; they are not a comprehensive GitHub activity census.

## 1. OneTinyTransformer — a learned question is not necessarily the best question

[Source README](https://github.com/anttiluode/OneTinyTransformer/blob/main/README.md) · [Full measurement receipt](https://github.com/anttiluode/OneTinyTransformer/blob/main/experiments/LEARNED_POLICY.md).

A genuinely trained but narrow **24-residual-feature, four-block, two-head** browser LM is preserved as an inspectable offline artifact. An *additional* promptless recurrence is a separately designed state transition, not evidence the original LM maintains a free-running private stream. A new coordinate-query transformer is trained with counterfactual labeled simulation feedback and a shared Gaussian decoder. It uses the original language model's blocks as an optional initialization, not as a natural-language question-answering engine.

**Four looks, one 960-trial held-out synthetic evaluation:** fixed order **60.7%**, random **62.5%**, fine-tuned LM-initialized **73.0%**, frozen LM-initialized **71.9%**, trainable random initialization **72.6%**, and analytic posterior disagreement **87.8%**. A learned selector is viable, but pretrained LM weights are not established to help; the cheap analytic policy wins strongly. One seed, privileged training feedback, a known decoder and a small synthetic candidate family limit claims.

## 2. SihtiSilma — a useful instrument for looking where memory disagrees

[Source README](https://github.com/anttiluode/SihtiSilma/blob/main/README.md) · [Preregistered 200-photo result](https://github.com/anttiluode/SihtiSilma/blob/main/RESULTS_V2.md).

**Direct trained-model ancestry:** [SihtiImageModel](https://github.com/anttiluode/SihtiImageModel) exports its original trained **512-expert P3 patch codebook** and multiscale sieve into SihtiSilma. The observer can reveal disjoint 8×8 tiles, not inspect the hidden original. The new local expert-disagreement score is a selection heuristic, *not* a calibrated posterior.

After **20 looks on all 200 BSDS500 test photos**, P3 + edge selection scores **23.49 dB** PSNR, P3 + disagreement **24.06 dB** (**+0.57 dB, 89% wins, 95% interval 0.49–0.66**), and scale-free error-feedback **24.18 dB** (another **+0.12 dB**). The old four-photo pilot measured 27.91 dB for both disagreement and feedback, but v1 feedback was actually pinned by its clamp. The revised score passes the small predefined +0.1 dB gate. Per-band recalibration adds only **+0.03 dB**, failing its +0.2 dB gate. Expert predictions are **not re-run after measurements**; observed pixels are pasted, and the oracle uses forbidden ground truth.

## 3. Muru — an internal Eye/Body separation, and what the pillars really mean

[Source README](https://github.com/anttiluode/Muru/blob/main/README.md) · [Five-seed matched-observation pillar audit](https://github.com/anttiluode/Muru/blob/main/RESULTS_RANK.md).

Muru is an **untrained** offline two-organ attention toy inspired conceptually by the active-eye experiments and by OneTinyTransformer. The Eye holds four recent looks and fast value-weight changes; the Body receives only compressed Eye activations, retains multi-timescale EMA memory, and sometimes feeds back a look bias and updates. This is **not** a fork of the Sihti P3 image reconstructor, nor a pretrained thinking assistant.

Five seeds and **identical observation streams** across mutual, clamp-after-24 and always-clamped arms: at look 96, Eye **delta-W effective rank 1.041** and row uniformity **0.993**; Body **delta-W rank 5.454** and row uniformity **0.284**; actual Body slow-memory rank **1.058**, nearly the same under every clamp. Crucial distinction: the two *weight maps* are weight **changes**, and the third map is memory, not weights. The slow-memory pillars arise without reciprocal weight coupling because 16 EMA rows all receive the same compressed message. Muru is roughly tied with the Bayesian variance baseline; the audit does not establish emergent intelligence or learning.

## 4. CrystalMoonV3 — Fable 5.2 changes colour/light, not the big crystal bodies

[Source README](https://github.com/anttiluode/CrystalMoonV3/blob/main/README.md) · [V2 parent](https://github.com/anttiluode/CrystalMoonV2).

This is a direct source descendant of V2: 16,384 synthetic ray photons **per RGB band**, with stronger bending for blue than red, three-channel deposited light, chromatic fine-lattice growth, transparent glass that can reveal internal beads, plus bloom/tone passes. Fable reports the original **12 core tests** and **four new tests** passing; blue/red/white illumination leaves internal grain over about **74%/29%/62%** of a controlled test body. Software headless GPU-vs-CPU update parity is approximately 10^-7.

**The body field remains the old swollen-blob law.** The visible colour difference across lit regions is localized (mean |B−R| **0.09** at level 0), and the claim that *new grain changes later spectral bending enough to matter* has not been tested as a closed causal loop. The dispersion is exaggerated, ray tracing is geometric rather than wave interference, and GPU speed/flight responsiveness on a native RTX 3060 remain unverified. More rendering fidelity is not necessarily new morphogenesis.

## 5. NotKansas2 — Fable 5.2 gives the hyperbolic moon eight connected insides

[Source README](https://github.com/anttiluode/NotKansas2/blob/main/README.md) · [NotKansas parent](https://github.com/anttiluode/NotKansas).

**Direct implementation descendant** of NotKansas, not of CrystalMoonV3. The moon now selects one of **eight regular Coxeter hyperbolic honeycombs** across levels, including four with finite corners and four with ideal vertices. The inner world's crystal is sampled on each cell *face*, and a pearl at a cell centre takes the camera into the next outside level. The source reports **6/6 geometry tests**, plus a level-2-to-3 browser descent checked in software rendering. For N4, the chamber fold requires more than 40 passes on a few ideal-corner samples (up to **6 of 4,000** in the given test).

**Still an open problem:** the crystal itself grows on the next world's *flat* 64³ lattice; mirrors map it to hyperbolic space. The frame and pearls are rendered geometry, not structures produced by the crystal-growth law. Native GPU timing is unmeasured; pearl choices have identical destinations, and there is no returning up the chain. This expands the navigable topology, but not the field physics.

## Correct ancestry and the shared unfinished question

```text
GeometricNeuronOriginReview --(conceptual question)--> OneTinyTransformer
SihtiImageModel --------(model/code inheritance)------> SihtiSilma
OneTinyTransformer ------(conceptual convergence)-----> SihtiSilma
OneTinyTransformer -----(conceptual extraction)-------> Muru
SihtiSilma -------------(conceptual extraction)-------> Muru

CrystalMoon --> CrystalMoonV2 --> CrystalMoonV3
                          `-----> NotKansas --> NotKansas2
```

The **new pass encodes only six defensible graph edges**; the ECG connection is historical context, not a claim of shared implementation. The railway family (TurntableNeuron, TurntableAISol, KasvavatKiskotSol, KasvavatKiskotClaude, BrainRailRoad) remains in the **November 8** passes, with its negative 50%-accuracy rescue intact. The more recent Fable ECG interpretation already has a separate provisional November 10 chapter.

The deepest shared open test is whether a *measured internal change* — uncertainty, fast weights, crystal grain, or curved geometry — causes a corresponding **held-out improvement in future action or prediction**, rather than just producing a more interesting image of the mechanism. Sources above report their own checks; this Genealogy update has **not independently rerun the parent projects' scientific benchmarks**.
