# Genealogy

Evidence-backed archaeology of Antti Luode's research repositories.

The central premise is that hundreds of repositories are not hundreds of independent ideas. The project separates raw repository inventory from curated scientific interpretation, then records explicit inheritance, corrections, rediscoveries, convergences, extracted mechanisms, and the empirical evidence attached to individual claims.

## Live atlas

https://anttiluode.github.io/Genealogy/

The static atlas includes:

- the complete repository census,
- a curated genealogy graph,
- modular archaeology passes,
- scientific-era Timeline and Corrections views,
- a first-class Empirical Evidence view,
- cross-repository motif-evidence summaries,
- per-repository evidence ledgers in the genealogy detail panel,
- survivor motifs and archaeology queue,
- family/status/pass/edge filters,
- one-hop lineage focus,
- dependency-free SVG wheel zoom, drag pan, `− / + / Fit` controls, and zoom readout.

## Two kinds of confidence

Genealogy keeps documentary and empirical questions separate.

**Lineage / interpretation confidence** asks whether the corpus supports an ancestry edge or a curated reading of a repository. An explicit README statement can therefore justify a high-confidence inheritance edge even when the scientific claim itself is still weak, mixed, or untested.

**Empirical evidence** asks a different question: what experiment was run, on what units, with which controls, what was measured, what replicated, what failed, and what limitations remain?

`data/evidence.json` stores those evidence objects without collapsing them into a universal score. Evidence records may be `supports`, `contradicts`, `mixed`, or `inconclusive`. Missing evidence records mean only that the archaeology layer has not encoded the experiment yet; they do not imply that the source repository has no experiments.

The ledger deliberately mixes positive, mixed, null and confounded results. Current audited examples include:

- `GeometricNeuronV24` active sensing and the soma-noise observability boundary,
- `ReadWrite` state-dependent probing plus the failed coprime-vs-best-single-grid claim,
- `LentoOrava` PulseTriage and scalar-only repair localization,
- `GrowingAnttisNeuron` matched developmental controls,
- `Operaattori` cross-cell nonlinear closure,
- `ActiveVectorNN` sparse state synchronization,
- `NewMachine` factorized repair/publication control,
- `WorldModel`'s preserved RGB-only geometry failure,
- `PhaseStigmergy`'s replicated morphology null,
- `FusionMachine`'s readiness result retained as inconclusive because training quality confounds attribution.

## Motif evidence

An evidence record may name the specific survivor motif it bears on. The atlas validates that the repository actually belongs to that motif before accepting the link.

This lets the Evidence view distinguish:

```text
motif appears in several repositories
```

from:

```text
motif has supporting controlled evidence in several repositories
```

and from:

```text
the same motif also accumulated nulls, mixed results or confounds
```

Two supporting experiments inside one repository do not count as cross-repository support. The aggregation counts distinct repositories, not just record count.

## Current archaeology passes

### Foundation atlas

The first cross-family curated slice. It captures recurring mechanisms such as bounded observation, structural memory, operator compilation, active probing, persistent state, sparse publication, splat/world representation, and search/routing.

### GeometricNeuron ladder

Treats the numbered GeometricNeuron repositories as scientific eras instead of assuming version-number ancestry. Explicit corrections survive; unsupported numerical ladders do not become edges.

### Splat / WorldModel

Tracks layered Gabor tools, phase transport, persistent fields, sparse predictive belief, observer-resource attacks, shared operator worlds and active inverse sensing. This pass corrected the atlas's own earlier speculative `Splatworld2 → WorldModel` edge using WorldModel's explicit ancestry.

### Clockfield pruning

Separates four things that had become entangled in the Clockfield family:

1. executable toy field dynamics,
2. grand physical identifications,
3. later falsifiers/autopsies,
4. computational mechanisms that remain useful after the physics story is removed.

The pass adds nine reviewed repositories, including `BirthOfClockfield`, `SimpsonsUniverse`, `HorizonNet`, `OutoSynapsi`, and `ClockfieldUnified`. The strongest survivors are not the cosmological claims: they are the Beurling-lattice mathematical object isolated by the SimpsonsUniverse audit, HorizonNet's idleness/observer-horizon result, traffic-shaped body geometry in OutoSynapsi, and the narrow Physics Router extraction in ClockfieldUnified.

## Evidence rule

A genealogy edge means documentary evidence was found for that relationship. Similar names and version numbers are only discovery hints.

An empirical evidence record means a specific experimental result was audited and encoded separately. A supporting result is not the same thing as high lineage confidence, and a high-confidence lineage edge is not the same thing as a replicated scientific effect.

Negative results remain in the tree and in the evidence ledger. A failed interpretation often explains why a later mechanism exists, so deleting it would erase the actual genealogy.

## Data layout

```text
data/repos.json          complete census snapshot
data/nodes.json          foundation curated nodes
data/edges.json          foundation lineage/evidence-of-ancestry edges
data/motifs.json         foundation recurring mechanisms
data/evidence.json       structured empirical evidence records + motif links
data/passes/index.json   enabled archaeology passes
data/passes/*.json       separable reviewed passes
```

Passes stay modular so later archaeology can correct one family without rewriting the whole atlas. Empirical evidence stays separate so the same claim can accumulate support, nulls, contradictions, stronger controls, or replication over time.

## Validation

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
node --check assets/app.js
node --check assets/tools.js
node --check assets/evidence.js
node --check assets/zoom.js
```

GitHub Actions runs the same checks on pull requests and `main` pushes. The repository census refresh remains separate from interpretation changes.

## Rule

**Names are hints, not evidence. Negative results stay in the family tree. Documentary confidence and empirical support are different axes.**
