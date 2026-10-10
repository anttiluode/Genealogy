# MoonFormer: a retained medium read through consequences

Reviewed experiment snapshot: [`ef26aef`](https://github.com/anttiluode/MoonFormer/tree/ef26aeff37a70ad5142e2b26b0eda333a83708a2), 2026-10-10.
Remote main at inspection was `457f03e`; its only additional change is the static Pages deployment workflow. The experiment and evidence below are pinned to the tested implementation.

## Documented parent

[CrystalMoon](https://github.com/anttiluode/CrystalMoon) is the direct parent. MoonFormer's README and `reference/crystalmoon/PROVENANCE.md` identify the original attachments supplied before the parent's webcam/wall changes. They are preserved separately rather than silently replaced by today's parent main.

MoonFormer adapts the original scalar Swift–Hohenberg equation, density-dependent mobility, density lens and antipodal inversion. It is a new 2-D memory/probe experiment, not another validation of the original 3-D field. The existing AnttisBrain2 → CrystalMoon edge gives the earlier geometric lineage; no extra direct ancestry from AnttisBrain2, Kuulustelu or other association projects is inferred here.

## Implemented mechanism

A fixture writes an arc, fork, loop or zigzag for 1,500 structural steps. Both its additive drive and growth-gain mask are then absent for 6,000 steps. The numerical field is the retained state; the probe does not receive the old label or trail. Density is a symmetric blur of squared field values. It sets the speed of a separate damped wave while the medium is held fixed during reading.

Four fixed sources, four moon receivers and six time bins produce 96 response features. A small supervised ridge readout is fitted only on training responses and labels. A bounded, clipped inversion map actually participates in receiver sampling. Its discrete transpose scatters the exact interpolation weights; coordinate involution alone is not an adjoint identity.

The reverse Jacobian differentiates the actual wave recurrence and density map. It describes how a small signed material change would alter one selected response. It does not assign semantic meaning or certify the effect of a large erasure. The Jacobian Lens comparison is inspiration about downstream effects, not implementation of Anthropic's language-model J-space.

## Audited receipt and checks

The committed `moonformer-geometric-memory-v1` receipt uses 64 training episodes and 32 held-out variants of four familiar families, with separate seeds and small translation, rotation and scale changes. This is held-out variation, not unseen-family recognition.

| Reader or intervention | Correct / 32 |
| --- | ---: |
| Wave responses, 96 features | 25 |
| Direct density, 64 features | 25 |
| Mean density | 10 |
| Erased material | 8 |
| One fixed material | 8 |
| Material-to-wave coupling disabled | 8 |
| Shuffled training labels | 7 |
| Donor state scored against original history | 2 |

Donor substitution reproduces the donor response vector exactly in 32/32 cases. Coupling-off produces identical features across different media. These controls support dependence on the retained numerical state. They do not establish that wave reading or inversion is uniquely necessary: direct density ties it, with a different feature budget.

For this atlas addition, `npm test` was rerun at the pinned source: **12/12 pass**. This includes central directional finite differences for early and late response bins, the inversion transpose identity, read-only probing, coupling-off, donor substitution and imported-state safeguards. The complete experiment receipt and model were reproduced during implementation; the repository's independent review also reproduced that experiment. This atlas pass audits those artifacts and reruns the short suite, rather than claiming a new independent dataset or full benchmark replication.

Sources: [README](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/README.md), [architecture](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/docs/architecture.md), [receipt](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/results/experiment.json), [tests](https://github.com/anttiluode/MoonFormer/tree/ef26aeff37a70ad5142e2b26b0eda333a83708a2/tests), [implementation review](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/docs/review.md).

## What remains open

The material often grows beyond the original teaching shape. Four longer runs track amplitude and raw force for another 24,000 unforced steps, but decoder accuracy was not measured at all those later delays. Neither permanent shape retention nor faithful image storage is established.

No partial-cue restoration, multiple-memory interference experiment, learned query policy or recurrent associative search exists in v0. An equal-budget receiver comparison is the next clean discriminator for the moon: ordinary versus inversion-mapped receivers, with the same sources, feature count, training split, classifier selection and noise. This can separate a useful receiver geometry from an interesting display without changing the already demonstrated state-dependent response.

The entry records an implemented synthetic field-memory reader. It makes no claim that this is a transformer, the equation of the brain, or an experience of thinking.
