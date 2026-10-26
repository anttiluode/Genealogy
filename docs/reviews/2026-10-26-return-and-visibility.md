# October 25–26, 2026 — what the return contains

This review keeps three kinds of outcome separate: a mechanism implemented in software, a controlled synthetic measurement, and a claim about an actual physical scene. It covers the latest [OddOne](https://github.com/anttiluode/OddOne) and [SimplyPut](https://github.com/anttiluode/SimplyPut) branch, then fills gaps among the frequently visited practical repositories.

The machine-readable genealogy is in [return and hidden vision](../../data/passes/october-25-26-return-and-hidden-vision.json) and [popular artifact archaeology](../../data/passes/october-26-popular-artifact-archaeology.json). Evidence records appear in the atlas's Evidence view, not only in this narrative.

## OddOne: reading a return is not the same as inventing the missing scene

The webcam app trains on one half of a frame and predicts the other half. It includes a running linear estimator and an optional CNN. Its new `diagnose.py` reports frozen test performance, time-shuffled and average-brightness controls, multi-resolution change R², channel correlations, exposure and midline leakage diagnostics, and an out-of-training-input indicator.

[The committed six-scenario synthetic receipt](https://github.com/anttiluode/OddOne/blob/main/diagnose_synthetic.json):

| Synthetic scene | R² at full resolution | R² at 1/8 resolution | What the score actually means |
| --- | ---: | ---: | --- |
| Independent halves | −0.022 | −0.074 | No recoverable signal |
| Smooth glow | 0.052 | 0.550 | A few coarse spatial degrees of freedom |
| Edge shadow | 0.131 | 0.728 | Spatial light modulation carries more structure |
| Crossing midline | 0.963 | 0.990 | Continuation, not necessarily non-line-of-sight optical inference |
| Global exposure | 0.985 | 0.972 | A brightness-only control obtains 0.985 at full resolution |
| New light colour | −10.516 | −6.907 | The trained linear mapping extrapolates very poorly |

The effect of an occluding edge is therefore a real *synthetic* signal-identifiability contrast, not a measured success rate for hidden people in the user's room. The novelty threshold in the detector was revised after the example was observed. Frame-level predict-before-train scoring is welcome but adjacent frames are correlated; truly new positions, novel objects and camera-specific auto-exposure effects still demand separated interventions.

**Next discriminator:** freeze the trained lens, keep actors and objects wholly in the hidden half, introduce never-trained positions/colours, lock or measure camera exposure, switch an occluder on/off without changing the visible action, and compare the linear mapping with brightness, temporally shuffled, continuity-only and CNN baselines. Prefer temporally separated evaluation episodes over only adjacent new frames.

The conceptual relatives are [Varjoluotain](https://github.com/anttiluode/Varjoluotain) and [KulmanTakaa](https://github.com/anttiluode/KulmanTakaa). [DoDis](https://github.com/anttiluode/DoDis) is a useful *contrast*: donor-based missing-image completion can look plausible without containing the actual hidden scene. No code ancestry is asserted between the two methods.

## The bell: which part of experience survives?

- [SimplyPut](https://github.com/anttiluode/SimplyPut) makes contact outcomes useful through ordinary context-indexed action memory. Shortcut and plain action table both reach 100% first-attempt success in 32 synthetic worlds, so the neural novelty claim is intentionally absent.
- [SimplyPutClaude](https://github.com/anttiluode/SimplyPutClaude) tests route-local plasticity on four sequentially learned reaches. The source reports mean final corrections **0.68 ± 0.04** for experience-chosen routes versus **2.94 ± 0.13** for the shared tanh net (10 seeds). Reducing route capacity spoils retention; the teacher still supplies a 2-D correction near contact.
- [SimplyPutSol](https://github.com/anttiluode/SimplyPutSol) instead learns from its own paired motor probes and scalar feedback. Four of five locked gates pass, but final adaptive-cable error **0.396** fails to improve on frozen cables **0.395** and phase-disabled cables **0.390**. The extra machinery has not earned a causal advantage.
- [HailMery](https://github.com/anttiluode/HailMery) tests a different layer: in a designed delayed multisensory world, self is what one's actions predict, not simply what cross-modal correlations share. Vision/sound/touch self readouts reach **R² 0.995 / 0.998 / 0.999** on one constructed run. It does not prove awareness or an actual cortical observer-of-observers.

## Earlier projects worth keeping visible

[PhaseSpaceVisualizerVST](https://github.com/anttiluode/PhaseSpaceVisualizerVST) was already curated in the [Practical Islands pass](../../data/passes/practical-islands.json). Four other frequently visited repositories now receive explicit reviewed cards:

- [LLmit2](https://github.com/anttiluode/LLmit2) and [LLmIT3](https://github.com/anttiluode/LLmIT3): a local LLM-populated social playground, later with bot profiles; both document rough edges. Version succession is supported; emergent autonomous society is not.
- [StableAIflow](https://github.com/anttiluode/StableAIflow): a creative diffusion/phase-registration feedback filter; quantitative superiority to other temporal stabilizers has not been independently tested.
- [ResonantCortex](https://github.com/anttiluode/ResonantCortex): phase/amplitude network with source-reported modular arithmetic and Lorenz metrics, deserving same-budget, same-split baseline reproduction before any general architectural ranking.

**Surviving pattern:** The work is strongest when a probe reveals a signal channel and the trivial look-alikes are explicitly ruled out. Working tools are also wins in their own right; they do not need a universal physics explanation.
