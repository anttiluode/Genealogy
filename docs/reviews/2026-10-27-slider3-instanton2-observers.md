# October 27, 2026 — From the OpenAI wave paper to Slider3 and Antti's Instanton 2

**Reviewed repositories:** [Slider3](https://github.com/anttiluode/Slider3) and [AnttisInstanton2](https://github.com/anttiluode/AnttisInstanton2). These extend the [existing October 27 wave/wall genealogy](2026-10-27-wave-paper-written-wall-memory.md); the five already-reviewed new repositories are **not duplicated**. Source paper: [OpenAI, *Local smoothing for the Euclidean wave equation* (October 25, 2026)](https://github.com/openai/math/blob/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf).

## Why these are distinct descendants

**Slider3** begins with the problem of distinguishing equal-energy wave configurations. Its original four-condition browser microscope is an approximate interference-and-screened-potential instrument, not a faithful implementation of the paper. Its [paper-grounded extension](https://github.com/anttiluode/Slider3/blob/main/PAPER_IMPLEMENTATION.md) constructs the seven-coordinate finite-mode Friedrichs wave-current tensor and a separate fixed-fiber directional Appendix D solver. They are numerically verified *components*, not the full cofactor/two-circle local-smoothing proof. The source-current current and planar examples do **not** use the same set of physical Fourier modes, so the manuscript is not reproduced end to end.

**AnttisInstanton2** preserves the original nonlinear `phi^4` substrate and its green positive-field center of mass. It has a [free-wave laboratory](https://github.com/anttiluode/AnttisInstanton2/blob/main/lifted_current.py) implementing the positive conserved finite-wave tensor, true Proposition 2.2 time density and a variable-coefficient disk solve on one fixed auxiliary slice. It also has a [nonlinear bridge](https://github.com/anttiluode/AnttisInstanton2/blob/main/nonlinear_bridge.py): each nonlinear snapshot is independently projected into free-wave reference modes using **both** `phi` and `phi_t`. The free-wave theorem is *not* transferred to nonlinear `phi^4`.

The projects share a paper and a diagnostic theme but do not establish a code fork. The Genealogy edge between them is **converges**, not inherits.

## Evidence ledger, with negative results retained

### Slider3: phase sensitivity is not exclusive information

The [64 seeded phase-change trials](https://github.com/anttiluode/Slider3/blob/main/PAPER_IMPLEMENTATION.md) kept all modal magnitudes fixed. Magnitude-only Fourier power detected **0/64**. The paper current and the directional potential detected **64/64**; however, ordinary coherent intensity and a **three-delay single-sensor phase-space observation also detected 64/64**. This is an important mathematical demonstration of phase sensitivity, but it does *not* show an information or cost advantage over a conventional phase-aware observer. The tests compare *noiseless nonzero differences*, not classification accuracy.

The original approximate interference microscope also provides a caution: at matched real displacement mean-square power **0.5**, the auxiliary potential's peak-to-mean is **1.000** for one wave, **1.161** for two locked waves, **1.161** for the same pair with scrambled phase between observations, and **4.683** for six scrambled waves. Instantaneous concentration and temporal coherence are not interchangeable. [Source](https://github.com/anttiluode/Slider3/blob/main/README.md).

### AnttisInstanton2: auxiliary response fails an incremental prediction gate

The [frozen 256-wave benchmark](https://github.com/anttiluode/AnttisInstanton2/blob/main/EXPERIMENTS.md) kept spectral magnitudes and physical energy constant over four independent phase families. It fit the same ridge model to **166** training wave realizations and evaluated **90** held-out realizations. Target: future spatial log-`L4` concentration.

| Features available at present time | Held-out RMSE |
| --- | ---: |
| Present L4 only | 0.058256 |
| Present L4, intensity contrast, energy flux, phase locking | **0.040245** |
| Same ordinary controls **plus paper-derived auxiliary response** | 0.040435 |
| Paper-derived response only | 0.058355 |

The paired gain interval crosses zero (95% bootstrap **[-3.462e-5, +6.702e-6]** in MSE units). The paper's fixed-fiber response has Pearson correlation **0.999714** with ordinary present `L4`. On a secondary future-contrast target, there is a tiny numerical gain, again with an uncertainty interval crossing zero. The correct outcome is **no demonstrated held-out incremental value for this ensemble and slice**, not a theorem that no wave-current representation can ever help.

### AnttisInstanton2: moving centers are an open experiment, not an observed advantage

The later [live three-panel observer](https://github.com/anttiluode/AnttisInstanton2/blob/main/real_paper_instanton.py) and [center dynamics analysis](https://github.com/anttiluode/AnttisInstanton2/blob/main/center_dynamics.py) track the green positive-field CoM and a magenta Appendix-D-inspired map CoM. They may meet, split, and apparently cross, but these are **weighted centroids of evolving distributions**, not two interacting particles. The observer uses an approximate frozen screening and adds separate cap intensities; its nonlinear behavior is **not** protected by the paper's free-wave conservation law.

Tracking now records periodic nearest-arc motion (instead of confusing wraparound with jumps), mass/resultant confidence, projected signed relative motion, lag curves, and ordinary **gradient** and **kinetic** activity center controls. The repository reports **30 passing tests** at this integration. There is not yet a measured held-out multi-seed prediction advantage. A viewer displaying possible 'overshoot' cannot by itself establish a new physical effect.

## A controlled research discriminator

The open question is whether the lifted-focus centroid predicts the nonlinear positive-field center's *future* periodic displacement or domain-wall topology better than ordinary phase-aware intensity, gradient energy, kinetic energy and equally long position histories. The experiment must freeze lag windows, center validity gates and train/test seed splits; compare equal-cost predictors on multiple independent runs; and score future events without peeking. Keep the positive field's original Cartesian center as a historical comparison, but use the **same** periodic convention for relative movement.

If the paper-derived observer is not better, retain it as an instrument and keep the *mathematical* construction without attributing additional empirical sensing powers. If a narrow positive effect holds against stronger controls, document the regime and cost, without claiming that the mathematical local-smoothing theorem applies to a nonlinear particle.

## Provenance and scope

This review reads source docs and recorded experimental receipts; **Genealogy did not independently rerun** the Slider3 or AnttisInstanton2 simulations. The new evidence records distinguish numerical identities from held-out controls and from exploratory screenshots. The preexisting [October 27 Berglund-to-written-wall review](2026-10-27-wave-paper-written-wall-memory.md) remains untouched.

- [Slider3 source and methods](https://github.com/anttiluode/Slider3)
- [AnttisInstanton2 source and methods](https://github.com/anttiluode/AnttisInstanton2)
- [New curated pass](../../data/passes/october-27-lifted-wave-observers-and-instanton.json)
