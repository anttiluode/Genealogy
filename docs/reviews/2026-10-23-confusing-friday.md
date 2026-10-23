# Confusing Friday — October 23, 2026

**Genealogy field note.** The date connects six repositories without turning them into a single successful system. The first three — [BindingClaude](https://github.com/anttiluode/BindingClaude), [BindingSol](https://github.com/anttiluode/BindingSol) and [WhiteBox](https://github.com/anttiluode/WhiteBox) — were already curated in the [early October 23 source review](2026-10-23-binding-whitebox.md). This supplement adds [SihtiGraphModel](https://github.com/anttiluode/SihtiGraphModel), [DoDis](https://github.com/anttiluode/DoDis) and [GhostYou](https://github.com/anttiluode/GhostYou).

## The story of Friday

**First: can we find the binding?** BindingClaude's toy parity/dendritic constraints can be recovered and used for masked settling, yet revision after a rule flips fails in 9/10 seeds. BindingSol learns an actually usable one-bit sender/receiver message in just 2/5 precommitted seeds and loses to a matched-size direct MLP on mean held-out performance. WhiteBox extracts a sparse **behavioral** parity rule from trained synthetic MLPs, not their actual internal causal circuits. The alternative methods use different search, compute and teaching budgets.

**Second: is the binding visible inside an image classifier?** SihtiGraphModel replaces toy signs with **64 multiscale spatial input switches** on a fixed 32×32 CIFAR bird and asks the frozen CNN for its logit margin under many masks. The original v1 source-reported gate failed. v2's 50-piece direct graph on the first bird reached **R² 0.534** at 50% retained under mean fill, yet collapsed to **−3.035** at 90%. The v3 saved results are more informative:

| Held-out masked-input readout | Bird #65, global mixture | Bird #70, separately refit global mixture |
| --- | ---: | ---: |
| 50% pieces kept, R² | **0.295** (v3 p=.50 gate fails) | **0.508** |
| 90% pieces kept, R² | **0.666** | **0.851** |
| 95% pieces kept, R² | **0.635** | **0.882** |

A p=.90-only sparse graph reaches **0.839/0.886** on bird #65 and **0.864/0.918** on bird #70 at 90%/95% retention respectively, yet it falls to **−3.372** on bird #65 with only 50% retained. The learned same-tile B0×B3 links have **zero overlapping tiles** between the two birds. This shows a meaningful *input-mask explanation* for individual images at a chosen retention regime; it does **not** show a transferable relational graph, a causal map of CNN neurons, nor image generation. Source: [committed v3 results](https://github.com/anttiluode/SihtiGraphModel/blob/main/runs/v3_birds_mixture_seed41/results.json). The README's older “not run” language is overtaken by the committed result files; the preregistration gates must not be silently replaced.

**Third: can the relationship machine actually fill something in?** DoDis has three distinct roles: **memory proposes content**, a learned graph scores whether pieces fit, and a CNN-purpose surrogate can bias a decision. The 12 held-out bird v1 run hides half the multiscale residues and reports:

| Reconstruction arm | Mean pixel MSE (lower better) | Frozen CNN bird margin (higher better) |
| --- | ---: | ---: |
| Memory + smoothness | 0.01494 | −0.590 |
| Memory + learned binding | **0.01417** | −0.003 |
| Memory + shuffled-binding | 0.01438 | −0.339 |
| Memory + binding + CNN purpose | 0.01482 | **+1.578** |

The learned-vs-shuffled advantage is **only about 0.00021 MSE**. The shuffled graph captures roughly **73%** of the reduction relative to memory+smoothness. The CNN-purpose term increases the recognizer's bird preference but *worsens actual image reconstruction* relative to binding alone. Better bird classification confidence is not evidence of a better bird picture. Evidence: [v1 saved receipt](https://github.com/anttiluode/DoDis/blob/main/runs/v1/results.json), [preregistration](https://github.com/anttiluode/DoDis/blob/main/PREREG.md).

**Fourth: the useful new idea is about addresses.** DoDis v2 changes retrieval from globally similar source images to **per-missing-piece local donors**, scored using only visible nearby, same-scale and cross-scale information. This implements the older [SihtiImageModel](https://github.com/anttiluode/SihtiImageModel) thought: a coarse/partial observation may help locate a fine residue even if it cannot itself recreate that residue. The protocol includes a no-repair mask baseline, whole-image donors, same-band-only retrieval, cross-scale local retrieval, learned-binding, shuffled-binding and CNN-purpose arms. The upstream [v2 runs folder](https://github.com/anttiluode/DoDis/tree/main/runs/v2_local_100_birds) now contains **100 individual bird receipts** and a large results.json, though the README still says outcomes are pending. The full aggregate (>5 MB) was not retrievable/parsed by this atlas curation, so **neither PASS nor FAIL is recorded for v2 CIFAR** here. Counting files is not a result.

**And a ghost.** [GhostYou](https://github.com/anttiluode/GhostYou) is a finished playful Halloween webcam/toy: movement fades a person into a learned background and plays a sine-wave theremin, with vertical position setting pitch and movement setting loudness. It is browser-local according to its README, with a [GitHub Pages demo](https://anttiluode.github.io/GhostYou/). No scientific inference or live device validation is claimed for it. It deserves a practical card without a fabricated link to the CNN research.

## Why the day is called *Confusing Friday*

The confusion was productive because it kept revealing **different things that can be mistaken for one another**:

- The hidden variable's statistical dependence, a readable neural feature, and a causal circuit are not the same thing.
- Explaining a classifier's reaction to damage is not reconstructing the missing picture.
- Lowering a solver's chosen energy is not minimizing held-out pixel error.
- Raising a bird classifier's margin is not recreating the correct bird.
- A visible context can be an **address** for missing information without containing the missing information itself.
- A working interactive ghost can be useful without being a novel scientific finding.

The most promising next image-model experiment is therefore bounded: **fix the same observed mask, donor budgets and held-out images; compare cross-scale local retrieval with same-band-only, global and no-repair controls; then test whether learned binding adds a statistically credible improvement over a shuffled graph**. Do not replace this with a beautiful image montage or a classifier-margin-only metric. First numerically audit the already uploaded v2 100-bird receipts and registered gates.

This note curates source-reported measurements; it does not rerun CNN training, 100-bird image reconstruction, browser camera access or SGD.
