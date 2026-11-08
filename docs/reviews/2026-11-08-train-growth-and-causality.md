# November 8, 2026 — The rails start building their own roads

[Live wall chapter](https://anttiluode.github.io/Genealogy/#nov8-railway-causality) · [Curated archaeology pass](../../data/passes/november-8-train-growth-and-causal-audits.json)

This day's entry is based on the user's November 8 GitHub contribution tally: **15 commits across six repositories**. The atlas census changes **599 → 604** because only five repositories were absent. **GeometricNeuronOriginReview was already in the inventory** and receives a reviewed node rather than another census row.

| Repository | Nov 8 commits | What changed |
| --- | ---: | --- |
| [TurntableNeuron](https://github.com/anttiluode/TurntableNeuron) | **5** | Rotating input, phase-bearing trains, pilot synchronization, listening windows and classical phasor path sums |
| [TurntableAISol](https://github.com/anttiluode/TurntableAISol) | **4** | Nine communicating stations over three layers, with apical, basket and chandelier roles |
| [KasvavatKiskotSol](https://github.com/anttiluode/KasvavatKiskotSol) | **3** | Deterministic timed exploratory network, material competition, cut and retarget |
| [KasvavatKiskotClaude](https://github.com/anttiluode/KasvavatKiskotClaude) | **1** | Independent stochastic ant-like railway with flow, Physarum and oracle baselines |
| [TorsionFreeMirrorLock](https://github.com/anttiluode/TorsionFreeMirrorLock) | **1** | November 8 correction of hidden-parameter fibers, reader drift and the unearned group-theoretic name |
| [GeometricNeuronOriginReview](https://github.com/anttiluode/GeometricNeuronOriginReview) | **1** | Exact causal reduction of the September ECG-like loop, with the real host period |

## Phase is more than decoration — TurntableNeuron

The [TurntableNeuron README](https://github.com/anttiluode/TurntableNeuron/blob/main/README.md) documents four numbered iterations from the original v2 yard. A fixed turntable rotates through three dendritic tracks and the axon exit; incoming advection-diffusion pulses are gated by direction and phase. The v2 scalar accumulator is monotone, so it cannot compute XOR. The v3 complex platform adds phasors and can cancel balanced opposing signals, allowing a *particular* XOR. Releasing departures after a delay derived from the platform's angle carries **1.44 additional bits** over carriage count in a source-reported 512-pattern, zero-jitter experiment.

The v4 pilot gives a shared sender clock without letting the information-bearing train itself reset the listener phase. The report preserves all three correct routes across **32/32** common-delay shifts, compared with **4/32** without pilot synchronization. It does not eliminate jitter private to data trains. V5 revisits window width, matching windows to address spacing, multiple-period aliasing and a classical sum of arrival phasors; the README reports **19 Node tests** and unmodified earlier result receipts.

The single-frequency phasor sum is mathematically an interference-like path accumulation. It is **not** a Feynman quantum path integral or evidence that the yard independently solves fastest-path problems. These are deliberately engineered, nonbiophysical rules.

## A single yard becomes a network — TurntableAISol

The independent [TurntableAISol README](https://github.com/anttiluode/TurntableAISol/blob/main/README.md) describes **nine** hard-wired yards in three layers, with periods between **29 and 43 ticks**. Upward excitatory packet routes, descending apical input and lateral connections coexist with separate simulated basket and chandelier interventions.

Source-reported controlled comparisons: **basal 0.7 alone yields 0/30 departures**, whereas apical context allows **30/30**; basket input reduces an accumulated **1.5 → 0.3699** while chandelier input vetoes the exit and preserves **1.5**. In the designed 420-tick all-yards scenario, the network makes **72 departures**, versus **31** with its vertical routes disabled. The layout is causal and interactive, but it has **fixed wiring**, not learned growth; the physiological names are analogies to distinct computational functions rather than measured biological mechanisms.

## The rails themselves learn — two *independent* implementations

These two repositories were built simultaneously from the vine-feeler, Tokyo/Physarum and phase-window discussion. **They are siblings, not successive forks of each other's code.** Both change operational connectivity with a construction budget, but the algorithm that decides where to build is importantly different.

### [KasvavatKiskotSol](https://github.com/anttiluode/KasvavatKiskotSol/blob/main/README.md)

A fixed **12×7** grid with candidate exploratory edges and an overall **15-unit** construction budget. The destination sends a reply after the earliest phase-gated exploratory arrival. The simulator retraces that arrival's predecessor chain and credits the winning edges; active rails exist when their material exceeds a threshold. The same JavaScript runs the offline visual laboratory and experiments.

The source reports **73 ticks** for phase-sensitive delivery against **94** for flow-only on this one hand-designed terrain. After a rail is cut, a new **80-tick** route grows, while flow and static networks fail at the selected budget. After a destination shift, **78 ticks** versus **118** for flow-only. Eleven tests and passing GitHub Actions are reported.

**The crucial methodological limit:** the exploratory scheduler itself is a time-dependent earliest-arrival search over all candidate edges, comparable to a time-aware Dijkstra computation. The ACK remembers the winning predecessor path and material is managed globally. This demonstrates *storage of selected routes as built rails*, not spontaneous local discovery of a shortest-path algorithm, and not a general traveling-salesman solver.

### [KasvavatKiskotClaude](https://github.com/anttiluode/KasvavatKiskotClaude/blob/main/README.md)

A separate **7×7** graph with **226** candidate rails, a **14-unit** global construction budget and **100 stochastic walkers each epoch**. Walkers reinforce a path only when the arrival is inside the receiver's phase window. The project reports baseline comparisons to static wiring, time-blind flow reinforcement, a Kirchhoff-style Physarum model and a timing-aware oracle on 20 worlds.

The worlds are **deliberately selected so the cheapest ordinary route misses the timing window**. In that task, phase-gated growth succeeds in **14/20**, flow-only in **5/20**, and Physarum in **1/20**; the accepted route's median length is **1.49×** the timing-aware oracle cost. After cutting the strongest used rail, the phase learner succeeds **13/20**; after retargeting and changing the window, **19/20**. When timing no longer matters, **Physarum wins the ordinary shortest-route task 20/20**.

The main learner is susceptible to false-history lock-in: preload an inferior but acceptable route and the default high-feedback setting stays stuck or fails in **15/20** cases. Rewards retrace complete remembered paths, so this is ant-colony-like global trail memory, not yet the strictly local forward/reply coincidence mechanism originally proposed. The budget is globally administered. Neither repository stores its own desired goal internally.

## Causal audits that put a boundary around grand interpretations

### [TorsionFreeMirrorLock](https://github.com/anttiluode/TorsionFreeMirrorLock/blob/main/README.md)

The earlier Friday mirror-lock hides a dynamical sector behind an imposed reflection symmetry. This experiment instead constructs a **fiber of indistinguishable interior graph weightings**: four boundary ports cannot identify which interior parameter realization produced their transfer function. The chosen case has a source-reported **nine-dimensional parameter fiber**, and a privileged clamped-port, interior-access key can read a stored word.

The November 8 review corrects the original description. A stale fixed decoder that fails after plasticity does **not** imply immediate word erasure—recalibration may recover the same 64 labels until noise and saturation actually collapse their separation. Public-boundary updates and a shared hidden gain retain the boundary equivalence in the tested system. Maps connecting hidden words do **not** compose, so the title is **not** proof of torsion-free group structure. All graph modes can reach ports: this is hidden **parameter identifiability**, not an inaccessible state mode or a self-repairing memory with a local key.

### [GeometricNeuronOriginReview](https://github.com/anttiluode/GeometricNeuronOriginReview/blob/main/README.md)

The archived PerceptionLab checkerboard → image vector → four feedback samples → homeostatic controller appears high dimensional, but the complete image branch can be replaced bit-exactly by a **scalar lookup** for the controller. The real closed-loop state still includes a nonlinear switch and **ordered 50-sample** feedback history. The host's four-tick update scheduling gives the faithful cycle **period 59**; the old **period 52** came from running the loop at one tick per update. The integral_state variable is updated but never read in this mode. Clamping feedback stops the rhythm and permuting the window changes the future even with the same mean and variance. The feedback wires are not four eigenmodes, and the old system was not a proven biological ECG generator.

## The connective tissue — documentary relationships

1. **PerceptionLab → GeometricNeuronOriginReview**: source extraction and reduction of the historical graph.
2. **Friday → TorsionFreeMirrorLock**: explicitly compared hidden-storage questions; conceptual convergence, *not* the same code or hidden-sector mechanism.
3. **SliderV3 → TorsionFreeMirrorLock**: the strain plasticity rule is explicitly transferred for testing.
4. **TurntableNeuron → TurntableAISol**: selected angular gate and phase-release concepts, implemented in a separate multilayer engine.
5. **TurntableNeuron → KasvavatKiskotSol and KasvavatKiskotClaude**: timing-window research question extracted into two independent rail-learning architectures.
6. **TurntableAISol → KasvavatKiskotSol**: named conceptual bridge; the nine-yard apical/basket/chandelier design is *not yet incorporated*.
7. **KasvavatKiskotClaude ↔ KasvavatKiskotSol**: independently convergent experiments, not verified implementation ancestry.

## Where the next falsifiable question sits

Test all learning rules on a **shared, varied set of maps** under identical delay-window targets, exploration/energy accounting and construction budgets. Compare against a strong *time-aware* shortest-arrival algorithm, not merely a time-blind flow model. Remove privileged path traceback, decentralize resource movement, inject shared and private timing jitter, damage true bridges and change targets after long training. Keep the negative and trap outcomes.

A second, genuinely separate **Levin-shaped** test asks whether an internally readable and rewritable target, held within the medium, could guide local repair without an external experimenter-held oracle. Neither growing-rail version accomplishes this yet.

*Provenance:* the six commit counts are supplied by the user. Scientific numbers and test counts above come from the cited project READMEs/results; Genealogy does not claim to have independently rerun all six project's experiments.
