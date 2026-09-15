# Genealogy Atlas — Design

Date: 2026-09-15

## Purpose

Build a living research atlas for the `anttiluode` GitHub corpus. The project must help answer four different questions without conflating them:

1. **What exists?** — a complete repository census.
2. **What descended from what?** — curated, evidence-backed genealogy.
3. **What mechanisms recur independently?** — cross-family survivor motifs.
4. **What is actually useful?** — practical extractions and projects that crossed from metaphor into an externally useful mechanism.

The atlas is deliberately not a machine-generated story over repository names. Completeness belongs to the census; confidence belongs to the curated genealogy.

## Approach

Use a hybrid architecture.

- Automatically inventory every accessible repository and basic metadata.
- Curate relationships only after inspecting repository evidence (README, results, commits, branch notes, or explicit lineage notes).
- Store uncertainty explicitly rather than filling gaps with guesses.
- Render everything in a dependency-free static GitHub Pages application.

This avoids the two failure modes at the extremes: a small hand-written family tree that immediately becomes stale, and a visually impressive 400-node graph whose inferred edges are mostly fiction.

## Data model

### Repository inventory

`data/repos.json` contains one record for every discovered repository.

Suggested fields:

- `name`
- `url`
- `visibility`
- `default_branch`
- `size`
- `created_at` / `updated_at` when available
- `description` when available
- `inventory_status`: `unread`, `sampled`, `reviewed`
- broad name-derived hints only when clearly marked as hints

Inventory records do not imply genealogy.

### Curated nodes

`data/nodes.json` contains research interpretation only for inspected repositories.

Fields:

- `id` — repository name
- `family` — e.g. geometric-neuron, clockfield, splat-world, bounded-observer, morphogenesis, operator-response, practical-tools
- `status` — one of `idea-mine`, `experiment`, `negative`, `ledger`, `tool`, `survivor`, `active`
- `claim` — narrow statement the repo actually tested or embodied
- `survived` — mechanism worth carrying forward
- `killed` — interpretation/control that failed or was narrowed
- `usefulness` — `none`, `conceptual`, `scientific`, `practical`
- `confidence` — `low`, `medium`, `high`
- `evidence` — short human-readable note and relevant repository path/URL
- `tags` — mechanism tags such as `bounded-observation`, `active-probing`, `persistent-state`, `operator-update`, `routing`, `structural-memory`

### Curated edges

`data/edges.json` records only relationships supported by evidence.

Edge types:

- `inherits` — direct conceptual or code lineage
- `forks` — deliberate branch/new repo from predecessor
- `rediscovery` — same mechanism reached from another route
- `corrects` — later repo explicitly narrows/kills an earlier interpretation
- `extracts` — practical tool/mechanism extracted from a research line
- `converges` — multiple lineages intentionally combined

Fields:

- `source`
- `target`
- `type`
- `confidence`
- `why`
- `evidence`

No edge is created solely because names look similar.

### Survivor motifs

`data/motifs.json` represents mechanisms that appear across multiple families. Initial motifs:

- persistent distributed state
- structure determines computation
- bounded/addressed observation
- intervention reveals hidden dynamics
- experience changes future operators
- sparse publication / routing identity
- state is not current relevance
- provenance: observed versus imagined state
- low-rank change in a high-rank substrate
- scalar consequence localizes causal action

A motif links to curated nodes, not raw repos.

## Static application

The root `index.html` is a no-build GitHub Pages app using plain HTML/CSS/JavaScript and SVG.

Views:

### 1. Genealogy

Interactive SVG graph of curated nodes and evidence-backed edges.

- pan/zoom-lite through viewBox controls or simple transform
- click node to open a detail panel
- edge legend and confidence styling
- filters by family, status, mechanism, usefulness
- search by repository name

The initial graph is intentionally sparse. Unreviewed repos remain visible in the census rather than being given speculative ancestry.

