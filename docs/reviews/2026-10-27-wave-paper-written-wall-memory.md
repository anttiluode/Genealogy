# October 27, 2026 — Berglund resonators, the OpenAI wave paper, and writable-wall memory

**Archive scope:** six curated repository cards, seven explicitly typed lineage/convergence edges, three surviving motifs, six empirical-evidence receipts, one unresolved write–retain–read question. Source inspection on 2026-10-27; **this genealogy pass did not independently rerun the experimental suites**.

[Open the wall](https://anttiluode.github.io/Genealogy/#oct27-wave-memory) · [Curation pass](../../data/passes/october-27-wave-paper-and-written-wall-memory.json) · [OpenAI local-smoothing manuscript (2026-10-25)](https://github.com/openai/math/blob/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf)

## Before the October paper: a real ancestor, not an invented link

**[ResonantNeuron](https://github.com/anttiluode/ResonantNeuron)** was created in **June 2026** and was already in the GitHub census but remained *unreviewed* on the curated wall. Its README explicitly cites Nils Berglund's angled resonator geometry, translates satellite cavities into dendrites and a central interference cavity into a soma, and uses an amplitude-band axon to make logical decisions.

Its designed phasor gates can compose: source-reported XOR, 8/8 full-adder rows, 1000/1000 algebraic and 60/60 dynamic ripple additions. Those are computational demonstrations, not autonomous wall plasticity or a biological neuron model. The later V11–V18 simulations discover limitations when replacing the lumped oscillator picture with a spatial wave equation and hard boundary.

This matters because *Kavitaatio inherited the question, not a demonstrated neural learning rule*. The later experiments work with externally imposed, persistent material parameters and read their effects from echoes.

## The two branches the paper motivated

OpenAI's October 25 manuscript derives a directional free-wave multiplier roughly
`exp[-ρ|ξ|(1−cos(θ−ω))]`: it preserves a selected angular direction with a width narrowing at high spatial frequency. The paper is about Euclidean free-wave local smoothing, **not** physical memory, image objects, learned cavity wall updates or optimal active probing. Parabolic/curvelet-style angular allocations are older known mathematics.

- **[ParabolicOrientationSihti](https://github.com/anttiluode/ParabolicOrientationSihti)**: changes the angular decomposition of Sihti's exact image residues. On 200 BSDS test images parabolic beats the tested fixed-eight control on 145 and its *implemented sp8 angular control* on 171. The paper's specific imaginary-ray window does **not** outperform ordinary stepwise parabolic windows (82 vs 118). Fixed-eight equality at matched PSNR fails the primary gate (112/200, p=.10), and isotropic Sihti wins the main G4 score. Here the directional law is a measured representation choice, not an object-understanding theorem.
- **[Kavitaatio](https://github.com/anttiluode/Kavitaatio)**: separates persistent Robin boundary springs from temporary wave amplitudes. The additive one-wall readout fails on multi-patch memory (0/12); a fourth-order material-interaction expansion decodes all 93 specified 5+-bit held-out records but measures 163/256 calibration configurations per source. Repeated scattering changes the response with the material settings although each fixed-wall wave PDE remains linear.
- **[ResonanceAsControlledMethod](https://github.com/anttiluode/ResonanceAsControlledMethod)**: turns the directional law into a *launched*, energy-matched source rather than a virtual full-field receiver lens. The original single-frequency win is not conclusive: setting fixed angular width `q=k` can exactly match the parabolic source at that frequency. After choosing one shared fixed width `q=0.45` on the original ellipse only, two unseen cavities **favor fixed**. Stadium: **70.8% fixed vs 51.1% parabolic**. Rotated ellipse: **42.2% fixed vs 34.7% parabolic**, 657 paired noisy trials per geometry. The claimed general source advantage is rejected without questioning the free-wave theorem itself.

## A stronger cavity calibration result arrived the same day

**[WallMemoryLaw](https://github.com/anttiluode/WallMemoryLaw)** builds directly on Kavitaatio's non-additivity. The time at which waves can interact with multiple written wall patches is constrained by a shortest scattering tour. That known causal-propagation principle becomes a *specific calibration-set proposal* in this cavity.

The project reports a pre-registered K16 validation of interaction arrival with an overly conservative full-order cutoff, then introduces a per-subset scattering-tour law and a source-ellipse-fitted amplitude-pruning rule. The **separate pre-registered Bunimovich stadium** with **24 written patches** is the most important follow-up:

| Test | Simulated source-reported result |
|---|---:|
| Possible 24-bit wall words | 16,777,216 |
| Unpruned causal-tour calibration | 7,164 settings; 300/300 held-out words decoded |
| Ellipse-trained amplitude-pruned calibration | **848 settings; 300/300** held-out words decoded under specified noise |
| Additive wall model | 0/300 |
| Degree-two-only tour truncation | 56/300 |
| Measured amplitude transfer to stadium | r = 0.92 on 1,380 active sets |

The new stadium was not used to choose the ellipse amplitude coefficients. The experiments include inactive-subset and search-error controls, documented in [PREREG_STADIUM.md](https://github.com/anttiluode/WallMemoryLaw/blob/main/PREREG_STADIUM.md) and the [WallMemoryLaw results](https://github.com/anttiluode/WallMemoryLaw/blob/main/README.md). No claim is made that any arbitrary cavity, pulse spectrum, noise threshold or biological material has this sparse calibration.

**The result is about reading externally written material changes.** The walls are *not* learning the patterns themselves yet.

## A neighboring but distinct reader experiment

**[BigKahuna](https://github.com/anttiluode/BigKahuna)** explicitly descends from [Kahuna](https://github.com/anttiluode/Kahuna)'s four learned records and querying needle. It does **not** implement wave interference, the OpenAI paper, or physical wall springs.

Four identified 2×2 maps are learned first and frozen. In five synthetic switching-world tasks, a reader can buy extra noisy observations. Across 20 paired directional-world seeds (1,200 predictions each), the adaptive needle improves charged loss by **23.4%** against feedback-only tracking, but loses **2.4%** to the calibrated fixed probe and wins only **0 of 20** seed comparisons. The fixed probe is therefore the stronger documented baseline. More disagreement is not automatically more predictive value.

## How they belong on the graph

We added the following **documented inheritance/convergence**, without pretending all projects share code:

- ResonantNeuron → Kavitaatio (*converges*, Berglund/cavity motivation)
- Sihti → ParabolicOrientationSihti (*inherits* image-residue and G4 apparatus)
- Kavitaatio → WallMemoryLaw (*inherits* physical simulation and interaction problem)
- Kavitaatio → ResonanceAsControlledMethod (*inherits* physical wave and Robin-wall memory)
- WallMemoryLaw → ResonanceAsControlledMethod (*converges* around causal/limited calibration)
- Kahuna → BigKahuna (*inherits* four-record learning bank and needle idea)
- ResonanceAsControlledMethod → BigKahuna (*converges*, failure of naive adaptive questions, **not code inheritance**)

The three motifs are: **the wall stores, not the wave**; **paper-derived directionality is not guaranteed memory advantage**; **the best question is measured by its effect on decision error, not by focus or disagreement alone**.

## What we can now legitimately say

**Built:** reproducible wave-memory forward models, externally persistent wall spring bits, signed-point echo measurements, a causal interaction-tour sparsifier with a successful simulated 24-bit transfer test, energy-controlled incident packet comparisons, image direction-budget tests and a four-record query-policy test.

**Not built:** a cavity that writes stable memory by its own local experience-dependent learning rule; a decoder with guaranteed polynomial calibration cost across arbitrary geometries; a demonstration that the new OpenAI Euclidean-wave theorem implies any of those; a biological neuron or physical hardware implementation.

The next open question in the Genealogy questions layer deliberately demands a *write → decay → retain → interrogate* protocol with fixed/indexed memory and matched-cost learning baselines. A beautiful echo, a successful synthetic recall and a physical learning memory are three different things.
