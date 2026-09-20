# Genealogy

Evidence-backed archaeology of Antti Luode's research repositories.

The central premise is that hundreds of repositories are not hundreds of independent ideas. The project separates raw repository inventory from curated scientific interpretation, then records explicit inheritance, corrections, rediscoveries, convergences, extracted mechanisms, empirical evidence, and the scientific questions that remain unresolved.

## Live atlas

https://anttiluode.github.io/Genealogy/

The static atlas includes:

- the complete repository census,
- a curated genealogy graph,
- modular archaeology passes,
- scientific-era Timeline and Corrections views,
- a first-class Empirical Evidence view,
- cross-repository motif-evidence summaries,
- a first-class Unresolved Questions view,
- per-repository evidence ledgers in the genealogy detail panel,
- survivor motifs and a separate archaeology queue,
- family/status/pass/edge filters,
- one-hop lineage focus,
- dependency-free SVG wheel zoom, drag pan, `− / + / Fit` controls, and zoom readout.

## Four layers

Genealogy now treats research memory as four distinct layers:

```text
inventory -> interpretation -> empirical evidence -> unresolved questions
```

**Inventory** says what repositories exist. **Interpretation** says how reviewed repositories relate and what mechanism survived. **Empirical evidence** says what experiment was actually run and what its result supports, contradicts, mixes, or leaves inconclusive. **Unresolved questions** say what competing explanations remain compatible with the audited evidence and what observation would separate them.

These layers deliberately do not collapse into one score.

## Documentary confidence and empirical evidence

**Lineage / interpretation confidence** asks whether the corpus supports an ancestry edge or a curated reading of a repository. An explicit README statement can therefore justify a high-confidence inheritance edge even when the scientific claim itself is still weak, mixed, or untested.

**Empirical evidence** asks a different question: what experiment was run, on what units, with which controls, what was measured, what replicated, what failed, and what limitations remain?

`data/evidence.json` stores those evidence objects without collapsing them into a universal score. Evidence records may be `supports`, `contradicts`, `mixed`, or `inconclusive`. Missing evidence records mean only that the archaeology layer has not encoded the experiment yet; they do not imply that the source repository has no experiments.

The ledger deliberately mixes positive, mixed, null and confounded results. Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, and `WhatToLookAt`.

## Motif evidence

An evidence record may name the specific survivor motif it bears on. The atlas validates that the repository actually belongs to that motif before accepting the link.

Claim outcome and motif relation are intentionally separate. `data/evidence.json` says what happened to the tested claim. `data/evidence_motif_relations.json` says whether that result **supports**, **limits**, or merely **documents** the broader motif. This matters because a contradicted claim can positively document the `negative-results` motif instead of being misread as evidence against it.

Two supporting experiments inside one repository do not count as cross-repository support. The aggregation counts distinct repositories, not just record count.

## Unresolved questions

`data/questions.json` turns the evidence ledger into explicit research-planning objects. Each question records:

- the motifs and evidence records that motivate it,
- at least two live competing explanations,
- what is already known,
- the missing discriminator,
- a concrete candidate experiment,
- at least two conditional outcomes describing how the interpretation would change.

Question state is `open`, `partially-resolved`, or `resolved`. A question cannot become `resolved` merely because someone edits its label: the validator requires a real `resolution_evidence` record. Conversely, unresolved questions are forbidden from carrying resolution evidence.

The initial questions cover active intervention under explicit probe cost/dense causes, late relevance after equalizing training fit, active addressing versus grid-specific measurement structure, structure-to-function beyond coarse graph summaries, and factorized persistent-state control at matched communication cost.

Questions are intentionally **not** probabilities, rankings, or predictions. Candidate experiments describe observations that would discriminate between explanations; they are not presented as results that have already happened.

## Questions versus archaeology queue

These are different workflows.

**Archaeology queue:** which existing, unreviewed repository should be inspected next?

**Questions:** which scientific uncertainty exposed by already-audited evidence deserves a new discriminating experiment?

