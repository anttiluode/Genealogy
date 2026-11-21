# The Sihti line — a closer look, 21 November 2026

[Back to the special top-of-wall chapter](../index.html#nov21-sihti-lineage) · [Machine-readable evidence and lineage](../data/passes/november-21-sihti-head-and-retrospective-residue.json)

**The guiding idea:** the difference that disappears under a coarse reading is not destroyed. Preserve it exactly. Later, if the coarse state predicts incompatible futures, ask which saved distinction might resolve them. A feature is not vindicated until it improves prediction on independent future observations.

## The ancestors

[SighImageSuper](https://github.com/anttiluode/SighImageSuper) precedes [Sihti](https://github.com/anttiluode/Sihti). Sihti takes an image through a sequence of purifiers and keeps every signed difference so that the final core plus residue bands exactly reconstructs the original. [SihtiImageModel](https://github.com/anttiluode/SihtiImageModel) studied no-backprop image modeling with fixed residue memory. [SihtiImageModel2](https://github.com/anttiluode/SihtiImageModel2) explored a separately backprop-trained layout generator plus residue reconstruction; the Genealogy wall retains these as different experiments, not one universal mechanism.

## November 21: two streams converge

**The image/prediction stream:** Sihti → **[SihtiAI](https://github.com/anttiluode/SihtiAI)** (21 user-reported commits) → **[PredictiveSihtiV2](https://github.com/anttiluode/PredictiveSihtiV2)** (7) → **[LazyRetrospectiveCreditAssignment](https://github.com/anttiluode/LazyRetrospectiveCreditAssignment)** (6).

SihtiAI asks if the unsigned persistence of a disappearing texture can write a better relation between pixels. The proposed beta=1 grouping failed; a post-hoc beta=8 setting isolated one synthetic striped object (mean ARI around 0.970 across ten noise seeds), not broad image understanding. PredictiveSihtiV2 uses signed Sihti layers with coordinate-free local patch transition memories. Where familiar shape-only addresses recall conflicting futures, it can ask a second question about motion rather than asking everywhere. Its frozen synthetic 1→5 transfer in automatic mode measured about 39.6% error reduction against hold-last. LazyRetrospectiveCreditAssignment saves the earlier signals until a later ambiguous outcome provides a reason to inspect them; in synthetic 100-tick episodes it recovered exact 80-tick cue channel/lag in 20/20 sparse, 20/20 noisy and 20/20 sign-reversed seeded trials.

**The head/closure stream:** **[SaturdayAfterRHproof](https://github.com/anttiluode/SaturdayAfterRHproof)** (2) → **[HEAD](https://github.com/anttiluode/HEAD)** (5) ↗ LazyRetrospectiveCreditAssignment. The Saturday experiment exhibits two identical coarse states that differ under a future copy-left action; the smallest distinguishing sign bit makes the given task predictively closed. HEAD shows when a second reading can expose a contrast with limited access. It uses supervised gradient optimization in its controlled training runs; it is a conceptual contributor, not proof of an entirely backprop-free lineage.

These are documentary inheritance and conceptual convergence links, *not* a claim that each repository is the same codebase.

## The cold wall: what did not work

| Test | Observation | Interpretation limit |
| --- | --- | --- |
| Sihti decomposition | Exact C + signed residues reconstruction to floating-point precision | Reconstruction is not prediction |
| PredictiveSihtiV2 frozen pulses | ~39.6% synthetic 1→5 error reduction | Not robust real video performance |
| Retrospective synthetic cue | 20/20 correct exact-lag finds in three seeded cue conditions | Repeated, constructed task with a simpler FastHead |
| Retrospective null condition | **2/20 false promotions**; a lower B coincided with worse held-out prediction | Internal certainty is not accuracy |
| Real webcam, user-exported audit | **480 scored frames; −31.3% vs. hold-last; 45 sampled auto alarms; WAIT** | No useful real delayed precursor established |

The real webcam trial archived 481 signed frames; the peak core+residue reconstruction discrepancy was about 4.47×10⁻⁸. The live instrument automatically triggered on persistent disagreement and then on every 10-frame debounce, so 45 alarm samples do *not* mean 45 independent physical events. The retrospective validation rejected the weak historical associations. The full camera footage and reconstructable raw frames are not included in this public Genealogy entry; only summary measurements supplied by the user.

## Why the latest tip belongs at the top

The strong continuity is not a claim of new AI capability. It is a concrete engineering question: **Can a system keep detail it cannot currently use, recover it when its forecast fails, and refuse to believe false historical explanations?** The next credible step is to test whether a probationary memory latch reduces held-out surprise on real streams, against the extremely strong hold-last baseline.
