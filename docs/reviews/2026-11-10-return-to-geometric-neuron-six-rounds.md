# Return to the Geometric Neuron: six rounds, one inheritance, and a missing learner

*10 November 2026 · Source-linked audit of [ReturnToGeometricNeuron](https://github.com/anttiluode/ReturnToGeometricNeuron), a direct coupled-loop descendant of [GeometricNeuronOriginReview](https://github.com/anttiluode/GeometricNeuronOriginReview).*

**Evidence status.** The source repository publishes its Python simulator, browser parity test, six-round experimental scripts and numerical receipts. Sol's fourth- and fifth-round scripts were executed successfully through [GitHub Actions](https://github.com/anttiluode/ReturnToGeometricNeuron/actions); the source's six existing regression tests passed. Fable reports reproducing the fifth round locally and ran a sixth-round timing/last-block control, committed as [`experiments/round5_check.py`](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/experiments/round5_check.py) and [`results/round5_check.json`](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/round5_check.json). Genealogy has inspected sources and results but **has not independently rerun the entire six-round study**. These are synthetic simulation results, not biological or general-AI demonstrations.

## Documented ancestry

```text
PerceptionLab / ecg.json
  └── GeometricNeuronOriginReview
        archived node code; bit-exact scalar response; W=50, d=4, period 59
          └── ReturnToGeometricNeuron
                six copies of that reduced loop; coupled splitter taps;
                optional designed local plasticity, trigger and short refractory
```

The original unit is a **delayed finite-history feedback oscillator**: a checkerboard is measured by an image-to-vector path, and the first four splitter outputs feed a homeostatic switching controller. November 8 established the bit-exact reduction; [November 10's committed forgetting-clock experiments](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/FORGETTING_CLOCK.md) analyze the refractory-like 59-tick cycle, finite resets and abrupt forgetting. Those results do **not** establish membrane physics or synaptic plasticity in the original loop. They should not be confused with the extra learning and trigger mechanisms in its later colony.

## Six experimental rounds

| Round | Main question | Observation and boundary |
|---|---|---|
| **1** | Can six connected copies retain order and resist fast common forcing? | News-gated weights encode taught order and mostly stop writing under 20-tick common forcing; 22/24 final-weight history decodes after a 1,000-tick event. This learning rule was designed, and recovery claims initially lacked a heterogeneous control. |
| **2** | Is it learning or simple asymmetry, and is communication phase-sensitive? | Any unequal frozen weight matrix breaks exact long-term synchrony; learning adds **direction-related** behavior relative to shuffled weights. A single-loop pulse can delay the next beat in phase-dependent windows (an 8-tick substructure within period 59; its cause is not established). |
| **3** | Does a learned two-order colony select a replay after a cue? | **No.** Native inhibitory-only coupling gives ~0–1% exact two-order replay. A hand-coded excitatory trigger alone causes runaway activity; a 10-tick refractory allows one direction to replay but not two reliably, and spontaneous replay is common. |
| **4** | Can the dynamics express both directions with a good frozen matrix? | **Yes, imperfectly.** Hand-set bidirectional nearest-neighbour links (0.22, distant 0.02) achieve **62.5% forward, 67.7% reverse** exact 40-tick order across 96 paired trials per condition; matched no-cue **12.5%/27.1%**, shuffled ideal **6.3%/1.0%**. This proves no extra context unit is needed for this specific opposite-end-cue task, not that the matrix was learned. |
| **5** | Can local event timing learn a usable matrix? Do learned tap filters add value? | An engineered **nearest preceding forced beat** credit rule produces adjacent/shortcut weights **0.1976/0.0319**. With fixed clean-beat taps 0–1 it replays **68.8%/80.2%**, compared with original News weights **7.3%/1.0%**. Learned 16-tap filters score **65.6%/66.7%** and **do not beat fixed taps**. Shuffle tests abolish most replay. |
| **6** | Does round five work across different teaching gaps, and are spontaneous replays a confound? | The unchanged rule builds adjacency for gaps **1–5**; at gaps **6 and 8** it does not, exactly matching its programmed 1–5-tick eligibility window. Reversing the final teaching block flips no-cue dominance: for three-tick teaching, **0123 spontaneous 3% → 31%**, **3210 spontaneous 32% → 5%**. Even at gaps where nothing was learned, cue-3 replay can reach **17–25%**. Those numbers therefore cannot all be credited to persistent learned weights. |

**Comparability note.** The ideal hand-set chain reads **62.5%** forward in round four but **51.0%** in round five. These were different experiment runs and starting states: round four replaces weights after a conventional News-trained AB state; round five starts from the separately forced nearest-predecessor training state. The pair should **not** be presented as a discrepancy in one matched test, nor pooled into a single point estimate.

## The negative result is the most important guardrail

The fifth-round nearest-predecessor rule was **not** a self-teaching geometric neuron. During teaching, the original four units are **externally forced** into an A or B sequence, while network weights remain 0.02. The new rule counts which forced beat came closest before another; it converts those counts into a weight matrix *after teaching*. The same weight matrix could be computed from the known teaching schedule alone, without running the oscillators. Further, its replay hops use a **hand-written five-tick trigger latency**, regardless of the teaching gap. This solves *sequence-adjacency extraction from an observed timetable*, not endogenous, state-dependent credit assignment.

The original News rule, by contrast, uses each unit's own recent variance as a learning gate. It preserves some order but **does not construct the required bidirectional adjacency**. The two strengths have not been combined into a successful rule.

The sixteen raw splitter outputs are correlated measurements of a single checkerboard scale, not 16 independent latent dimensions. Tap choice changes what signal reaches a neighbour (clean beat, lead-up, idle ripple or idle activity), and shuffle ablations show it matters. Yet the currently engineered learned tap filter fails to outperform a fixed choice. That is not evidence geometric learning is impossible; it is evidence this example doesn't establish a benefit.

## What is actually still open?

**Can a locally excitable unit's own state influence *what it learns*, while the network discovers useful routing without a teacher-schedule counter?** The next discriminating control would teach using heard input rather than directly forced postsynaptic beats, freeze all externally calculated counts, and compare against schedule-only, fixed-geometry, shuffled and hand-specified-chain baselines. A later generalization test should vary teaching gaps *beyond* the initial eligibility window without retuning it.

A population of these units has a real distributed state, so its joint phase/history can be viewed as a vector; that observation does not make it a transformer or attention model. Nor does superficial nested timing establish MIT's measured cognition-related theta/beta/gamma organization. Functional machine-learning comparisons (ordinary RNN/reservoir/sequence memory, matched capacity and data) remain missing.

## Primary receipts

- [Original ECG reduction](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/CAUSAL_REDUCTION.md)
- [Committed original forgetting-clock analysis](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/FORGETTING_CLOCK.md)
- [Colony README and six-round ledger](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/README.md)
- [One-loop phase response](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/phase.json)
- [Third-round negative](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/cue.json)
- [Fourth-round ideal chain](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/ideal_chain.json)
- [Fifth-round learned adjacency and tap controls](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/tap_learning_round5.json)
- [Sixth-round spacing and teaching-order controls](https://github.com/anttiluode/ReturnToGeometricNeuron/blob/main/results/round5_check.json)
