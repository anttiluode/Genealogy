# October 29, 2026 — RoundAndRound, temporal memory, and physical state transfer

Seven sources enter [Genealogy](https://github.com/anttiluode/Genealogy). They do not establish one shared biological mechanism.

## Physical and feedback experiments

**[Complexity](https://github.com/anttiluode/Complexity).** Its numerical model reports 11/11 seeded cold droplets recovering their shape after a kick while retaining altered internal breathing. With reference-oscillator phase variables, held-out local probe prediction error falls from 0.402 to 0.218. Neither generic spontaneous formation nor long-lived organisms follow.

**[ChainNeuronsWithPhaseSpike](https://github.com/anttiluode/ChainNeuronsWithPhaseSpike).** Its phase-coded burst is ordinary two-tone beating, not a biological spike; near a locking edge a different pair produces threshold-like 2π phase slips. Near-contact sender pattern accuracy 0.85 versus 0.62 leakage control does not establish multi-hop regeneration.

**[ChainNeuronsWithPhaseSpikeSol](https://github.com/anttiluode/ChainNeuronsWithPhaseSpikeSol).** Independent beat and passive propagation audit, followed by a stationary active receiver with history-dependent phase response. Moving bonded-chain spike relay is not demonstrated.

**[ThursdaySol](https://github.com/anttiluode/ThursdaySol).** Three homeostat/checkerboard loops with explicitly engineered A→B→C connections. A deterministic matched-visible-state graft at B changes C's later-probe interaction by 0.666833 and B→C disconnection makes it zero. Crucial negative: at input noise SD 0.003, 0/8 default paired preparations exceed 0.05 interaction.

## Computation and reactivation

**[MoebiusLoopMemory](https://github.com/anttiluode/MoebiusLoopMemory).** Fixed rotating feature-space state plus a contextual multiplicative gate makes historical XOR(lags 2,3) 83.3% linearly readable in five-seed synthetic tests; state erasure drops to chance. Cyclic and orthogonal conditions tie or beat the signed topology on tested tasks. No special Möbius benefit.

**[LoopAImemory](https://github.com/anttiluode/LoopAImemory).** Trains linear heads on the fixed recurrent state, including two-event comparison, lagged recall and second-order synthetic prediction. Dual path achieves 99.9% on the event-equality toy, while quadratic mean gets 100%. Prediction 91.1% ties the explicit two-frame oracle. Real webcam generalization is not measured.

**[RoundAndRound](https://github.com/anttiluode/RoundAndRound).** A new NumPy implementation: continuous-time autonomous plane rotations, Sihti-style ringdown differences plus final core, ridge-learned cue-to-residue slow memory, complete fast-state erasure and cue-driven reawakening. Five unit tests passed locally.

### First local benchmark receipt

12 synthetic histories with 8 noisy training repetitions each and a 24-dimensional cue. Max telescoping reconstruction error 3.55e-15. Learned cue reactivation after hard fast reset has RMSE **0.22174**; wrong cue **3.67203**; empty fast state **2.95856**. The restored loop evolves eight time units with RMSE **0.14218** against the target future.

**Essential control:** an identically regularized direct cue-to-state ridge readout achieves RMSE **0.22174**, mathematically tied because linear prediction commutes with summing Sihti residues. This is a working write–erase–reawaken mechanism, **not** evidence that residual encoding compresses better or avoids catastrophic forgetting.

## Typing the connections

- MoebiusLoopMemory → LoopAImemory: actual recurrence inheritance.
- MoebiusLoopMemory and LoopAImemory → RoundAndRound: conceptual convergence on trained bounded-history interfaces, but RoundAndRound uses its own continuous-time motion and a separately trained slow memory.
- ChainNeuronsWithPhaseSpike → ChainNeuronsWithPhaseSpikeSol: independent parallel audit, not an inferred code fork.

## Next falsification

Train sequential sets of distinct histories under an equal total scalar budget; erase fast state between tasks; compare band-selective consolidation with direct memory, fixed-buffer history and trained recurrent baselines on old-task retention, new-task acquisition, noisy cues and out-of-distribution delays. Separate self-generated probes from new external evidence before allowing them to write. Do not claim consciousness, hippocampal circuitry or a general continual-learning cure.

Source attribution: the six earlier projects' numerical findings are sourced from their READMEs and ledgers rather than independently rerun here. RoundAndRound's five tests and deterministic first benchmark were run locally before committing its code.


## RoundAndRound Gate 2 — selective consolidation was not enough (October 29, later update)

The follow-up [consolidation protocol](https://github.com/anttiluode/RoundAndRound/blob/main/docs/CONSOLIDATION_GATE.md), [benchmark](https://github.com/anttiluode/RoundAndRound/blob/main/consolidation_benchmark.py), and [eight-seed results ledger](https://github.com/anttiluode/RoundAndRound/blob/main/results/CONSOLIDATION_RESULTS.md) now test three successive task sets A→B→C with fixed **192-scalar** online linear associative memories and complete fast-state erasure between episodes.

Sihti-derived fast-residue/slow-core selective consolidation improved post-C old A late-state NRMSE to **0.9885**, compared with **1.2700** for a uniformly fast direct-state writer. But the **direct per-feature learning-rate control also gets 0.9885**, and a uniformly slow direct writer matches the same old late-state score. On new C, selective encoding scores **0.7565**, worse than direct fast's **0.6622** and outside the locally specified +0.05 tolerance. With a normalized error of **1.0 for predicting zero**, the old A signal has almost disappeared: it worsened from **0.7694** immediately after task A to **0.9885** after task C.

**Decision:** compound gate fails; no residue-specific protection or catastrophic-forgetting solution demonstrated. Eight fixed seeds 401–408, all eight favored selective over uniform fast on old A, but **none of that improvement survives the feature-rate-matched explanation**. The local test passed five unit checks and an independently running GitHub CPU workflow; claims remain synthetic.

The next discriminating hypothesis is learned slow *dynamics/operator structure*, not merely a linearly invertible re-encoding of the same vector. Force complete fast-state erasure, use a later identical neutral probe and compare history-dependent operator response against equally charged direct-state/slow-rate alternatives.


## Gate 3 (later October 29) — bounded operator coexistence works; residue advantage does not

A new [three-slot response-operator implementation](https://github.com/anttiluode/RoundAndRound/blob/main/structural_memory.py) and [registered-local benchmark](https://github.com/anttiluode/RoundAndRound/blob/main/docs/STRUCTURAL_GATE.md) replace Gate 2's cue-to-state storage with **slow transition structure** learned from short ringdown differences. The fast state is erased after each exposure. New, unseen probe directions later activate the learned operator, with no original training trace available. No class labels are provided to the learned cosine-similarity prototype router.

After development on seeds 301–308, **independent confirmation 501–508** preserves the same result. Operator-specific trajectory gain is defined relative to the no-memory base response (1=perfect, 0=no improvement). After sequentially learning three tasks A→B→C, the old A/B and new C gains for the 219-scalar context-routed slow operator bank are **0.997089 / 0.996825 / 0.997703**. An overwritable shared operator has **−1.095388 / −1.211567 / 0.997703**; a 216-scalar FIFO is **0.004771 / 0.007747 / 0.562644**. All A matrices are bitwise unchanged during later B/C writes in the tested, well-separated-context worlds. See the [results ledger](https://github.com/anttiluode/RoundAndRound/blob/main/results/STRUCTURAL_RESULTS.md) and [seedwise compact receipts](https://github.com/anttiluode/RoundAndRound/blob/main/results/structural_confirm_summary.json).

**Essential correction:** a matched **219-scalar context-routed direct-transition learner** ties the Sihti-residue learner to floating-point precision (matrix difference below 5×10⁻¹⁷). Because next state = current state − residue, these are algebraically equivalent updates. The demonstrated win is **modular allocation and gated writing**, not a novel residue learning rule, compression or emergent hippocampal mechanism.

**Predeclared attackers expose limits:** making A/B contexts nearly identical destroys old A gain (**−1.1094**); a fourth unfamiliar task D offered to three full slots is refused and has gain approximately zero; increasing test cue noise from 0.12 to 0.38 drops context routing to **52.93%** and old A gain to **0.5308**. The experimenter supplied well-separated clusters and a three-slot capacity. This is a **bounded, synthetic structural-memory mechanism**, not open-ended continual learning or evidence of an autonomous self.

**Next discriminating question:** how could the system learn *which contexts deserve distinct operators*, merge similar ones, and safely reallocate scarce slow memory without knowing task boundaries? Any improvement must exceed matched context-routed direct transition learning, not just a single shared overwritable operator.


## Gate 4 — active interrogation of ambiguous stored dynamics (October 29)

[RoundAndRound Gate-4 results](https://github.com/anttiluode/RoundAndRound/blob/main/results/ACTIVE_REENTRY_RESULTS.md) now distinguish *what the bank contains* from *what evidence a receiver can obtain*. Three learned 8D operators are identified from transient teaching responses even when their contextual cue centers are identical. Slow memory stores 219 scalars. Later, with fast activity erased, a limited controller chooses two unit-norm probes and receives one scalar response from an **external** unknown system per action. **Only that response evidence** can identify which stored dynamics currently apply; cue-only identification is 33.3% for three equally likely memories.

On independent confirmation seeds 701–708, active posterior-guided probes identify the current operator **77.29%**, versus **72.26%** for repeating the *best globally optimized fixed probe*, **54.62%** random and **33.33%** cue only. Operator-specific gain is just **0.5025**, far below the registered 0.80 requirement. Gate 4 is therefore **PARTIAL/FAIL**, not a universal reactivation win. An engineered information-gain eigenvector rule chooses probes; the system did **not** learn the probing rule from experience.

Noisy high-confidence retrieval-based writes make a small changed-A memory **worse** (response gain 0.99168 read-only → 0.96776 after external plastic updates), and occasionally damage wrong slots. A guard that rejects explicitly internal replay prevents those writes. Confidence and provenance alone are insufficient for safe reconsolidation.

A separate **post-confirmation** experiment uses posterior-weighted predictions from several stored loops concurrently. With exactly the same two external measurements and 219 stored scalars, but more rollout computation, fresh seeds 801–808 yield response gain **0.8045 soft adaptive**, **0.7059 hard adaptive**, **0.7124 soft optimized fixed**, **0.2885 cue-only prior mixture**. The soft-versus-hard difference is positive in 7/8 new worlds. This is ordinary Bayesian model averaging applied to dynamical memories, with encouraging relevance to active PresentMoment retrieval; it is **not** novel Sihti compression, biological hippocampal re-entry, an independent claim of selfhood or a fix for catastrophic forgetting.

Source: [active re-entry protocol](https://github.com/anttiluode/RoundAndRound/blob/main/docs/ACTIVE_REENTRY_GATE.md), [mixture follow-up](https://github.com/anttiluode/RoundAndRound/blob/main/docs/MIXTURE_FOLLOWUP.md), [next falsifiable learned-policy target](https://github.com/anttiluode/RoundAndRound/blob/main/docs/NEXT_EXPERIMENT.md).
