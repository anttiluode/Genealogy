# Genealogy

**A research archaeology of 400 public repositories: what descended from what, what failed, what survived, and what accidentally became useful.**

Live atlas: **https://anttiluode.github.io/Genealogy/**

The important rule is that this repository keeps two different objects separate:

```text
repository census                     curated genealogy
what exists                           what the evidence supports
complete / mechanical                 deliberately incomplete
names and metadata                    inspected claims and lineage
no ancestry implied                   confidence-labelled edges
```

A missing genealogy edge means **not established yet**, not “unrelated.” Repository names and version numbers are useful search hints and nothing more.

## What the page shows

- **Genealogy** — evidence-backed relationships arranged by research family. Selection opens the narrow claim, what survived, what died, and upstream/downstream evidence. A 1-hop focus mode isolates the local ancestry trail.
- **Timeline** — reviewed repositories grouped by scientific era. This is specifically designed to expose cases where the object itself changed even though the version naming continued.
- **Corrections** — explicit `corrects` edges plus negative/ledger nodes and the claims they narrowed or killed.
- **Census** — the full public repository inventory. Reviewed repos are distinguished from unread inventory.
- **Survivors** — mechanisms that reappear across otherwise different metaphors.
- **Archaeology queue** — transparent heuristics for deciding which unreviewed repositories deserve inspection next.

The header shows archaeology coverage so the page cannot visually confuse “40 interpreted repos” with “400 repos understood.”

## Modular archaeology passes

The original cross-family scaffold remains in the base files:

- `data/nodes.json`
- `data/edges.json`
- `data/motifs.json`

Deeper digs live under:

```text
data/passes/
    index.json
    geometric-ladder.json
    clockfield.json          # future
    splats.json              # future
    ...
```

Each pass carries its own metadata, nodes, edges and optional motifs. The Python validator and browser loader merge enabled passes at runtime while preserving `pass_id`.

This is intentional scientific bookkeeping. If a later pass changes our interpretation, we can see **which archaeology pass proposed which relationship** instead of silently rewriting one monolithic history.

## Evidence rules

Edges use six meanings:

| edge | meaning |
|---|---|
| `inherits` | a mechanism/idea is explicitly carried forward |
| `forks` | a deliberate descendant/new repo from a predecessor |
| `rediscovery` | substantially the same mechanism reached by another route |
| `corrects` | a later repo explicitly narrows or kills an earlier interpretation |
| `extracts` | a smaller practical/scientific mechanism was pulled out of a larger project |
| `converges` | formerly separate lineages are intentionally combined |

An edge needs repository evidence: an explicit lineage statement, result note, code descent, commit history, or other inspected material. **Name similarity or version order alone never earns an edge.**

Confidence is part of the record. `high` means the relationship is explicit or directly evidenced; `medium` means there is real support but more commit-level archaeology is warranted; `low` should be rare and must still have evidence.

## Negative results are ancestors too

This atlas keeps failed experiments because many of the strongest later mechanisms exist **because** a seductive earlier story failed.

The genealogy tracks both:

```text
idea -> success -> extraction
idea -> falsifier -> correction -> better question
```

The Geometric-ladder pass makes this explicit: V8, V21 and V22 are not dead ends. They are selection events that remove mechanisms and force narrower descendants.

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

`.github/workflows/refresh-repos.yml` refreshes automatically and `static.yml` deploys the repository root directly to GitHub Pages.

## Adding a research pass

1. Read the repositories themselves. Prefer README/result ledgers, explicit lineage notes and relevant commits over retrospective memory.
2. Create a pass file under `data/passes/`.
3. Give each node a **narrow** `claim`, plus `survived`, `killed`, `usefulness`, `confidence`, `evidence`, tags, and an `era`/`era_order`.
4. Add only edges you can defend. Do not create a chain because filenames look sequential.
5. Add the pass to `data/passes/index.json`.
6. Record surprising reversals or rediscoveries in `RESEARCH_LOG.md`.
7. Run the validator and tests.

The goal is not to make every old idea look prescient. The goal is to discover which small mechanisms survive repeated attempts to kill them—and which useful things were abandoned when the next repo began.
