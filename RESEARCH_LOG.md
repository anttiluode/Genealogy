# Research log

## 2026-09-15 — first archaeological scaffold

This first graph is intentionally sparse. The repository census and the genealogy are different objects: a repo can exist in the census without receiving a lineage edge until there is evidence.

### Strong first-pass findings

- **PhaseStigmergy → FunctionalArbors** is a real lineage: the later arbor work explicitly reuses a PhaseStigmergy-style Laplacian/opportunity growth process, while keeping the negative phase-specific results visible.
- **Operaattori → OperaattoriJako** is an unusually clean extraction: a broad morphology-to-operator study produced a small reusable transport-vs-feedback diagnostic.
- **Geometric-Neuron → GeometricNeuronV24** is a correction lineage: V24 strips away the old thermostat story and keeps the addressable-observation problem.
- **GeometricNeuronV24 + TinyAvatar2 → ReadWrite** joins sensing and intervention as `M J`.
- **LentoOrava** is the strongest practical extraction in the current AI/neuron spine because its scalar intervention idea became PulseTriage rather than remaining only an analogy.
- **AnttisNeuron → GrowingAnttisNeuron → ActiveVectorNN → NewMachine → FusionMachine** is unusually explicit in the repositories themselves.
- **Clockfield** belongs in the atlas partly because its direct adaptive-weight-decay test was negative.
- **Kompressori** is a model case of failure producing a better object: partial-field reconstruction mostly failed, revealing response geometry and then low-rank operator updates.

## 2026-09-15 — Geometric Neuron ladder pass

The GeometricNeuron version numbers initially suggest one cumulative theory. Reading the repositories does **not** support that simple picture. The family contains at least four different scientific eras.

### Era 1 — the origin accident and its later autopsy

The PerceptionLab ECG loop mattered historically, but later audits show why it is dangerous to let the origin myth harden into the mechanism.

`GeometricNeuronOriginReview` freezes the old graph and shows that the four feedback values were spatial samples from a resolution-dependent coarse image representation, not four eigenmodes. Because the readout is inside feedback, changing `output_dim` changes the measurement operator and therefore the future trajectory.

`GeometricNeuronV21` goes further: the loop is a quantized aliasing staircase wrapped in a finite-memory variance thermostat. Its most important role in the genealogy is corrective. It explicitly distinguishes that old loop from the later V9–V20 lag-operator object and kills several attractive explanations, including the old phase-addressed memory demonstration under a missing null.

### Era 2 — maximal geometry story

V2 and V4 contain the maximal physical interpretation: dendrites as Takens unfoldings, soma as recurrence geometry, AIS as Moiré interferometer/grating, and morphology as the learning substrate.

These repos remain useful **idea mines**. They are not promoted to verified ancestors merely because later work retained words such as geometry, delay, phase or AIS. The pass deliberately contains **no V2 → V4 edge**: version numbering is not lineage evidence.

### Era 3 — operator and signal-processing turn

V5 is a major transition. It introduces the bilinear cross-time chirality readout

`L = Im(z(t) * conj(z(t-lag)))`

and explicitly recognizes the Wiener–Khinchin ceiling: linear/second-order delay-space magnitude cannot carry temporal direction.

V8 then provides a useful negative result of its own: orthogonalizing read templates with a frame potential makes them diverse but does not make them cover the data.

V9 is a clean correction. It moves directed structure into the skew half of lag covariance,

`A_tau = (C_tau - C_tau^T)/2`,

and derives rotation planes/eigen-islands rather than hand-assigning the directed edges used in V5.

V10 puts the same operator on a live stream and adds a predict/correct dead-reckoning loop. V20 is not treated as a new discovery; its own README correctly calls it a **recomposition** of previously earned mechanisms and negative results.

### Era 4 — external falsification and conceptual reset

V22 collides the abstraction with an external morphology target. The initially impressive graph/modal result largely disappears under the common-synapse control: ordinary area/path geometry performs at least as well. That null is genealogically important because it removes pressure to rescue the feature set.

V23 then states a much narrower object:

`geometry constrains coupling + local mechanisms carry state + events read/update state + receivers determine visibility`.

It explicitly does **not** claim a positive result yet.

V24, via a different direct edge from V21, removes the thermostat and turns the origin anomaly into an observability laboratory: addressable readout, active perturbation, nullspaces, rank and noise-limited identifiability.

### Era 5 — route-local causal search

V25 should not be drawn as “just the next GeometricNeuron.” It is a branch into route-attached causal state:

`where × what changed × how long × temporal mode`.

The fixed resonator bank succeeds on-grid and fails off-grid; a local generate/compete/retain search over the pole partially repairs the failure. The negative F8 gate remains part of the object.

### What this pass changes in Genealogy itself

The atlas is now modular. The original cross-family 28-node scaffold remains the foundation pass. The Geometric ladder lives in `data/passes/geometric-ladder.json` and is merged at load time.

That matters scientifically: a later archaeology pass can revise or supersede a relationship without silently rewriting the historical pass that proposed it.

The HTML now exposes:
- **Timeline** — nodes grouped by scientific era rather than filename/version order.
- **Corrections** — explicit `corrects` edges and killed/narrowed claims.
- **Pass filter** — see only one archaeology dig.
- **Edge filter** — isolate corrections, extractions, convergence, etc.
- **1-hop focus** — inspect the evidence neighborhood around a selected repo.
- **coverage meter** — keeps the difference between 400 inventoried repos and interpreted repos visible.

## Archaeology queue

Next priority is still not “newest first.” Inspect:

1. the Splat/Slapstack/TinyAvatar family and its transition into WorldModel;
2. the Clockfield cluster (`BirthOfClockfield`, `ClockfieldHierarchy`, `ClockfieldUnified`, `ClockfieldAsUniversalOperator`, collapse/ribbons/dimensionality) for repeated rediscoveries and dead branches;
3. the old PKAS / Deerskin / phase-keyed storage line because later GA/routing ideas may have appeared there much earlier;
4. the EEG / Takens / Koopman / metastability tools, separating publishable instrumentation from speculative interpretation;
5. the GAx / ThirdWay / TransformerStudy cluster with commit-level dates to distinguish direct inheritance from convergent rediscovery;
6. practical islands (audio/video, PDF/text, trading/stock, visualizers) to locate forgotten software that may be more useful than the grand-theory repos.

## Atlas status

The public census contains 400 public non-fork repositories. The curated atlas remains deliberately incomplete. A missing genealogy edge means **not established yet**, never “unrelated.”

The static explorer uses deterministic layouts rather than a force simulation. This is a research choice: the purpose is to inspect evidence, eras and corrections, not to produce an impressive graph-shaped cloud.

The public census is generated separately by `scripts/refresh_repos.py`. In environments without outbound DNS the script fails without overwriting existing data; GitHub Actions is the canonical refresh environment.
