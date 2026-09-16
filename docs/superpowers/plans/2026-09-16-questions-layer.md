# Questions Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a first-class unresolved scientific questions layer that turns audited evidence into explicit competing explanations and candidate discriminating experiments without scores or fake probabilities.

**Architecture:** Store explicit question records in `data/questions.json`, validate all references and resolution-state invariants in `scripts/validate_data.py`, and render a dedicated additive Questions view through `assets/questions.js` / `assets/questions.css`. Keep Queue unchanged and reuse the existing atlas/evidence hooks for navigation.

**Tech Stack:** Static HTML/CSS/JavaScript, JSON data, Python `unittest`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-16-questions-layer-design.md`

## Global Constraints

- No probability, universal score, ranking, or winner field.
- Questions may cite only known evidence and motif IDs.
- `resolved` questions require resolving evidence; unresolved questions must not claim resolution evidence.
- Candidate experiments must include at least two explicit possible outcomes.
- Queue remains semantically and technically separate.
- Questions UI must fail gracefully if its data cannot load.

---

### Task 1: Lock the Questions data contract with failing tests

**Files:**
- Create: `tests/test_questions_layer.py`

**Interfaces:**
- Consumes: repository JSON files and static assets.
- Produces: executable expectations for `data/questions.json`, validator loading, and Questions UI hooks.

- [ ] **Step 1: Write failing tests**

Create tests asserting: `questions.json` exists with at least five records; IDs are unique; initial records include active intervention, late relevance, bounded observation, structure-as-computation, and persistent-state motifs; `load_atlas()` exposes `questions`; `validate_atlas()` rejects malformed question references/state; `index.html` exposes a Questions tab/section and loads `assets/questions.js`; `questions.js` contains `renderQuestions` and loads `data/questions.json`.

- [ ] **Step 2: Run CI and verify RED**

Expected: Python test step fails because the questions data and UI do not exist yet while existing atlas validation remains green.

- [ ] **Step 3: Commit the red tests**

Commit message: `test: define unresolved questions layer contract`.

---

### Task 2: Add the structured questions ledger and validator

**Files:**
- Create: `data/questions.json`
- Modify: `scripts/validate_data.py`

**Interfaces:**
- Consumes: motif IDs from atlas motifs and evidence IDs from `data/evidence.json`.
- Produces: `atlas["questions"]: list[dict]` with validated unresolved-question objects.

- [ ] **Step 1: Seed five evidence-grounded questions**

Encode the five contrasts from the design spec. Each candidate experiment has:

```json
{
  "design": "...",
  "cost": "small / medium / large with concrete resource note",
  "outcomes": [
    {"if": "observable outcome A", "then": "interpretation A becomes more plausible"},
    {"if": "observable outcome B", "then": "interpretation B becomes more plausible"}
  ]
}
```

All initial records are `open` or `partially-resolved`; none include `resolution_evidence`.

- [ ] **Step 2: Extend `load_atlas()`**

Load `data/questions.json` into `atlas["questions"]`.

- [ ] **Step 3: Add validator rules**

Add `KNOWN_QUESTION_STATES = {"open", "partially-resolved", "resolved"}` and enforce the design invariants, including reference integrity and the ban on score/probability/winner keys.

- [ ] **Step 4: Run focused tests**

Expected: data-contract and validator tests pass; static UI-hook test remains red.

- [ ] **Step 5: Commit**

Commit message: `feat: add unresolved questions ledger`.

---

### Task 3: Add the Questions view as an isolated UI module

**Files:**
- Create: `assets/questions.js`
- Create: `assets/questions.css`
- Modify: `index.html`

**Interfaces:**
- Consumes: global `atlas`, `loadJson`, `filters`, `escapeHtml`, `switchView`, and evidence/node IDs.
- Produces: `renderQuestions()`, Questions tab/section, evidence/node navigation.

- [ ] **Step 1: Add Questions tab and section**

Insert Questions between Evidence and Survivors, load `assets/questions.css`, and load `assets/questions.js` after evidence.js so question rendering can use evidence metadata already attached to `atlas`.

- [ ] **Step 2: Implement additive loader and renderer**

`questions.js` loads `data/questions.json`, attaches `atlas.questions`, wraps `renderCurrentView`, and renders cards with state, motifs, repositories/evidence, competing explanations, discriminator, candidate experiment, conditional outcomes, and notes.

If loading fails, show an in-view diagnostic while leaving all other atlas views functional.

- [ ] **Step 3: Add navigation hooks**

Repository buttons call `switchView('genealogy')` + `selectNode(id)`. Evidence buttons set search to the evidence record's node/relevant identifier and open the Evidence view.

- [ ] **Step 4: Add responsive styling**

Use existing variables and visual vocabulary; distinguish `open`, `partially-resolved`, and `resolved` without implying a quality score.

- [ ] **Step 5: Run JavaScript syntax and Python tests**

Expected: all new tests pass.

- [ ] **Step 6: Commit**

Commit message: `feat: render unresolved questions and candidate experiments`.

---

### Task 4: Documentation and CI coverage

**Files:**
- Modify: `README.md`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: the completed Questions data/UI.
- Produces: documented semantics and CI syntax coverage.

- [ ] **Step 1: Document the fourth layer**

Explain the progression:

```text
inventory -> interpretation -> evidence -> unresolved questions
```

and explicitly distinguish Questions from Queue.

- [ ] **Step 2: Add JS syntax check**

Add `node --check assets/questions.js` to validation workflow.

- [ ] **Step 3: Run full validation**

Expected: `scripts/validate_data.py`, all unittests, and all JS syntax checks pass.

- [ ] **Step 4: Commit**

Commit message: `docs: explain unresolved questions workflow`.

---

### Task 5: PR review, exact-head verification, merge, and deployment check

**Files:** none beyond review fixes.

**Interfaces:**
- Consumes: completed feature branch.
- Produces: merged/deployed Questions layer.

- [ ] **Step 1: Open draft PR**

Describe the five seeded questions, validation invariants, and intentional RED→GREEN cycle.

- [ ] **Step 2: Review full diff**

Check for overclaiming, accidental ranking/scoring language, broken references, and any claim that candidate experiments are already observed results.

- [ ] **Step 3: Verify exact PR head**

Require GitHub Actions success for data validation, Python tests, and JS syntax on the current head.

- [ ] **Step 4: Mark ready and merge**

Squash merge after green verification.

- [ ] **Step 5: Verify merged `main`**

Confirm post-merge validation and GitHub Pages deployment both succeed for the merge commit.
