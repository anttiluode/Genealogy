# Genealogy Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a dependency-free GitHub Pages atlas that separates a complete repository census from an evidence-backed research genealogy and cross-family survivor motifs.

**Architecture:** Plain JSON files are the source of truth. A small Python validator enforces graph/data integrity; a no-build HTML/CSS/JavaScript client renders the genealogy, census, survivor motifs, and archaeology queue. A Python inventory script plus GitHub Actions workflow can refresh the full public-repository census without turning repository-name similarity into genealogy evidence.

**Tech Stack:** JSON, Python 3.11+ standard library, `unittest`, plain HTML/CSS/JavaScript/SVG, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-15-genealogy-atlas-design.md`

## Global Constraints

- Dependency-free static page: no npm, bundler, framework, CDN, or build step.
- Names are discovery hints, never lineage evidence.
- Negative results are first-class nodes.
- Inventory completeness and genealogy confidence remain separate.
- Unknown/missing optional data must produce visible diagnostics, not a silently empty atlas.
- Scientific hypotheses never make CI red; CI validates data/page integrity only.

---

### Task 1: Define and validate the atlas data contract

**Files:**
- Create: `data/repos.json`
- Create: `data/nodes.json`
- Create: `data/edges.json`
- Create: `data/motifs.json`
- Create: `scripts/validate_data.py`
- Create: `tests/test_data.py`

**Interfaces:**
- Consumes: JSON arrays from `data/*.json`.
- Produces: `scripts.validate_data.load_atlas(root: Path) -> dict[str, list[dict]]` and `scripts.validate_data.validate_atlas(atlas: dict[str, list[dict]]) -> list[str]`.

- [ ] **Step 1: Write failing validation tests**

```python
from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]

class AtlasDataTests(unittest.TestCase):
    def test_repository_data_is_valid(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])

    def test_curated_nodes_are_unique_and_have_known_statuses(self):
        atlas = load_atlas(ROOT)
        ids = [node["id"] for node in atlas["nodes"]]
        self.assertEqual(len(ids), len(set(ids)))
        allowed = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
        self.assertTrue(all(node["status"] in allowed for node in atlas["nodes"]))

    def test_edges_and_motifs_reference_existing_nodes(self):
        atlas = load_atlas(ROOT)
        ids = {node["id"] for node in atlas["nodes"]}
        for edge in atlas["edges"]:
            self.assertIn(edge["source"], ids)
            self.assertIn(edge["target"], ids)
        for motif in atlas["motifs"]:
            self.assertTrue(set(motif["nodes"]).issubset(ids))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `python -m unittest tests.test_data -v`

Expected: FAIL because `scripts.validate_data` and the data files do not yet exist.

- [ ] **Step 3: Add minimal data files and validator**

`data/repos.json` initially contains `[]`; the curated files contain small valid seed arrays that will be expanded in Task 2.

Validator requirements:

```python
KNOWN_STATUSES = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
KNOWN_USEFULNESS = {"none", "conceptual", "scientific", "practical"}
KNOWN_CONFIDENCE = {"low", "medium", "high"}
KNOWN_EDGE_TYPES = {"inherits", "forks", "rediscovery", "corrects", "extracts", "converges"}
```

`validate_atlas` must detect duplicate node IDs, unknown enum values, dangling edge endpoints, duplicate edge triplets `(source, target, type)`, motif references to unknown nodes, and duplicate repository names.

- [ ] **Step 4: Run tests and validator**

Run:

```bash
python -m unittest tests.test_data -v
python scripts/validate_data.py
```

Expected: PASS and `atlas data: OK`.

- [ ] **Step 5: Commit**

Commit message: `feat: define genealogy data contract`

---

### Task 2: Seed the evidence-backed genealogy and survivor motifs

**Files:**
- Modify: `data/nodes.json`
- Modify: `data/edges.json`
- Modify: `data/motifs.json`
- Create: `RESEARCH_LOG.md`
- Test: `tests/test_data.py`

**Interfaces:**
- Consumes: schema validated by Task 1.
- Produces: at least 25 inspected pivotal nodes, evidence-backed edges, and at least five cross-family motifs.

- [ ] **Step 1: Add a failing content-floor test**

Add:

```python
def test_first_slice_has_meaningful_curated_content(self):
    atlas = load_atlas(ROOT)
    self.assertGreaterEqual(len(atlas["nodes"]), 25)
    self.assertGreaterEqual(len(atlas["edges"]), 20)
    self.assertGreaterEqual(len(atlas["motifs"]), 5)
    self.assertGreaterEqual(sum(node["usefulness"] == "practical" for node in atlas["nodes"]), 2)
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `python -m unittest tests.test_data.AtlasDataTests.test_first_slice_has_meaningful_curated_content -v`

Expected: FAIL until the seed genealogy is populated.

- [ ] **Step 3: Populate inspected nodes**

Seed from already inspected evidence and explicit lineage notes, including at minimum:

`Clockfield`, `Geometric-Neuron`, `FunctionalArbors`, `Operaattori`, `OperaattoriJako`, `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `BlackBoxLab`, `SplatWorld`, `Splatworld2`, `TinyAvatar`, `TinyAvatar2`, `WorldModel`, `Kompressori`, `GAx`, `ThirdWay`, `AnttisNeuron`, `GrowingAnttisNeuron`, `NewMachine`, `FusionMachine`, `PhaseStigmergy`, `Child`, `AlgoSchalgo`, `ObjektiYksi`, `TransformerStudy`.

Every node must include `claim`, `survived`, `killed`, `usefulness`, `confidence`, `evidence`, and `tags`. Wording must distinguish measured results from interpretation.

- [ ] **Step 4: Add only evidence-backed edges**

Use explicit lineage statements, repo evolution, or inspected documentation. Include practical extraction edges such as `LentoOrava -> LentoOrava/PulseTriage` only if represented as a dedicated node; otherwise record PulseTriage as the practical `survived` mechanism on `LentoOrava` and avoid inventing a repository node.

- [ ] **Step 5: Add survivor motifs and research log**

Initial motifs: `persistent-state`, `structure-as-computation`, `bounded-observation`, `active-intervention`, `operator-update`, `scalar-causal-credit`, `late-relevance`, `provenance` where enough reviewed nodes support them.

`RESEARCH_LOG.md` records why the first graph is sparse and lists the major corrections/negative results discovered in the initial sweep.

- [ ] **Step 6: Run validation tests**

Run:

```bash
python -m unittest tests.test_data -v
python scripts/validate_data.py
```

Expected: PASS.

- [ ] **Step 7: Commit**

Commit message: `data: seed evidence-backed research genealogy`

---

### Task 3: Build the static atlas explorer

**Files:**
- Create: `index.html`
- Create: `assets/app.js`
- Create: `assets/style.css`
- Create: `tests/test_static_page.py`

**Interfaces:**
- Consumes: `data/repos.json`, `data/nodes.json`, `data/edges.json`, `data/motifs.json` via `fetch()`.
- Produces: browser UI with `genealogy`, `census`, `survivors`, and `queue` views.

- [ ] **Step 1: Write failing static-contract tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StaticPageTests(unittest.TestCase):
    def test_page_has_required_views_and_no_external_dependencies(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for view in ("genealogy", "census", "survivors", "queue"):
            self.assertIn(f'data-view="{view}"', html)
        self.assertNotIn("https://cdn", html)
        self.assertNotIn("unpkg.com", html)

    def test_app_loads_all_data_files(self):
        js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
        for path in ("data/repos.json", "data/nodes.json", "data/edges.json", "data/motifs.json"):
            self.assertIn(path, js)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run and verify failure**

Run: `python -m unittest tests.test_static_page -v`

Expected: FAIL because page assets do not yet exist.

- [ ] **Step 3: Implement semantic page shell and styling**

`index.html` contains the masthead, summary counters, search/filter controls, four view buttons using `data-view`, graph container, detail panel, diagnostics panel, and footer linking the repository.

`assets/style.css` uses CSS variables and responsive layout. It must remain readable on narrow screens and use status/family shapes/borders in addition to color so meaning is not color-only.

- [ ] **Step 4: Implement the data loader and diagnostics**

`assets/app.js` exports/defines:

```javascript
async function loadJson(path)
async function loadAtlas()
function validateClientAtlas(atlas)
function renderDiagnostics(messages)
```

Each optional data load failure is caught and shown visibly; missing census data does not prevent curated genealogy from rendering.

- [ ] **Step 5: Implement graph, details, filters, and views**

Use dependency-free SVG. A deterministic family-column layout is sufficient for v1; do not implement a physics simulation. Clicking a node populates claim/survived/killed/evidence/usefulness. Filters hide nodes/edges without mutating source data. Census renders a searchable table. Survivors render motif cards linking back to curated nodes. Queue prioritizes unread census items with simple transparent heuristics.

- [ ] **Step 6: Run tests**

Run:

```bash
python -m unittest tests.test_static_page -v
python -m unittest discover -s tests -v
```

Expected: PASS.

- [ ] **Step 7: Commit**

Commit message: `feat: add interactive genealogy atlas`

---

### Task 4: Add reproducible full-repository census refresh

**Files:**
- Create: `scripts/refresh_repos.py`
- Create: `tests/test_refresh_repos.py`
- Create: `.github/workflows/refresh-repos.yml`
- Modify: `data/repos.json`

**Interfaces:**
- Produces: `fetch_public_repos(user: str, opener=urlopen) -> list[dict]` and normalized repository rows written to `data/repos.json`.
- GitHub workflow invokes `python scripts/refresh_repos.py anttiluode` and commits changes when the census differs.

- [ ] **Step 1: Write failing normalization/pagination tests**

Use fake JSON responses for pages of repositories; test that pagination stops on a short page and normalized rows contain `name`, `url`, `default_branch`, `size`, `visibility`, `description`, `created_at`, `updated_at`, and `inventory_status`.

- [ ] **Step 2: Run and verify failure**

Run: `python -m unittest tests.test_refresh_repos -v`

Expected: FAIL because refresh script does not exist.

- [ ] **Step 3: Implement standard-library GitHub API fetcher**

Use `urllib.request.Request` with `Accept: application/vnd.github+json`, `User-Agent: genealogy-atlas`, `per_page=100`, and monotonically increasing `page`. If `GITHUB_TOKEN` exists, add bearer authorization. Preserve existing `inventory_status` by repository name when rewriting the census.

- [ ] **Step 4: Add workflow**

Workflow triggers on `workflow_dispatch` and weekly schedule, grants `contents: write`, runs validator/tests after refresh, and commits only `data/repos.json` with message `data: refresh repository census` when changed.

- [ ] **Step 5: Populate/refresh the initial census**

Run: `python scripts/refresh_repos.py anttiluode`

Expected: public repositories are written in stable case-insensitive name order. If rate-limited, retain the current file and print a nonzero actionable error; never replace it with an empty census.

- [ ] **Step 6: Run all tests**

Run: `python -m unittest discover -s tests -v`

Expected: PASS.

- [ ] **Step 7: Commit**

Commit message: `feat: automate repository census refresh`

---

### Task 5: Document contribution rules and verify the first slice

**Files:**
- Create: `README.md`
- Modify: `RESEARCH_LOG.md`

**Interfaces:**
- Produces: human instructions for extending census, nodes, edges, motifs, and evidence without introducing inferred lineage.

- [ ] **Step 1: Add README**

Document the four views, local static serving command (`python -m http.server 8000`), validation command, census refresh command, edge evidence rules, status meanings, and GitHub Pages entry point.

- [ ] **Step 2: Record first-slice archaeological findings**

Update `RESEARCH_LOG.md` with reviewed families, strongest practical extractions, major negative results, and an explicit prioritized queue for the next archaeology pass.

- [ ] **Step 3: Run full verification**

Run:

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
python -m http.server 8000
```

Expected: validator reports `atlas data: OK`; all tests pass; `http://localhost:8000/` loads the four-view atlas without console-blocking data errors.

- [ ] **Step 4: Commit**

Commit message: `docs: explain genealogy archaeology workflow`
