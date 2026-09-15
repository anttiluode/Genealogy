# Genealogy

**A research archaeology of ~400 repositories: what descended from what, what failed, what survived, and what accidentally became useful.**

Live atlas: **https://anttiluode.github.io/Genealogy/**

The important rule is that this repository keeps two different objects separate:

```text
repository census                     curated genealogy
what exists                           what the evidence supports
complete / mostly mechanical          deliberately incomplete
names and metadata                    inspected claims and lineage
no ancestry implied                   confidence-labelled edges
```

A missing genealogy edge means **not established yet**, not “unrelated.” Repository names are useful search hints and nothing more.

## What the page shows

- **Genealogy** — reviewed repositories arranged by research family. Click a node to see its narrow claim, what survived, what died or was narrowed, confidence, and evidence.
- **Census** — the full public repository inventory once the refresh workflow has run. Reviewed repos are distinguished from unread inventory.
- **Survivors** — mechanisms that reappear across otherwise different metaphors: bounded observation, persistent state, structure-as-operator, active intervention, low-rank operator change, sparse causal publication, and more.
- **Archaeology queue** — transparent heuristics for deciding which unreviewed repositories deserve inspection next.

The graph is intentionally not a force-directed 400-node hairball. The curated graph stays sparse enough that every arrow should be defensible.

## Evidence rules

Edges live in `data/edges.json` and use six meanings:

| edge | meaning |
|---|---|
| `inherits` | a mechanism/idea is explicitly carried forward |
| `forks` | a deliberate descendant/new repo from a predecessor |
| `rediscovery` | substantially the same mechanism reached by another route |
| `corrects` | a later repo explicitly narrows or kills an earlier interpretation |
| `extracts` | a smaller practical/scientific mechanism was pulled out of a larger project |
| `converges` | formerly separate lineages are intentionally combined |

An edge needs repository evidence: an explicit lineage statement, result note, code descent, commit history, or other inspected material. Name similarity alone never earns an edge.

Confidence is part of the record. `high` means the relationship is explicit or directly evidenced; `medium` means there is real support but more commit-level archaeology is warranted; `low` should be rare and must still have evidence.

## Negative results are ancestors too

This atlas keeps failed experiments because many of the strongest later mechanisms exist **because** a seductive earlier story failed. `Clockfield`, `PhaseStigmergy`, `FunctionalArbors`, `GeometricNeuronV24`, `Kompressori`, `AnttisNeuron`, and others are useful partly because they record what did *not* survive a stronger control.

The genealogy therefore tracks both:

```text
idea -> success -> extraction
idea -> falsifier -> correction -> better question
```

## Data files

- `data/repos.json` — repository census. Generated mechanically; no genealogy claims.
- `data/nodes.json` — reviewed repositories and their current archaeological interpretation.
- `data/edges.json` — evidence-backed relationships.
- `data/motifs.json` — recurring cross-family mechanisms.
- `RESEARCH_LOG.md` — human research notes, corrections, and next dig sites.

The design and implementation plan are frozen under `docs/superpowers/`.

## Run locally

The site has no build step and no frontend dependencies.

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

Validate the atlas and run tests:

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
node --check assets/app.js
```

## Refresh the repository census

```bash
python scripts/refresh_repos.py anttiluode
```

The refresh uses GitHub's public API, paginates 100 repositories at a time, preserves existing review-state annotations, writes atomically, and refuses to replace a good census with an empty response.

`.github/workflows/refresh-repos.yml` refreshes on the first relevant `main` push, on demand, and weekly. The existing `static.yml` deploys the root directly to GitHub Pages.

## Adding a reviewed repository

1. Read the repository itself. Prefer README/result ledgers, explicit lineage notes, and relevant commits over retrospective memory.
2. Add/update its record in `data/nodes.json` with a **narrow** `claim`, plus `survived`, `killed`, `usefulness`, `confidence`, `evidence`, and mechanism `tags`.
3. Add only edges you can defend.
4. Add the repo to a motif only when the same mechanism genuinely recurs; do not group by vocabulary alone.
5. Record surprising reversals or rediscoveries in `RESEARCH_LOG.md`.
6. Run the validator and tests.

The goal is not to make every old idea look prescient. The goal is to discover which small mechanisms actually survived repeated attempts to kill them—and which useful things were abandoned when the next repo began.
