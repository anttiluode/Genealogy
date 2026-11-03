# November 3, 2026 — BrahSol × BrahClaude: the path that answers back

**Source-linked Genealogy review.** Parallel synthetic experiments; not evidence of real-neuron introspection or an invented biological synapse. [BrahSol](https://github.com/anttiluode/BrahSol) · [BrahClaude](https://github.com/anttiluode/BrahClaude) · [PerceptionLab](https://github.com/anttiluode/PerceptionLab) · [GeometricNeuronOriginReview](https://github.com/anttiluode/GeometricNeuronOriginReview).

## How these branches arose

The earlier [checkerboard homeostat](https://github.com/anttiluode/GeometricNeuronOriginReview) used a controller to change a generated checkerboard, resize it, flatten it, and feed four scalar outputs back into the controller. The coupler **sums** those outputs. Changing the observation grid changes the effective closed-loop dynamics, but the program did not learn a model of how its interventions cause returns. The November 3 conversation turned this into a testable question: can a bounded pinger learn the pathways between stimulation and feedback when those pathways have their own time-dependent states?

Two separate repositories address different halves; neither is a fork of the other.

## BrahSol — what should I ping, and what happens when the medium changes?

[README](https://github.com/anttiluode/BrahSol/blob/main/README.md) · [v2 code](https://github.com/anttiluode/BrahSol/blob/main/brahsol_v2.py) · [v2 results](https://github.com/anttiluode/BrahSol/blob/main/RESULTS_V2.md) · [write–wait–read pilot](https://github.com/anttiluode/BrahSol/blob/main/route_probe.py).

A hidden network of **24 leaky recurrent units** has activity adaptation, optional Hebbian weight changes, **8 intervention ports**, and **4 observed returns**. A controller learns action-conditioned one-step predictors and chooses pings by random, shuffled-balanced, homeostatic or uncertainty-weighted strategies.

- **v1, common held-out world:** after 100 training pings, active RMSE **0.02571** versus random **0.03146** and balanced **0.03394** (20 seeds). At 650 pings the active/random difference is tiny (**0.01631** versus **0.01654**). This is a particular sample-efficiency result, not a universal active-learning benefit.
- **v2, engineered rerouting at tick 170:** the intervention replaces some recurrent input weights *and permutes the stimulation-port mapping*. Late post-change RMSE (12 seeds) is **0.0483 active with forgetting**, **0.0561 random with forgetting**, **0.1008 active without forgetting**. Forgetting old associations is the larger effect; **removing Hebbian learning hardly changes it**.
- **route_probe.py:** an intentionally identifiable two-route memory construction gives about **97.6% balanced** versus **97.4% random** write–wait–read accuracy; no priming or resetting memories returns performance to about chance. It shows a mechanism, **not discovered strategic priming**.

The repository's published v1/v2 results are artificial and source-reported; these calculations were not independently rerun by Genealogy. The main limitation remains that the controller is not yet learning an unknown biological synapse's mechanisms from experience.

## BrahClaude — what do the routes themselves remember?

[README and numerical gates](https://github.com/anttiluode/BrahClaude/blob/main/README.md) · [preregistration](https://github.com/anttiluode/BrahClaude/blob/main/PREREGISTRATION.md) · [edge implementation](https://github.com/anttiluode/BrahClaude/blob/main/brah/edges.py).

Each route keeps 8 exponential pulse-history traces with octave timescales from 2 to 256 steps. The differences between consecutive traces are called *Sihti residues* and telescope exactly to the slowest trace. A binary spike's release amplitude depends on the stored history and per-terminal band weights. Before the clipping nonlinearity the result is a **second-order Volterra kernel**.

**Important correction:** Sihti differences are invertible, so they supply no new information beyond the original exponential traces. The important resources are **multiple timescales and distinct readout projections**.

- **G0:** numerical telescoping/Volterra identity agrees to about **5 × 10⁻¹⁵**.
- **G1:** optimized hidden-route identification reaches **99.4%** against a **94.7%** best fixed protocol, but misses its registered gain threshold **+0.05** (achieved **+0.047**). Count it as a *failed* registered gate, not a pass.
- **G2a:** after 150 completely output-silent steps, a neutral ping identifies which routes were written at **99.6%**, and residue resetting returns **12.5%** chance. However the decoder is handed separate outputs for eight routes.
- **G2b:** for 16 classes combining pulse amount and age, four **heterogeneously tuned terminals** reach about **85%** versus **41%** for four homogeneous terminals. It proves a benefit against *this homogeneous readout*, not against every equal-budget raw-trace readout.
- **G3:** reward-only policy finds which route and time to prime for a later third-party event. Since pre-clipping history is linear, the best strategy is a **matched filter**, explicitly acknowledged by the project.
- **G4:** burst multiplexing misses the preregistered event-rate correlation **0.8** (achieved **0.757**, at its chosen ideal event-count baseline), despite strong burstiness decoding. Two bug fixes after the first run, including one affecting a control, are disclosed in the README.

## Shared conceptual frontier: addressability and the price of asking

These systems must not be conflated. BrahSol learns from returns but has no eight-octave Sihti edge stack. BrahClaude places state on routes but often supplies known decoder templates and individually readable route outputs.

There is a simple exact **failure case** in Claude's G2a. Every item activates two of eight identical facilitating routes. At read time the two written routes each answer about **1.4202**, and the other six answer **1.0**. Summing into a single undifferentiated input produces **2 × 1.4202 + 6 = 8.8404** for *every* route pair. Even though the stored memory persists, its *address* is lost. Selectively targeting subsets or reading separate dendritic compartments could break that symmetry; this has not been demonstrated in a biological neuron.

Likewise, a probe that reads synaptic resource state might itself alter that state. The next disciplined experiment would compare **global pings, selective pings, and no read**, holding the final diagnostic time and stimulation budget constant; use a Tsodyks–Markram-style nonlinear depletion/facilitation control, measure both physical state separation and decoding, and test whether a learned controller maintains its outgoing-ping history (an efference copy). An additional slow-plasticity control should distinguish short-lived residue from genuine long-term connectivity change.

## What survives

*The interesting inheritance is not the name “Sihti,” nor a claim that a neuron knows itself. It is a concrete experiment-design problem: a bounded observer has to learn which interventions make a changing, memory-bearing pathway identifiable, while paying for the back-action of interrogation.*

The open test is whether a policy that **chooses when to write, when to ping, and when to stay silent** beats equally budgeted fixed/random strategies in unseen hidden media. No such full closed-loop result is established by the two reviewed repositories yet.

**Evidence status:** all numerical results above are source-reported, with no independent Genealogy reruns or biological observations. [BrahSol source](https://github.com/anttiluode/BrahSol) · [BrahClaude source](https://github.com/anttiluode/BrahClaude).
