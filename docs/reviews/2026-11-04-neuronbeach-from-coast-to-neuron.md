# NeuronBeach — a neuron made legible as a coast

**Reviewed:** 2026-11-04  
**Source:** [NeuronBeach](https://github.com/anttiluode/NeuronBeach) · [single-neuron page](https://anttiluode.github.io/NeuronBeach/) · [six-neuron network](https://anttiluode.github.io/NeuronBeach/network.html)  
**Experiment:** [single-neuron code](https://github.com/anttiluode/NeuronBeach/blob/main/sim.js) · [network code](https://github.com/anttiluode/NeuronBeach/blob/main/netsim.js) · [tests](https://github.com/anttiluode/NeuronBeach/tree/main/tests) · [committed results](https://github.com/anttiluode/NeuronBeach/tree/main/results)

## Origin and the working picture

The beach metaphor developed in the ComputingBeach discussions: waves pass over a medium whose past can affect later passage. NeuronBeach turns that into a deliberately **neuron-like illustration**: low-pass dendritic marshes, a collecting soma pool, an AIS berm and threshold-triggered sluice, a regenerative axon, back-propagating spikes, synaptic sandbars, eligibility footprints, a neuromodulatory tide, and a distant apical-tuft hot zone. The interactive pages need only HTML/JS.

This is a convergence of the wave-memory question and earlier geometric/dendritic-neuron illustrations, **not evidence of a new biological neuron law**. The network simulator implements linear water-like propagation across graph channels with explicitly coded threshold, spike, synaptic learning, inhibition, and reward/tide rules. A synaptic sandbar is stored as a numerical weight, **not sediment dynamically eroded by a wave stress PDE**.

## What the committed source reports

Single neuron (tests/single.js; results/single.json):

- One, two, three simultaneous basal swells produce unspiked pool peaks **0.211 / 0.423 / 0.634**; the configured 0.5 berm fires only for the third.
- At tested marsh settings, equal-strength slow swells produce **2.11–2.82 times** the somatic peak of fast ripples: an illustrative low-pass filter.
- A far-shore input alone does not ignite; paired with a basal volley it generates **5–6 spikes** when delivered within about **0–80 arbitrary simulation steps**, but not at +120/+200.
- Eight pairings strengthen the A sandbar **0.60 → 1.60** until A alone fires. Tide mode defers the effective weight change until tide events. An input arriving 30 steps after the somatic spike can still be potentiated because the back-propagating signal has not yet reached that distal mouth; +80 and +140 produce depression in the documented test.
- A weak ping does not change persistent weight or cause a spike. **However it does increment the transient eligibility trace** via inputWave(), so “no change” does not mean no internal state change.

Network (tests/experiments.js; results/network_heldout.json):

- Six neurons are arranged visually as a ring but each projects to every *other* neuron via delayed, event-driven input. The training order is shuffled across test seeds; it is **not fixed by spatial ring position**.
- Settings chosen on seeds 1–10 and frozen for held-out seeds 101–130. After 15 lessons, waking the first neuron yields **30/30 complete ordered replays**; shuffled-order training, no training, frozen plasticity and tide-without-reward each yield **0/30**.
- Inhibitory anti-waves matter: **14/30** succeed without them. Learned forward synapses approach **1.00**, reverse **0.05**. Replay interval is about **49 steps**, versus **60** during lessons.
- Increasing to eight neurons without increasing the total incoming sand budget reduces full replay to **7/30**, and reward-gated eight-neuron replay to **0/30**. Scaling the budget after observing failure improves it, but that intervention is **post hoc**.
- Homeostatic berm adjustment fails on the documented dev settings (**0/10**). That failure is part of the evidence, not hidden.

## Boundary between analogy and biology

AIS is better pictured as a **threshold-triggered regenerative wave machine** than as a literal reservoir releasing accumulated water. Biological action potentials arise from voltage-gated ion currents and electrochemical gradients; propagation can proceed axonward and back toward soma/dendrites, but not as two identical water waves. The code models the mechanism with chosen switches and state variables, not sodium-channel kinetics, ion transport, a quantitative dendrite, or biological time units. NeuronBeach is an explanatory *toy*, not validation of the water analogy as biophysics.

The test scripts compute and print outcomes; they do not contain explicit assertions. The recorded numbers are **source-reported** from the repository, not a new independent Genealogy replication.

## Why this belongs in the wall

The durable contribution is pedagogical: flow, filtering, spike initiation, backpropagation, timing-based learning and reward gating can be watched as parts of one physical metaphor. It also makes a useful experimental distinction: a weak query can leave a temporary trace despite not changing persistent weights. The system demonstrates simple learned sequential replay, **not** context-dependent retrieval, general memory, physical self-modification by scour, or a new synaptic learning rule.

**Next falsifier:** teach *two conflicting orders*, then ask whether a **separate apical-tuft context** can select which order is recalled; compare context removed, shuffled, wrong, and soma-only controls under equal activity and identical parameter counts. Also test robustness, interference and spontaneous waves. Until then, the successful six-step chain is a narrow, well-controlled toy result.
