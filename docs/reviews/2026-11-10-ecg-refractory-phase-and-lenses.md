# The ECG-like loop beats when it forgets — a phase, feedback and lens follow-up

*10 November 2026 · Follow-up to [GeometricNeuronOriginReview](https://github.com/anttiluode/GeometricNeuronOriginReview) and the [8 November causal reduction](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/CAUSAL_REDUCTION.md).*

> **Updated evidence status (10 November 2026):** At this note's initial writing, the pulse mechanism, 204-setting sweep, 3,000-start search and phase-response studies were **reported from Fable's workspace before their code was available to Genealogy**. They have since been committed in [experiments/forgetting_clock.py](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/experiments/forgetting_clock.py), with [results/forgetting_clock.json](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/results/forgetting_clock.json) and the [mechanism note](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/FORGETTING_CLOCK.md). The reported numbers are therefore **source-code-backed rather than uncommitted claims**. Genealogy has inspected the published methods but **has not independently rerun the entire sweep**. A subsequent, separate six-unit descendant with its own measured limits is [ReturnToGeometricNeuron](https://github.com/anttiluode/ReturnToGeometricNeuron) ([six-round review](2026-11-10-return-to-geometric-neuron-six-rounds.md)).

## What was already established (published reduction)

The archived PerceptionLab circuit is coupler → regenerated checkerboard → image-to-vector → first four samples → coupler, with a four-tick host delay. The full image path is causally replaceable by one response lookup `r = F_D(q)`, bit-exact over 3,000 ticks at dimensions 256, 1024 and 2048. The active state includes an **ordered 50-sample sliding history**, the nonlinear amplification/damping switch and delayed values in flight. The faithful 256-dimensional reload has a **59-tick cycle** (not the former 52-tick one-step reconstruction); its so-called `edge_of_chaos` mode is a deterministic switching oscillator, not evidence of chaos. The integral-state variable is written but never read in this mode.

Clamping its feedback to a constant stops the rhythm after its window flushes. Rearranging the sample order while retaining the last reading, mean and variance changes subsequent behavior. Raising vector dimension also changed the spatial footprint of the **four feedback samples**, not merely the richness of the image: at D=1024 the original sensor yielded an 8-tick rhythm, while a fixed-footprint control recovered a long cycle (113 ticks). At D=2048, the published cycle spent 93% of its time in a zone where the scalar feedback read zero. These are sensor/feedback effects, not evidence of neuron-like eigenmodes.

## Fable's proposed mechanism: an excitable forgetting clock

Fable's now-published follow-up describes the 50-sample window as a **refractory-like memory**. In its reported 256-dimensional run, a burst includes two large sampled returns (3.47 and 3.88), holding estimated variance above target. Most intervening ticks idle between square sizes 43 and 48. Once those returns leave the sliding history, the controller crosses its hard threshold, produces a kick and passes through a blind response region; a zero relative to the nonzero setpoint is an effective input, not an inert absence.

Its explanatory period count is **50 (window) + 1 (threshold recognition) + 4 (outbound delay) + 4 (return delay) = 59**. This is a proposed mechanism for this operating regime, **not a universal period theorem**. The published follow-up reports a 204-setting window/delay sweep: the approximation `period ≈ window + 2 × delay + c` had `c` in [−1, +4] except for 18 settings exhibiting approximately doubled periods. The period decomposition is supported by the source's committed experiment and report; Genealogy still has not independently rerun its parameter sweep, so it is a bounded result for this configuration rather than a universal theorem.

## Reported interventions: one sampled cycle, finite reset, weak-push insensitivity

- **Attractor search:** The committed source reports 3,000 random initial states converged to the same 59-tick limit cycle. This supports one observed basin under that sampling; it does **not prove** there are no other attractors.
- **Phase kicks:** The published experiment tests a one-tick kick at all 59 cycle phases. Kicks through 0.03 produced no lasting phase displacement; a 0.000001 kick washed out in four ticks. Positive kicks +0.3/+1 shifted phase by one tick at most phases; a −1 kick commonly restarted the phase clock.
- **Interpretation:** The current staircase response has little small-perturbation sensitivity yet large finite-perturbation effects. Thus **zero infinitesimal gradient does not imply zero finite causal effect**. The cycle could provide a resettable timing reference; it has **not** been shown to retain independently writable information about previous histories, nor to implement local learning.

The reported tests **do not establish** that all possible internal histories are erased; rather they suggest no persistent, distinguishable memory *beyond phase* in the sampled attraction regime. The 59 phases correspond to fewer than six binary bits of *possible phase states*, **not six demonstrated reliable information bits**.

## What kind of biological analogy survives?

This is **not a neuron**, cardiac cell, synapse or learned neural network. No ion-channel dynamics, membrane voltage, neurotransmitter release, pre/postsynaptic junction or enduring weight update is modeled. Still, the loop shares an **abstract dynamical motif** with excitable systems: threshold, recovery time, temporary suppression after activity and phase resetting by a strong disturbance.

A **synapse analogy** can be productive only in this limited sense: recent signaling can change responsiveness to the next signal, much as short-term facilitation/depression changes transmission efficacy. But the loop's controller describes a global delayed homeostatic oscillator; it has no identified synaptic transmitter state, separate pre- and postsynaptic units or demonstrated synaptic plasticity. The 50-sample window is better called **refractory-like history** than a synaptic weight.

Noble's [voltage-clamp illustration](https://pmc.ncbi.nlm.nih.gov/articles/PMC3262309/) and the ECG feedback clamp both show that rhythmic activity depends on closed-loop coupling. **They do not share the same biological mechanism**. In the archived ECG case, clamp means holding a software feedback value constant; in Noble's heart example, membrane voltage is clamped and voltage-sensitive channel currents relax.

## The lens insight: more pixels ≠ deeper explanation

The ECG-like waveform invited a biological explanation, then code reduction dissolved the attractive but unsupported description. Increasing vector dimension altered a measurement operator within the control loop, creating genuinely different dynamics. A changed observation can change the observed world **when the observation closes a feedback path**.

Distinguish three claims:

1. **Blur:** a coarse observer omits fine distinctions.
2. **Aliasing or measurement distortion:** a coarse or changed sampler can create apparent patterns or change which distinctions are seen. The D=1024 result is specifically a **changed sensor footprint in feedback**; it should not automatically be called classical frequency aliasing.
3. **Intervention-tested causal model:** the reduced lookup, ordered window, delay and switch predict the waveform and its response to clamping. This lens may be lower-dimensional yet more causally informative.

No resolution level is inherently more truthful. A deeper explanation is one that survives carefully chosen interventions and predicts when another apparent explanation will fail.

## Later tests and remaining open question

The [10 November forgetting-clock note](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/FORGETTING_CLOCK.md) **now includes** a bounded, six-variant smoothing study. The original hard loop is phase-rigid, while tested softened versions gave lumpy or irregular phase responses, not a measured smooth proportional gradient. The separate [six-round colony](2026-11-10-return-to-geometric-neuron-six-rounds.md) measures phase-gated communication and two-direction replay, but its most successful learning rule counts externally forced teaching beats. A genuinely **self-generated, state-gated learning rule** that constructs useful routing—and an external task comparison—remain open.

A smooth phase response could help credit assignment, but **having a limit cycle does not by itself guarantee a usable training gradient**. Nor does a phase-resetting controller imply that a synapse has been simulated.

## Provenance and links

- [Source model and archived nodes](https://github.com/anttiluode/GeometricNeuronOriginReview)
- [Reproducible 8 November causal reduction](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/CAUSAL_REDUCTION.md)
- [Genealogy's 8 November review](2026-11-08-train-growth-and-causality.md)
- **10 November follow-up:** initially reported in conversation; now backed by committed [experiment](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/experiments/forgetting_clock.py), [results](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/results/forgetting_clock.json), and [note](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/docs/FORGETTING_CLOCK.md). No independent full Genealogy rerun.
- [Six-round coupled-neuron descendant audit](2026-11-10-return-to-geometric-neuron-six-rounds.md): successful hand-specified replay, engineered timing-counter learner, and negative controls.
