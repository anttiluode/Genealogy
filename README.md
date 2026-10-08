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

## 2026-10-08 — Q-word: Möbius actions versus predictive belief

The [Möbius/Q-word transfer pass](data/passes/mobius-qword-transfer.json) adds
[Q-word](https://github.com/anttiluode/Q-word) to the wall and connects it to
[MovingTarget2's Möbius addendum](https://github.com/anttiluode/MovingTarget2/blob/main/MOBIUS.md). The exact first-harmonic
read family composes into a three-parameter group element per oscillator group;
in MovingTarget2's controlled twenty-seed protocol an 18-number action odometer
undoes 32 reads to near numerical precision without reading oscillator phases.
Cross-ratios are left invariant, but higher harmonic forcing changes them and
unknown interleaved drift defeats one-shot inversion.

Q-word independently tests **classical** oscillator worlds with a fixed binary
observation port and held-out hidden constellations. Its correct-law classical
particle filter (same observations, more prior dynamics knowledge) beats the
qubit-inspired recurrence on exact Möbius / shape-changing harmonic / hidden-drift
worlds: respectively **0.6751 / 0.6740 / 0.6809 versus 0.6824 / 0.6816 /
0.6892** NLL. Three seeds and short, unequal-compute training make this an
exploratory limit, not an architecture win. The Evidence and Questions views
retain the negative result and the next observability/learned-model tests.

## 2026-10-08 — MovingTarget2 and AnttisBrain2: memory across changing representations

The [memory-worlds pass](data/passes/moving-target-memory-worlds.json) adds
[MovingTarget2](https://github.com/anttiluode/MovingTarget2) and connects it to the
existing MovingProblem, VMN, VMNClaude and
[AnttisBrain2](https://github.com/anttiluode/AnttisBrain2) entries.
AnttisBrain2 is explicitly credited as the geometric origin of the later
[rooms, reflections and moons memory map](https://github.com/anttiluode/MovingTarget2/blob/main/docs/memory-worlds-and-languages.md).

The measured result is bounded: 96 oscillator phases move by a median 0.630
radians RMS while a frozen 12-number code predicts unseen weak responses at
1.83% normalized error. Stronger pings and later interactions expose information
that the small code omits. The Evidence view records both the successful
weak-response code and its stronger-query/read-update boundary.

Human pattern completion and partially shared multilingual LLM computation
motivate new retrieval tests. The proposed brain/LLM architecture is documented
as a research direction; the renderer and oscillator experiment do not establish
one universal tensor, an infinite recoverable past or an implemented LLM memory.

## 2026-10-07 — OpusPing: sender feature, receiver state, persistent write

The [synaptic-write pass](data/passes/state-conditioned-synaptic-write.json) adds
[OpusPing](https://github.com/anttiluode/OpusPing) to the wall, repository census
and Evidence view. It connects the explicitly named VMNClaude/Vision context to
the earlier FridayRepo and The_Ping_And_The_Listener mechanism by conceptual
convergence, without asserting code inheritance.

Five sender spikes keep their timing and count. The model represents the
sender feature as a **1.3x release factor**, then routes it through AMPA/NMDA
current, receiver voltage, calcium and a stored synaptic weight. A standard
probe 800 ms after the burst window changes by more than 5% and three standard
errors in at least one receiver state at five of six thresholds. Receiver state
conditions the size: at the 6x threshold the broad-minus-narrow probe contrast
is -10.4% when depolarized and -26.2% when hyperpolarized. This makes the
temporary-feature-to-persistent-write question concrete.

**A receipt correction matters.** The +56.6% depolarized contrast at the 2x
threshold is relative to the narrow condition. Final weights are 0.122 narrow
and 0.692 broad, both below the initial 1. Broad input therefore leaves less
depression; the run does not demonstrate net potentiation in that state. The
relative contrast does reverse sign across receiver states at one of six
thresholds. The registered lasting/immediate ratio is a weaker result because
its denominator can be small and already includes plasticity.

The [evidence ledger](data/evidence.json) separates the conditional delayed
response from those interpretation limits. The [open question](data/questions.json)
records plasticity-off, first-spike and calibrated-rate controls. Actual spike
waveforms, presynaptic calcium-to-release dynamics and ephaptic coupling are
outside this model; inhibition acts during induction, rather than restoring a
previous weight after a read.

The established ingredients are consistent with
[Shu et al.'s presynaptic voltage/spike-shape effect](https://www.nature.com/articles/nature04720)
and [calcium-threshold plasticity](https://pmc.ncbi.nlm.nih.gov/articles/PMC3309784/).
OpusPing supplies a specific toy composition of these ingredients, not a
replication of either paper or evidence for a waveform-borne world model.

## 2026-10-07 — VMN, VMNClaude and Vision: query, damage, restore

The [vortex/query/restore pass](data/passes/vortex-query-restore.json) adds
[VMN](https://github.com/anttiluode/VMN),
[VMNClaude](https://github.com/anttiluode/VMNClaude) and
[Vision](https://github.com/anttiluode/Vision) to the curated wall.
[Kompressori](https://github.com/anttiluode/Kompressori) was already present;
the new pass reuses that node as the upstream response-operator bridge rather
than duplicating it.

The useful common object is a **state-dependent response operator**. VMN's
geometry gate shows that a six-number state code can regenerate unseen
response changes far better than the tested fixed matrix dictionary, while the
stronger nonlinear-memory advantage fails. Its single-bank ping experiment
then makes the interface concrete: a useful read perturbs the phase memory, and
a sign-reversed counterpulse can preserve repeated reads. The restricted
four-channel listener still fails, and the trained listener is much larger than
the oscillator state.

VMNClaude independently develops the vortex/oscillator mathematics, noisy path
integration and ping-query interface. The uncoupled oscillator bank is the
important survivor; vortex coupling repeatedly fails to earn a role, the
proposed left/right theta-sweep cancellation story is killed, and exact undo
requires pre-query state. Vision carries the surviving read/write trade-off
into a tuft-inspired toy model. Input-locked inhibition at a whole-cycle delay
cuts lasting query damage 6.7× without hurting the answer, but the literal
output-driven Martinotti-erases-the-read story fails. BAC firing and the
KV-cache comparison remain explicitly labelled visions.

## 2026-10-06 — Jalanjälki and Thingy: readable state, causal writes

The [language-workspace pass](data/passes/language-workspace-control.json) adds
[Jalanjälki](https://github.com/anttiluode/Jalanjalki) and
[Thingy](https://github.com/anttiluode/Thingy) to the wall and Evidence view.
[Note](https://github.com/anttiluode/Note) was already curated in the
[codebook-growth pass](data/passes/note-language-codebook.json); its existing
entry is reused and connected to the two new instruments.

Jalanjälki compares identical-token Qwen3-0.6B base/instruct states, then tests
a post-training direction at the assistant boundary. Run 3's policy-score
dose slope is 1.726 per sigma versus 0.519 for a norm-matched random direction.
The earlier regex-based refusal AUC headline is withdrawn, exact J-lens words
remain unstable, and blind full-answer labels are still open.

Thingy's trained 1,813-parameter controller solves 1,260 fresh relation tasks.
Deleting a ping leaves 51/900 multi-hop answers correct; replay and
codebook-plus-residue restoration each recover 900/900. Text and latent
recurrence match its intact accuracy. The grammar, memory split and write rule
are engineered, so the result establishes editable causal computation in this
small task family. The new edges record conceptual convergence with Note and
ReadWrite; they do not assert code inheritance or tested concept consolidation.

## 2026-10-05 — temporal lenses, BrainLoops and Tupsu

The [temporal-control pass](data/passes/temporal-lenses-brainloops-tupsu.json)
adds [BrainLoops](https://github.com/anttiluode/BrainLoops) and
[Tupsu](https://github.com/anttiluode/Tupsu) to the curated wall and links them
to the existing [MultipleTemporalLenses pass](data/passes/multiple-temporal-lenses.json).
All three were already present in the raw repository census; MultipleTemporalLenses
already had a reviewed node, so it is reused rather than duplicated.

The comparison keeps their tests distinct. MultipleTemporalLenses stores useful
history, but its proposed query-softmax lens routing misses the frozen controls.
Tupsu's burst-driven cuts keep more bindings together yet lose far recall to
matched fixed chunks on all three seeds of the boundary-only run. BrainLoops'
canonical LEMON receipt reaches `PASS_LINEAR` for transitions in 22 held-out
people; state return passes the stronger phase control in both EC and EO. That
result neither measures inhibitory feedback nor establishes a seizure-prevention
function. The [Evidence view](data/evidence.json) retains each measured contrast.

A cross-repository correction narrows the MultipleTemporalLenses Gate 3 story:
the [BrainLoops task audit](https://github.com/anttiluode/BrainLoops/blob/main/docs/interpretation/2026-10-05-resonance-valves.md#related-memory-test-correction)
finds that Gate 3 discards candidate roles, collapsing opposite-label cases
onto the same observable input. Its expected 50% ceiling makes that gate
incapable of testing the intended later-context reinterpretation claim. The
other lens gates keep their recorded verdicts.

## 2026-10-02 — ChessFlyStatePings and InsideTheWave

The updated [ChessFly pass](data/passes/chessfly-state-pings.json) records the same-present history assay: opposite cue histories receive identical present inputs and one identical delayed ping. Responses differ, but continuation targeting fails its declared gate: 13/24 policy pairings (54.2%), 68.2% matched-control percentile and negative average native alignment. The first zero-ping receipt and the separately recorded source-timing correction remain visible. A structured record in the Evidence view keeps this mixed result distinct from lineage confidence.

The new [InsideTheWave pass](data/passes/inside-the-wave.json) adds the uploaded speculative working paper and its documented connection to ChessFly. Delay-as-phase, coherent interference and query-order examples are conditional mathematical models. The classical delayed-observation counterexample, extra assumptions behind a Born-shaped channel rule, and absence of a biological, consciousness or fundamental-physics result are part of the entry. The graph records the paper's use of earlier ChessFly results and Gate 4's explicit observer-replacement inspiration.

## Four layers

Genealogy now treats research memory as four distinct layers:

```text
inventory -> interpretation -> empirical evidence -> unresolved questions
```

**Inventory** says what repositories exist. **Interpretation** says how reviewed repositories relate and what mechanism survived. **Empirical evidence** says what experiment was actually run and what its result supports, contradicts, mixes, or leaves inconclusive. **Unresolved questions** say what competing explanations remain compatible with the audited evidence and what observation would separate them.

These layers deliberately do not collapse into one score.

### AInstein inside the transformer — Temporal Sihti and peripheral latent futures

Adds **AinsteinInsideTransformerResidualStream** as the point where the recent residue/operator line enters an actual frozen causal transformer. One current residual state is treated as a persistent present register; several bounded latent futures can fork from that common parent, leave provenance-stamped departure residues, and disappear. Selected residues may then interact nonlinearly and compile into a temporary residual/operator intervention before the main stream resumes.

The pass is deliberately hostile to its own metaphor. A vector merely leaving the span of its two branches is not evidence of invention. The pre-registered attackers include branch-only and convex/linear composition, provenance erasure or swapping, matched nonlinear post-concatenation, matched serial chain-of-thought, and matched textual branch search. If ordinary extra-token reasoning wins repeatedly at equal or lower compute, the peripheral-field architecture is to be dropped.

This also creates a strong new bridge to **CabbageFarmSihti**. Its shuffled-parent panel is the visual analogue of swapped provenance; its Gate-2 carrier swap is the cheap analogue of changing the transformer's composer family; and its Gaussian spectral null suggests a residual-stream null asking how much apparent collision structure is already predicted by low-order branch statistics. The image repo can therefore falsify control logic cheaply before the same mistake consumes an 8B-model GPU run.

### Observer in the loop — the measuring apparatus participates in the dynamics

Adds a cross-cutting survivor motif that had previously been scattered across observability, world-model, memory, operator-time and active-sensing passes. The recurring object is no longer only a changing hidden state; **the observer/query/instrument is itself stateful**.

The lineage is deliberately drawn as a motif rather than one invented ancestry chain. `MoireBrain` contributes scale-dependent visibility; `GeometricNeuronV24` and `ReadWrite` formalize bounded lenses and active intervention; `SighImageSuper` makes recoverability depend on the question; `PredictiveHKT` shows that a moving representation can impersonate world drift; `SplatWorld4` and `WhatToLookAt` actively choose observations; `AuditedEpistemicCache` records representation generation and provenance; `OperatorTime` makes reader state part of the effective operator; `AInstein` makes provenance load-bearing; and `AinsteinInsideTransformerResidualStream` now contributes a direct measurement failure.

Gate 0.7d is encoded as empirical evidence rather than a metaphor. Reversing the legacy three-row batch gives exactly zero numerical drift, while adding unrelated longer candidates changes the padded BF16 execution geometry enough to flip A/B first-action route conclusions; the longer trajectory remains semantically stable under the same attacker. The current fine-grained temporal claim is therefore suspended. The practical survivor is stricter: **a reusable belief needs a receipt for the observer under which it was measured**—query/intervention, viewpoint, provenance, representation generation and instrument context can all affect validity.

### AdaptiveObserverCache — persistent observer state becomes a transformer control loop

**AdaptiveObserverCache** now has a corrected first-ask distance result rather than the earlier re-ask confound. The previous visible-filler sweep is kept as a useful control: because its anchor already contained Qwen's closed valve answer and then asked the same question again, readable filler changed the conversational landscape and could not isolate positional age.

The corrected harness anchors **system + sources only** (93 cache tokens), withholds the 27-token first-question suffix, and advances distance with unreadable masked spacer rows. At distance 0, `m=-1` genuinely flips the complete candidate winner to sensor (**A−B summed margin −0.28697**) and the matched `valve`/`sensor` decision token to **−0.75**. After exactly **+256** masked positions, neutral is essentially unchanged (**+11.5491 vs +11.4495** A−B), so the earlier large neutral shift came from readable trajectory rather than masked positional age. Yet the observer still flips the local decision more strongly toward sensor (**token gap −1.75**) while the complete sensor sentence loses (**A−B +0.52131**). The current boundary is therefore precise: **local decision control survives while continuation control fails on this prompt.**

The next discriminator is now smaller than the old distance sweep: score the +256 B continuation with the observer **tonic throughout**, **phasic through the sensor decision then off**, and **neutral throughout with B forced**. If phasic release restores the tail, AOC has found a real frozen-model reason to pulse an intervention instead of steering every downstream token. If neutral forced-B is equally weak, ordinary long-distance continuation/copying is the better explanation.

### EATON — transient handoff as an explicit gating demonstration

**EATON** extracts that timing idea into a tiny resident-state machine: an addressed operator writes context, crosses an early boundary, then either releases before the payload computation or remains tonically active. The frozen v0 receipt is mechanically clean—early accuracy is **1.000** in all arms; final accuracy is **1.000 transient**, **0.500 tonic**, **0.501953125 reset**, with **64/64** seed wins against each attacker and matched event/state invariants.

But this is deliberately cataloged as a **constructed gating demonstration, not a discovery**. The tonic failure is derivable directly from the chosen coefficients: during the payload tick the always-on writer gives the new payload a larger term than retained context, so resident memory takes the payload sign and the balanced task collapses to chance. The overwrite problem also has classical input-gating antecedents such as LSTM-style memory protection. EATON therefore earns a clean harness and a useful vocabulary—event → transient operator → resident residue → handoff—but not a claim that phasic control is generally superior. The non-hand-designed test remains AOC/Qwen.

Genealogically, EATON sits where `SimpleNeuron`/`NSSN2` (rich resident state plus small travelling events), `FrequencyAddressedNonlinearModalCell` (addressed access to richer receiver dynamics), `OperatorTime` (history-conditioned effective operators), `ActiveVectorNN` (resident state versus sparse events), and `AdaptiveObserverCache` (persistent intent changing a frozen model's current read) meet. `AnotherOddThing` and `EvoX` remain adjacent rather than direct ancestors: they ask how to choose or search interventions/procedures, whereas EATON v0 only isolates the lifetime of an already-selected operator.

### Probe-defined operator coordinates — from neutral pings to gauge-aware tomography

Three September 23 repositories now join an older system-identification thread. **HeadAsResonator** had already provided a concrete calibration case: known speech plus observed electrode voltage identifies an approximate physical transfer function, which can then be inverted without turning the artifact into neural speech decoding. **ReadWrite** later made the more general observability point that a known state-dependent intervention can expose a hidden distinction that passive reading misses.

**SilentPing** joins that probe side to the resident-state line. In two deliberately constructed substrates, the same neutral ping carries no item label of its own, yet the response becomes item-decodable because resident state changes the operator the ping crosses. Reset returns decoding to chance, and the strongest control is a cross-label state transplant: moving only the resident state makes the ping report the donor item. The claim remains narrow. The mechanisms are known-answer constructions, parameters were tuned, and “silent” depends on the observer and traffic: the cable leaks to a variance decoder and background drive becomes a cloud of weak incoherent pings.

**PingToWord** provides a known-answer transfer calibration with an older engineering language. Identical source families driven through a moving vocal-tract-style resonator trajectory produce four synthetic words; the recovered filter trajectory classifies the word perfectly even when the source is replaced by whisper noise or a much higher pitch. Destroying order collapses the reverse-trajectory `we`/`you` pair to chance. This is classical source-filter/LPC territory, not a novelty claim. Its useful bridge is identifiability: endpoint-only chains admit order/gain ambiguities and a nonlinearity can hide an upstream stage, while logged residuals recover the actual intermediate trajectory. A residual-energy word leak remains as an explicit gain-gauge boundary.

**ResidentOperatorTomography** asks the harder question exposed by that calibration: when are two different-looking internal trajectories actually different computations? Residual logging plus local Jacobian probes is not enough unless the observer declares the allowed **gauge**. Under arbitrary invertible per-interface reparameterization, raw Jacobians, stage eigenvalues and singular values can change even though the computation is unchanged; in the tested d=8 chain only a deliberately coarse rank/nonlinearity descriptor survives the full gauge while still separating a genuinely different same-endpoint nonlinear factorization. Residual/shared-state architecture then shrinks the admissible gauge, restoring richer invariants such as per-stage eigenvalues. The result is still a toy with supplied stage boundaries and known stage families, but it gives the wall a stricter definition: a computation coordinate is a response-equivalence class **modulo representation changes the observer is allowed not to know**.

Genealogically this is a convergence, not a new invented ancestry chain: `HeadAsResonator` contributes measured transfer identification; `ReadWrite` contributes intervention-conditioned observability; `OperatorTime` and `EATON` contribute resident/state-conditioned operator language; `SilentPing` supplies the fixed-probe/transplant assay; `PingToWord` supplies a temporal operator-trajectory calibration; and `ResidentOperatorTomography` supplies the gauge-invariance attacker. The next serious handoff is a learned system or real residual stream where nobody chose the operator classes or coefficients to make the answer easy.

## Documentary confidence and empirical evidence

**Lineage / interpretation confidence** asks whether the corpus supports an ancestry edge or a curated reading of a repository. An explicit README statement can therefore justify a high-confidence inheritance edge even when the scientific claim itself is still weak, mixed, or untested.

**Empirical evidence** asks a different question: what experiment was run, on what units, with which controls, what was measured, what replicated, what failed, and what limitations remain?

`data/evidence.json` stores those evidence objects without collapsing them into a universal score. Evidence records may be `supports`, `contradicts`, `mixed`, or `inconclusive`. Missing evidence records mean only that the archaeology layer has not encoded the experiment yet; they do not imply that the source repository has no experiments.

The ledger deliberately mixes positive, mixed, null and confounded results. Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, `WhatToLookAt`, `AdaptiveObserverCache`, `EATON`, `SilentPing`, `PingToWord`, and `ResidentOperatorTomography`.

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

The later site gates turn that boundary into explicit causal controls. Gate 1 keeps a coarse parent, uses its local frame to organize fresh fine-scale noise, and compares correct-parent conditioning with a shuffled-parent / wrong-address panel. Gate 2 then exposes phase-warp banding as a carrier artifact and attacks the carrier separately by changing frame smoothing and sine / multi-sine / phase-noise families. The surviving question is no longer whether a striking image appears, but whether the **parent-conditioned relation survives wrong-address and carrier-family attacks**. The genealogy records `CabbageFarm → CabbageFarmSihti`, `Sihti2 → CabbageFarmSihti`, and now a direct `Sihti → CabbageFarmSihti` convergence for the residue-regrowth gates.

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

### LittleWorld and Perinto — what a small message can carry

The [marked-events-cultural-inheritance pass](data/passes/marked-events-cultural-inheritance.json) connects two separate experiments without treating them as one implementation. [LittleWorld](https://github.com/anttiluode/LittleWorld) supplies a three-coordinate sender mark and matching receiver transform, then holds the event budget fixed while removing marks, yoking them to another world, scrambling their timing, or resetting receiver memory. Its frozen 12-seed gate passes all four comparisons on blind hidden-world prediction. The supplied encoder and decoder limit the result to a constructed communication mechanism.

[Perinto](https://github.com/anttiluode/Perinto) moves the question across generations: what happens when elders can pass laws or isolated facts through only twelve sentences? Its frozen v1 with evolving trust fails all four predictions. A later post-hoc v1.1, precommitted on six fresh worlds with trust fixed at one, finds a law-based ratchet: twelve law-bearing sentences yield 21.0 fitness versus 13.8 for twelve fact-only sentences and 16.3 for forty fact-only sentences. The advantage for selected exceptions remains unsupported. These two repositories meet at a question about receiver state and compressed transmission; neither establishes learned spike coding, spontaneous language, or direct code ancestry.

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