The queue continues to prioritize old source material. The Questions layer plans future falsification work. Neither automatically ranks scientific importance.

## Current archaeology passes

### Foundation atlas

The first cross-family curated slice. It captures recurring mechanisms such as bounded observation, structural memory, operator compilation, active probing, persistent state, sparse publication, splat/world representation, and search/routing.

### GeometricNeuron ladder

Treats the numbered GeometricNeuron repositories as scientific eras instead of assuming version-number ancestry. Explicit corrections survive; unsupported numerical ladders do not become edges.

### Splat / WorldModel

Tracks layered Gabor tools, phase transport, persistent fields, sparse predictive belief, observer-resource attacks, shared operator worlds and active inverse sensing. This pass corrected the atlas's own earlier speculative `Splatworld2 → WorldModel` edge using WorldModel's explicit ancestry.

### Clockfield pruning

Separates executable toy dynamics, grand physical identifications, later falsifiers/autopsies, and computational mechanisms that remain useful after the physics story is removed. The strongest survivors are narrow mathematical/computational mechanisms rather than the discarded cosmological claims.

### Sigh residue fork — Sihti / SighImageFactorization

Tracks the explicit `SighImageSuper` fork into two different uses of the same telescoping residue identity. `Sihti` becomes a live sieve/instrument and tests where objects land under different purifiers on BSDS500. `SighImageFactorization` kills residue-space factorization as the source of objects, then follows the input/history-written operator through common-fate binding, relation authority, recoverable uncertainty, an identical-prefix observability boundary, genuinely predictive new observables, and environment-dependent cue meaning. The pass deliberately draws both descendants from Sigh rather than inventing peer ancestry between work developed in parallel.

### Sihti2 — noise writes a diffusion geometry

Adds **Sihti2** as the null-input / spectral-geometry continuation of Sihti. IID colour noise is no longer treated as merely something to denoise: it writes the local conductance graph through the same image-affinity rule, and the resulting lazy diffusion is measured as a reversible Markov process. The branch asks whether the boxy late states are metastable graph domains with reproducible scaling rather than "objects in noise."

The first experiment compares four matched controls: the signal writing its own graph, an independent IID draw writing the graph, the same conductance histogram shuffled over edges, and the blank spatial lattice. The measured objects are the small normalized-Laplacian spectrum, relaxation time, stationary-measure variance, weighted edge disagreement, stochastic heat trace and local spectral-dimension slope.

The correction is part of the node, not an afterthought: a visually coherent late state does **not** establish semantic objecthood, fractality, a renormalization-group fixed point or a Griffiths phase. Those stronger interpretations require finite-size and scaling evidence. The lineage edge is therefore narrow and explicit: `Sihti → Sihti2`, from "the operator decides what persists" to "what diffusion geometry did random data write?"

### CabbageFarmSihti — learn the law, not one stored world

Adds **CabbageFarmSihti** as a convergence between the old CabbageFarm coordinate-field ambition and the Sihti/Sihti2 operator/noise line. CabbageFarm asked whether a finite image could be encoded as a continuous coordinate-queryable world. The new branch changes the target: infer a stochastic transfer law from a finite reference, then apply that law to fresh coordinate-addressable noise so new territory comes from the law rather than from extrapolating one stored instance.

The v0 implementation begins with the strongest simple attacker rather than with a neural generator. It fits a 2-D spectral measure in a PCA colour basis and samples a globally defined random Fourier field. Separate crop requests with the same model/seed must agree exactly on overlap, making "arbitrarily large" a coordinate-consistency property rather than a giant bitmap. A Sihti-style Gaussian residue signature is recorded, but matching those linear second-order octave statistics does **not** count as extra Sihti evidence because the power spectrum already determines them for a stationary Gaussian process.

The live boundary is therefore sharp: phase-randomized / power-spectrum-matched synthesis must fail on measurable cross-octave spatial structure before a richer relation law such as `P(R_2d | R_d)` is earned. The genealogy records both inputs explicitly: `CabbageFarm → CabbageFarmSihti` for the continuous-world goal and `Sihti2 → CabbageFarmSihti` for the transfer-law/noise perspective.

