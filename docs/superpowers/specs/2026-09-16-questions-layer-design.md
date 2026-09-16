# Unresolved Questions Layer Design

## Purpose

Genealogy already separates repository lineage, experimental claim outcomes, and motif-level evidence relations. The next layer should represent **scientific uncertainty that is still actionable**: what competing explanations remain alive, what evidence bears on them, what discriminator is missing, and what experiment would most directly separate them.

The Questions layer is not a score, forecast, or automatic truth engine. It is an auditable research-planning object built from the evidence ledger.

## Core object

Add `data/questions.json` as an array of explicit question records. Each record contains:

- `id`: stable question identifier.
- `title`: concise unresolved contrast.
- `state`: `open`, `partially-resolved`, or `resolved`.
- `motifs`: motif IDs the question bears on.
- `evidence`: evidence-record IDs that motivate the question.
- `competing_explanations`: two or more live explanations stated neutrally.
- `known`: short statements already established by the encoded evidence.
- `missing_discriminator`: the specific observation that would separate the live explanations.
- `candidate_experiment`: a concrete, cheap next experiment with `design`, `outcomes`, and `cost` fields.
- `resolution_evidence`: evidence IDs that resolve the question; required only when `state == resolved` and forbidden otherwise.
- `notes`: optional limitations or caveats.

No probability, score, ranking, or winner field is allowed.

## Initial seeded questions

The first release should encode only contrasts already justified by the current evidence ledger:

1. **Active intervention — benefit versus probing cost / hidden-cause density.** GeometricNeuronV24, ReadWrite and LentoOrava support active probing/intervention under different synthetic settings. The missing discriminator is whether the advantage survives explicit probe cost and denser/non-sparse hidden causes.
2. **Late relevance — architectural factorization versus training-quality confound.** NewMachine supplies a clean overlapping-constraint construction; FusionMachine shows a much larger readiness gap but with a baseline training-quality confound. The next experiment should equalize training fit before comparing switch readiness.
3. **Bounded observation — active addressing versus grid-specific structure.** GeometricNeuronV24 supports active address selection while ReadWrite kills a stronger coprime-grid advantage against a best-single-grid attacker. The unresolved question is what part of the gain comes from active/adaptive placement versus a particular multiscale/grid code.
4. **Structure as computation — topological relation versus functional consequence.** GrowingAnttisNeuron and Operaattori both support structure-to-operator ideas, but on different endpoints. The missing test is whether a controlled structural change predicts a downstream task/response change better than coarse graph/spectrum summaries.
5. **Persistent state — communication savings versus task-dependent control.** ActiveVectorNN supports sparse synchronization of fixed maintained state; NewMachine supports separate repair/publication control in overlapping constraints. The unresolved contrast is whether the richer control still earns its complexity on vector tasks with matched communication budgets.

## UI

Add a top-level `Questions` tab between Evidence and Survivors. Keep the implementation additive in a dedicated `assets/questions.js` and `assets/questions.css`, following the existing evidence-layer pattern instead of expanding `app.js` substantially.

The view renders one card per question with:

- state and linked motifs;
- known evidence and source repositories;
- competing explanations;
- the unresolved discriminator;
- the candidate experiment;
- outcome interpretation written as conditional observations, not predictions.

Cards link back to the relevant repository nodes and evidence records by filtering/opening existing views where practical.

## Validation

`validate_data.py` loads and validates `questions.json`.

Validation rules:

- unique non-empty IDs;
- known `state` enum;
- every motif ID exists;
- every evidence and resolution-evidence ID exists;
- at least two competing explanations;
- non-empty `known`, `missing_discriminator`, and candidate-experiment `design`;
- candidate experiment contains at least two explicit possible outcomes;
- `resolved` requires at least one `resolution_evidence` ID;
- non-resolved questions must not contain resolution evidence;
- no numeric score/probability/winner keys.

Client-side absence of questions should degrade gracefully and must not break the rest of the atlas.

## Relationship to Queue

Keep Queue unchanged. Queue answers **which existing unreviewed repository should be archaeologically inspected next?** Questions answers **which scientific uncertainty deserves a new discriminating experiment?** They are intentionally separate workflows.

## Testing

Use TDD. Add failing tests before production changes for schema validation, initial question coverage, required UI hooks, and the invariant that unresolved questions cannot masquerade as resolved observations. CI must run the new JavaScript syntax check before merge.
