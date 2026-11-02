# November 1, 2026: Nopee and NopeeClaude — two controls on faster video

**Source review, not an independent rerun.** These are two independent experiments asking whether neuron-inspired spatial filtering and leaky temporal memory confer a measurable advantage. [Curated pass](../../data/passes/november-1-nopee-dual-video-controls.json) records their different mechanisms, observed results, limitations and conceptual links.

## Nopee: a real tiny predictor, but no overall advantage from the full adapter

[Nopee](https://github.com/anttiluode/Nopee) is an offline-capable, trained 32×32 frame forecaster. A shared convolutional transport/refinement base gets four frames and predicts future frames. An optional parallel branch combines difference-of-Gaussians (DoG) spatial filtering with a signed, damped recurrent E/I state. Fixed synthetic, learned and shuffled constants receive matched training streams; the UI offers reset, spatial-bypass and constant-shuffle interventions. There are no measured living-neuron constants, and the number of refinement-network calls is **not** a diffusion step budget.

Its [November 1 demonstration ledger](https://github.com/anttiluode/Nopee/blob/main/results/DEMO.md) reports a two-call, 12-world test with whole-frame MSE **0.03390** for adapter off, **0.03765** fixed and **0.03887** learned. The full branch **loses** to its matched base. Bypassing the spatial filter lowers the learned variant to **0.02522**; clearing memory also helps. The experiment demonstrates a real causal feature pathway, not a beneficial full adapter or biological specificity. It has one training seed, tiny moving-shape worlds and development choices made after visual inspection.

## NopeeClaude: first test the real sampling budget

[NopeeClaude](https://github.com/anttiluode/NopeeClaude) probes a *different question*: with Wan2.2-TI2V-5B on a 12 GB GPU, can a cheap sample remain close enough to a 40-step reference for a tiny DoG/E/I-inspired adapter to repair it? The [README and preregistration](https://github.com/anttiluode/NopeeClaude/blob/main/README.md) define paired reference/cheap trajectories and planned controls, including unconstrained kernels and unsharp masking.

On **12 validation prompts**, the source reports six-step output in **13.9 s** and 12-step output in **27.7 s**; qualitative examples often lose or change the subject. A **separate three-prompt cache sweep** reports 40-step FirstBlockCache 0.3 in **28.3 s** and cache 0.5 in **21.5 s**, with closer latent agreement than the reduced-step trials. These measurements use different prompt sets, so they do **not** establish a direct matched-prompt quality-speed frontier. The 40-step reference was also generated at an off-design 320×576 resolution.

**The planned adapter training was paused before real training** after these baseline measurements. There is consequently *no* result that a neural-inspired adapter repairs reduced-step sampling, outperforms caching, or achieves TBC-like quality. No measured neuronal constants were involved.

## Where the two branches meet

Nopee explicitly credits Antti's **Sihti / Janus / SignalIsASignal** discussions alongside the publicly described Oasis hypercolumn adapter as motivation. Both projects test a centre–surround + temporal-memory idea, but one measures an independently trained tiny next-frame predictor, while the other first measures generation-budget tradeoffs in an existing Wan model. Their graph edge is therefore **conceptual convergence**, never a software fork or experimental replication.

**Surviving lesson:** keeping a recurrent branch real and causally connected is necessary for studying it, but usefulness must still survive ordinary matched baselines, component ablations, timing and proper test sets. The reported negatives belong on the wall.