### WhatToLookAt — learned relations become a sensing budget

Tracks the step from history-written relation state to an explicit physical-observation currency. Gate 0 establishes the oracle upper bound, Gate 1 learns a persistent common-fate relation before a rearranged future is undersampled, and Gate 2 lets local relation confidence allocate extra sensing only where correspondence is uncertain. The key question is no longer only what the operator groups, but **how many measurements that learned structure lets the system stop taking**.

### GeometricNeuron_V20 — recomposition also preserves the whorl

The V20 curation is already a reviewed node, but its source provenance is now explicit on the wall. In particular, `03_faces_of_A/generate/whorl_field.py` and `whorl_README.md` are preserved from `ArtificialCortex/the_whorl`. The atlas now draws that curation edge directly instead of leaving the spiral-field branch buried inside the larger ArtificialCortex node.

### SelfAndOtherObjectsInTime — event-owned time and continuing reference

Adds the current Gates 1–9 line: self/other role binding, event-relative phase, discovered boundaries, nested local clocks with writeback, consequence-based event admission, active causal probing, selective temporal precision, and online timing reallocation without resetting event identity. The pass deliberately connects back to FrequencyAddressedState-dependentOperatorComposition, FusionMachine, SighImageFactorization, AnotherOddThing, ReadWrite and the ArtificialCortex/whorl phase substrate while keeping the biological/consciousness claims out.

### Operator Time — resident history changes the operator available now

Adds **OperatorTime**. The pass makes explicit the synthesis that emerged from GAx, FrequencyAddressedState-dependentOperatorComposition, Sihti, WhatToLookAt, SelfAndOtherObjectsInTime and the ArtificialCortex/whorl substrate line: learned/substrate parameters may stay fixed while resident history changes the effective operator acting now. Gate 1 keeps the current probe identical and parameter drift at zero, yet recent transient history remains decodable from the current operator response (0.9924 versus chance for fixed/reset controls). Gate 2 then treats frozen text-like residue as a serial perturbation: matched sequences with identical symbol multisets and identical endpoints separate only when order is preserved (1.0000 versus ~0.50 for bag/shuffle/endpoint controls), while the same frozen sequence can still lead to a different final operator when the reader begins from a different resident state. Gate 3 then makes constructive residue synthesis the north star: two provenance-stamped residues that are individually insufficient can jointly expose a useful operator outside the branch-only linear span (1.0000 synthesis versus ~0.50 branch/average/provenance-erased controls; 0.0999 operator novelty residual). The interaction is deliberately hand-designed, so the next goal is discovered rather than scripted synthesis. Transformer/KV and biological parallels remain labeled as analogies rather than established equivalences.


### AInstein — constructive residue synthesis becomes a held-out discovery gate

Adds **AInstein** as the direct continuation of OperatorTime Gate 3. Instead of hand-writing one useful cross-term and merely proving that it can work, Gate 1 presents a small interaction grammar and selects the mechanism on validation pairs, then freezes it for A/B pairings never seen together. Across 32 worlds the ordered interaction is selected 32/32 times; held-out operator R² is 0.9781 and held-out operator-application R² is 0.9789, while branch-only, convex branch mixing and pair lookup remain near chance/zero. Erasing provenance drops operator R² to 0.2651, and the joint operator retains a 0.7457 relative component outside the branch-only span.

The pass also records an important negative/correction rather than hiding it: a transformer-style convex retrieval followed by a nonlinear post-mix stage reaches 0.9467 R². So AInstein is **not** evidence that transformer attention is trapped in interpolation.