### 2. Census

Searchable/filterable table of the full repository inventory.

- reviewed vs unread count
- family hints where available
- links to GitHub
- sort by size/name/update date when metadata exists

### 3. Survivors

Mechanism-centric view answering: “What kept coming back?” Each motif shows the otherwise unrelated repos in which it appeared and how its interpretation changed.

### 4. Archaeology queue

A prioritized list of unread/sampled repositories worth inspecting next. Priority should favor:

- old repos that appear to precede a later major family
- abandoned starts with nontrivial code/results
- explicit cross-links from important later READMEs
- practical tools that may have been forgotten
- negative results that later lines may have unknowingly repeated

## Research rules

1. **Names are discovery hints, never lineage evidence.**
2. **Negative results are first-class nodes.** A killed idea can be more genealogically important than a successful demo.
3. **Separate mechanism from metaphor.** “Field,” “neuron,” “splat,” or “quantum” vocabulary does not define a family if the actual mechanism differs.
4. **Record practical extraction.** If an abstract experiment becomes a usable tool (for example scalar causal probing becoming regression triage), that gets an `extracts` edge.
5. **Do not erase embarrassing ancestors.** The atlas is useful precisely because it shows overclaims, rediscoveries, and course corrections.
6. **Confidence is visible.** Low-confidence edges are allowed only when there is some evidence and are visually distinct.

## Initial curated spine

The first usable version should include the families already supported by current inspection:

- early field / resonance / Clockfield idea-mine family
- Geometric Neuron sequence
- FunctionalArbors / morphogenesis
- Operaattori / operator view
- GeometricNeuronV24 / addressable observation
- ReadWrite / intervention + observability
- LentoOrava → PulseTriage practical extraction
- BlackBoxLab / history hardening into shared substrate
- SplatWorld / TinyAvatar / WorldModel
- Kompressori / response-geometry and low-rank operator updates
- GAx / ThirdWay / search-to-routing line
- AnttisNeuron / GrowingAnttisNeuron / NewMachine / FusionMachine convergence

This is not claimed to be the final genealogy; it is the first evidence-backed scaffold.

## Error handling

- The page must still render if one optional data file is absent; it should show an explicit “data not loaded” panel rather than silently presenting an empty atlas.
- Unknown statuses/families use neutral styling.
- Dangling edges are ignored and reported in the page diagnostics panel.
- Duplicate IDs are detected client-side and reported.
- External links use the canonical GitHub repository URL.

## Testing

Keep the project dependency-free but test the data and page contract.

- `tests/test_data.py` validates JSON syntax, unique node IDs, known enum values, edge endpoints, and motif references.
- a lightweight static smoke check confirms `index.html` references the expected data files and contains no build-time dependencies.
- CI runs the tests on pushes/PRs.

Scientific content is not made CI-red merely because a hypothesis is negative; CI validates atlas integrity, not whether an idea “won.”

## Growth strategy

The atlas grows in passes rather than pretending to finish 400 repositories at once.

- **Pass 0:** infrastructure + full census + ~25 pivotal curated nodes.
- **Pass 1:** major named families and explicit cross-links.
- **Pass 2:** older abandoned starts and idea mines.
- **Pass 3:** practical/software repos outside the brain/AI spine.
- **Pass 4:** duplicate-mechanism audit: identify experiments unknowingly repeated under new names.

Each pass updates both the machine-readable data and a short `RESEARCH_LOG.md` explaining notable discoveries/corrections.

## Definition of done for the first slice

The first slice is useful when:

- the static page opens directly from GitHub Pages;
- the complete repository census is present or clearly records pagination limits;
- at least ~25 pivotal repos are curated with evidence rather than name inference;
- at least five cross-family survivor motifs are visible;
- the page distinguishes unread inventory from reviewed genealogy;
- tests validate the graph/data structure;
- README explains how to extend the atlas without inventing ancestry.