Gate 2 then makes the AnotherOddThing / WhatToLookAt connection executable. Eight A residues and eight B residues create 64 legal collisions, but only three may be probed. Expected-information-gain selection reaches **0.9531** mean selected utility and **0.8999** oracle-pair hits versus **0.8460 / 0.1990** for matched random probing and **0.8041 / 0.0942** for greedy exploit-only probing. The most useful attacker is provenance misbinding: attaching the correct response library to the wrong pair addresses still produces a very sharp posterior (**0.247 bits**) while utility collapses to **0.4762**. The surviving rule is therefore stronger than "be confident": **confidence is not provenance**.

Gate 3 now removes one of those crutches. Instead of selecting a complete interaction from a menu, the system receives only coordinate address, multiplication and additive readout primitives and must grow six useful cross-residue programs. Under the same **12 nonlinear-node structural budget**, depth/order≤4 reaches **0.9986** held-out operator R², while depth/order≤3 reaches **0.6459** and depth/order≤2 reaches **0.3091**. Keeping the discovered branch-depth pattern but randomizing wiring gives **-0.0118**; globally shuffling the discovered addresses gives **-0.0030**. So unit count alone is not enough in this synthetic family: **how the interaction sites are wired and how deeply they compose is causal**.

This gate deliberately fences the biology. Aizenbud et al.'s morphology result is used only as an architectural provocation that geometry can matter beyond branch count. The numerical proximity between AInstein's earlier **0.7457 relative span residual** and the paper's **R²=0.74 dendritic-area correlation** is recorded as coincidence, not correspondence. The stronger genealogy links are to `DendriteAsIteratedFeedbackOperator` and `AnttisNeuron`, where structural depth/growth had already been treated as a computational resource under explicit controls.

Gate 4 then makes the older GAx connection executable. Eight historical operators are learned from noisy data and kept as separately stamped capabilities while a different current operator is learned. Noisy context reinstates the right historical transform with **0.9893** hit rate and **0.9784** old-task R²; averaging the cache reaches only **0.1191**, and erasing context drops to **-0.7551**. More importantly, simultaneous access to past and current transforms exposes a past→present relation operator at **0.9784 R²**. A wrong-era relation collapses to **-0.9917**, an oracle convex old/current blend to **-0.4726**, and a fresh 3-shot transfer fit reaches **0.4958**. So the new surviving object is not merely a remembered state but a **callable learned operator**, and present/past coexistence can define another operator: the relation between computational eras.

This is the closest AInstein has come to GAx's spectral-router idea: GAx preserves multiple computational modes so context can amplify the appropriate one; Gate 4 stores those modes explicitly as context-stamped operators that can be reused or compared. The live boundary now moves to trajectory-sensitive memory: can identical endpoints remain distinguishable because their histories, event roles or simulated/actual provenance differ?

## Evidence rule

A genealogy edge means documentary evidence was found for that relationship. Similar names and version numbers are only discovery hints.

An empirical evidence record means a specific experimental result was audited and encoded separately. A supporting result is not the same thing as high lineage confidence, and a high-confidence lineage edge is not the same thing as a replicated scientific effect.

Negative results remain in the tree and in the evidence ledger. A failed interpretation often explains why a later mechanism exists, so deleting it would erase the actual genealogy.

## Data layout

```text
data/repos.json                     complete census snapshot
data/nodes.json                     foundation curated nodes
data/edges.json                     foundation lineage/evidence-of-ancestry edges
data/motifs.json                    foundation recurring mechanisms
data/evidence.json                  structured empirical evidence records + motif links
data/evidence_motif_relations.json  supports / limits / documents relation to each tagged motif
data/questions.json                 unresolved contrasts + candidate discriminating experiments
data/passes/index.json              enabled archaeology passes
data/passes/*.json                  separable reviewed passes
```

## Validation

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
node --check assets/app.js
node --check assets/tools.js
node --check assets/evidence.js
node --check assets/questions.js
node --check assets/zoom.js
```

GitHub Actions runs the same checks on pull requests and `main` pushes. The repository census refresh remains separate from interpretation changes.

## Rule

**Names are hints, not evidence. Negative results stay in the family tree. Documentary confidence, claim outcome, motif relation, and unresolved question state are different axes.**
