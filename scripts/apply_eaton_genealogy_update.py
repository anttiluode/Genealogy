from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def upsert(items: list[dict], item: dict, key: str = "id") -> None:
    for i, current in enumerate(items):
        if current.get(key) == item.get(key):
            items[i] = item
            return
    items.append(item)


def main() -> None:
    evidence_path = DATA / "evidence.json"
    evidence = load(evidence_path)

    # Repair the bookkeeping mismatch exposed by the validator: the relation
    # map already documented these AOC results as negative-result evidence,
    # but the records themselves omitted the motif tag.
    aoc_negative_ids = {
        "aoc-qwen-heldout-graded-transfer",
        "aoc-qwen-order-identity-likelihood",
        "aoc-qwen-live-growing-cache",
    }
    for item in evidence:
        if item.get("id") in aoc_negative_ids:
            motifs = item.setdefault("motifs", [])
            if "negative-results" not in motifs:
                motifs.append("negative-results")

    upsert(
        evidence,
        {
            "id": "aoc-qwen-first-ask-masked-distance",
            "node": "AdaptiveObserverCache",
            "claim": "The corrected first-ask Qwen experiment isolates a split boundary: masked positional age leaves the neutral first-ask landscape almost unchanged and the observer still flips the matched valve-versus-sensor decision token at +256 positions, but maximum B trust no longer flips the complete candidate-sequence winner.",
            "design": "Build a source-only Qwen3-8B cache with no prior question or assistant answer, freeze the four previously selected causal heads, fork the cache at distance 0 and after exactly 256 unreadable masked spacer rows, then ask the question for the first time. At m=-1,0,+1 score complete candidate-sequence summed log probability and a matched first divergent token (valve versus sensor). Stop distance interpretation unless the full-sequence winner flip passes at distance 0.",
            "result": "mixed",
            "motifs": [
                "observer-participates-in-dynamics",
                "measurement-receipt-validity",
                "persistent-state",
                "transient-operator-handoff",
                "negative-results",
            ],
            "sample": {"unit": "masked first-ask distance checkpoint", "count": 2},
            "metrics": [
                {"name": "distance-0 neutral summed margin A-minus-B", "value": 11.44948466937052},
                {"name": "distance-0 m=-1 summed margin A-minus-B", "value": -0.2869706675410342},
                {"name": "distance-0 m=-1 matched token gap A-minus-B", "value": -0.7500000298023224},
                {"name": "distance-256 neutral summed margin A-minus-B", "value": 11.549099114722253},
                {"name": "distance-256 m=-1 summed margin A-minus-B", "value": 0.5213137194512569},
                {"name": "distance-256 m=-1 matched token gap A-minus-B", "value": -1.75},
                {"name": "distance-0 full sequence winner flip", "value": 1},
                {"name": "distance-256 full sequence winner flip", "value": 0},
                {"name": "distance-256 matched-token winner flip", "value": 1},
                {"name": "source-cache integrity", "value": 1},
            ],
            "controls": [
                "The canonical anchor contains system plus sources only: question_was_in_anchor=false and prior_assistant_answer_in_anchor=false",
                "Exactly 256 masked spacer rows advance cache/RoPE position while remaining unreadable to later queries",
                "Same frozen Qwen weights, source spans and four-head observer plan at both distances",
                "Complete summed candidate likelihood is reported alongside a matched decision-token diagnostic",
                "Source K integrity remains true and no prior assistant answer can create a re-ask policy",
            ],
            "replication": "One valve-versus-sensor calibration conflict at two masked positional distances with three trust states each",
            "held_out": false,
            "external_data": false,
            "limitations": [
                "This is one synthetic conflict with a saturated neutral preference, not a general long-context benchmark",
                "The matched local decision moves farther toward sensor at +256 while the complete sensor sentence loses; that does not by itself identify whether the tail failure is source-detail copying or continued observer interference",
                "A phasic tail control has not yet been run: observer through the sensor decision then m=0 for the tail versus tonic observer and neutral forced-B",
            ],
            "source": "https://github.com/anttiluode/AdaptiveObserverCache/blob/main/results/qwen_observer_first_ask_distance.json",
        },
    )

    upsert(
        evidence,
        {
            "id": "eaton-v0-gating-demo",
            "node": "EATON",
            "claim": "The frozen EATON v0 harness correctly implements a constructed gating demonstration: releasing a context-writing operator before the payload stage preserves resident context, while keeping that same writer active overwrites the state needed by the later operator.",
            "design": "Freeze a three-tick resident-state machine before running it. All arms receive the same context and payload events and are identical through the early decision. Transient releases operator A after the context write; tonic leaves A active during the payload tick; reset restores resident memory to the episode's initial value at handoff. Run 64 seeds with 256 balanced episodes each and fixed pass thresholds.",
            "result": "supports",
            "motifs": ["transient-operator-handoff"],
            "sample": {"unit": "seed", "count": 64},
            "metrics": [
                {"name": "median early accuracy transient", "value": 1.0},
                {"name": "median early accuracy tonic", "value": 1.0},
                {"name": "median early accuracy reset", "value": 1.0},
                {"name": "median final accuracy transient", "value": 1.0},
                {"name": "median final accuracy tonic", "value": 0.5},
                {"name": "median final accuracy reset", "value": 0.501953125},
                {"name": "transient seed wins versus tonic", "value": 64},
                {"name": "transient seed wins versus reset", "value": 64},
            ],
            "controls": [
                "Pass rule, coefficients, noise, seed count and event schedule were frozen before the canonical result",
                "All arms replay the same sampled world tape and have identical early-stage states and event budgets",
                "Tonic A and payload operator B write disjoint coordinates on the simultaneous payload tick, so Python update order is not the witness",
                "Reset differs from transient only at resident memory handoff",
            ],
            "replication": "64 canonical seeds; committed receipt is regression-checked against a fresh recomputation on Python 3.11 and 3.12",
            "held_out": false,
            "external_data": false,
            "limitations": [
                "The v0 outcome is analytically implied by the frozen coefficients: tonic A gives the new payload a larger contribution than retained context, so memory takes payload sign and the balanced final task collapses to chance",
                "This is a constructed demonstration of gating, not evidence that transient operator lifetime is a newly discovered or generally superior principle",
                "The overwrite problem has a classical antecedent in LSTM-style input gating; EATON v0 should be read as a harness validation and explicit resident-operator formulation",
                "The non-hand-designed Qwen question remains open: whether phasic observer control can recover the tail after the local sensor decision at +256 masked positions",
            ],
            "source": "https://github.com/anttiluode/EATON/blob/main/results/v0_handoff.json",
        },
    )
    save(evidence_path, evidence)

    relations_path = DATA / "evidence_motif_relations.json"
    relations = load(relations_path)
    relations["aoc-qwen-first-ask-masked-distance"] = {
        "observer-participates-in-dynamics": "supports",
        "measurement-receipt-validity": "supports",
        "persistent-state": "supports",
        "transient-operator-handoff": "documents",
        "negative-results": "documents",
    }
    relations["eaton-v0-gating-demo"] = {"transient-operator-handoff": "supports"}
    save(relations_path, relations)

    questions_path = DATA / "questions.json"
    questions = load(questions_path)
    for question in questions:
        if question.get("id") != "aoc-live-distance-control":
            continue
        question["title"] = "Why does first-ask observer control survive at the local decision but fail across the +256-token continuation?"
        question["state"] = "partially-resolved"
        if "transient-operator-handoff" not in question["motifs"]:
            question["motifs"].append("transient-operator-handoff")
        if "aoc-qwen-first-ask-masked-distance" not in question["evidence"]:
            question["evidence"].append("aoc-qwen-first-ask-masked-distance")
        question["competing_explanations"] = [
            "The observer is useful mainly at a local commitment boundary: it can select sensor over valve, but keeping the same query intervention active through later tokens perturbs a different copying/follow-through computation and erases the sequence-level win.",
            "The observer is not the main tail problem; copying older source-B details such as K and drifted becomes harder with positional age, so the same locally correct sensor choice still yields a weaker full B continuation even if the intervention is released.",
            "Both effects contribute: positional age changes the downstream basin while tonic observer expression adds a second token-specific disturbance, so phasic release will help but will not fully restore the distance-0 sequence margin.",
        ]
        question["known"] = [
            "The corrected source-only first-ask anchor is 93 tokens and contains neither the question nor a prior assistant answer; the withheld first-question suffix is 27 tokens.",
            "At distance 0, m=-1 flips the complete sequence to B with A-minus-B summed margin -0.28697 and flips the matched valve/sensor token gap to -0.75; m=+1 favors A, so both first-ask gates pass.",
            "After exactly 256 unreadable masked spacer positions, neutral remains almost unchanged (+11.5491 versus +11.4495 A-minus-B), so the large neutral flip in the earlier visible-filler sweep came from readable intervening conversation rather than masked positional age.",
            "At +256, m=-1 still moves the matched valve/sensor decision farther toward B (token gap -1.75), but the full B sentence loses to A by +0.52131, so local control survives while complete-sequence control fails on this prompt.",
        ]
        question["missing_discriminator"] = "A matched tonic-versus-phasic tail test at +256: keep the observer on throughout, turn it off immediately after the sensor decision token, and compare both with neutral scoring of the forced-B continuation. This separates observer-induced tail damage from distance/source-copy difficulty."
        question["candidate_experiment"] = {
            "design": "Reuse the corrected source-only first-ask +256 masked checkpoint and frozen four-head plan. Score the sensor-B candidate under three matched arms: (1) tonic m=-1 for every candidate token, (2) phasic m=-1 only through the first divergent sensor token and m=0 for the remaining tail, and (3) neutral m=0 throughout while the same B tokens are teacher-forced. Report summed B log-probability, tokenwise tail deltas, source-cache integrity and the A/B sequence margin; do not change the cache, prompt, head plan or candidate text across arms.",
            "cost": "low-to-medium relative to the completed 8B sweep: one +256 checkpoint and three forced-scoring arms on the already-defined valve/sensor conflict",
            "outcomes": [
                {
                    "if": "Phasic release materially improves the B tail and restores or strongly narrows the full sequence margin relative to tonic, while neutral forced-B is also stronger than tonic",
                    "then": "The current observer should be treated as a boundary-local intervention: persist the intention, recompute the tangent, and pulse its expression rather than steering every downstream token.",
                },
                {
                    "if": "Phasic and tonic tails remain similarly weak while neutral forced-B is also weak at +256",
                    "then": "The dominant failure is ordinary long-distance continuation/copying or downstream basin geometry, not overlong observer expression; EATON remains only a toy gating analogy.",
                },
                {
                    "if": "Phasic helps some tail tokens but not the complete sequence",
                    "then": "The boundary is token/head specific and the next mechanism needs an explicit release policy rather than one global on/off lifetime.",
                },
            ],
        }
        question["notes"] = [
            "The visible-filler distance run is retained as a re-ask/trajectory confound control, not as evidence for positional decay or amplification.",
            "Neutral is saturated on this prompt, so matched decision-token control and full summed sequence control must remain separate readouts.",
            "EATON v0 does not resolve this question because its tonic failure is analytically built into the synthetic coefficients.",
        ]
        question.pop("resolution_evidence", None)
        break
    save(questions_path, questions)

    aoc_path = DATA / "passes" / "adaptive-observer-cache.json"
    aoc = load(aoc_path)
    aoc["reviewed_at"] = "2026-09-23"
    aoc["summary"] = (
        "AdaptiveObserverCache now has a corrected first-ask distance result. The earlier visible-filler sweep is retained as a confounded re-ask/trajectory control: its anchor already contained Qwen's first valve answer and the same question was asked again. The new harness anchors system+sources only, withholds the first question, and advances cache position using unreadable masked spacers. At distance 0, m=-1 genuinely flips the complete valve/sensor candidate winner to sensor (A-minus-B margin -0.28697) and the matched decision token to -0.75. At +256, neutral remains essentially unchanged (+11.549 versus +11.449), closing the earlier filler-landscape confound, and the matched decision token still flips more strongly toward sensor (-1.75); however the complete sensor sentence loses by +0.521 A-minus-B. The current boundary is therefore local decision control versus continuation control, not simple positional fade. The next discriminator is a tonic-versus-phasic tail test: steer through the sensor choice, then release the observer and compare the tail with tonic and neutral forced-B scoring."
    )
    node = aoc["nodes"][0]
    node["survived"] = (
        "The DistilGPT2 Gates 2–7 still establish persistent retrieval control and explicit provenance/current-address rebinding. On Qwen3-8B, causally selected frozen heads produce a real first-ask valve/sensor switch. The corrected first-ask distance harness removes the prior-answer/re-ask confound: with a 93-token source-only anchor, distance 0 at m=-1 flips the full summed sequence to B (-0.28697 A-minus-B) and the matched decision token to -0.75. After exactly 256 masked unreadable positions, source-cache integrity remains true, neutral full-sequence preference barely changes (+11.4495 to +11.5491), and the matched valve/sensor token still flips toward B even more strongly (-1.75). Thus local causal control survives the tested masked positional age."
    )
    node["killed"] = (
        "Several stronger stories remain dead. Geometry steering alone is not enough; causal head selection is required. The held-out strong generation-transfer gate failed. The earlier visible-filler distance sweep did not isolate distance because it re-asked a question after Qwen's closed first answer and changed readable conversational state. The corrected first-ask run also kills a simple 'local control implies whole continuation control' story: at +256, m=-1 selects sensor at the matched decision token but the complete B sentence still loses by +0.52131 A-minus-B. Whether that tail loss comes from positional copying difficulty or from leaving the observer active too long is not yet known."
    )
    for tag in ("first-ask", "masked-distance", "local-vs-sequence-control", "phasic-control-open"):
        if tag not in node["tags"]:
            node["tags"].append(tag)
    save(aoc_path, aoc)

    repos_path = DATA / "repos.json"
    repos = load(repos_path)
    upsert(
        repos,
        {
            "name": "EATON",
            "url": "https://github.com/anttiluode/EATON",
            "default_branch": "main",
            "size": 0,
            "visibility": "public",
            "description": "Event-Addressed Transient Operator Networks. Sol thinking repo. ",
            "created_at": "2026-09-23T03:39:13Z",
            "updated_at": "2026-09-23T04:17:57Z",
            "inventory_status": "reviewed",
        },
        key="name",
    )
    repos.sort(key=lambda item: item.get("name", "").casefold())
    save(repos_path, repos)

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    aoc_heading = "### AdaptiveObserverCache — persistent observer state becomes a transformer control loop"
    documentary_heading = "## Documentary confidence and empirical evidence"
    before, remainder = readme.split(aoc_heading, 1)
    _, after = remainder.split(documentary_heading, 1)
    replacement = f'''{aoc_heading}\n\n**AdaptiveObserverCache** now has a corrected first-ask distance result rather than the earlier re-ask confound. The previous visible-filler sweep is kept as a useful control: because its anchor already contained Qwen's closed valve answer and then asked the same question again, readable filler changed the conversational landscape and could not isolate positional age.\n\nThe corrected harness anchors **system + sources only** (93 cache tokens), withholds the 27-token first-question suffix, and advances distance with unreadable masked spacer rows. At distance 0, `m=-1` genuinely flips the complete candidate winner to sensor (**A−B summed margin −0.28697**) and the matched `valve`/`sensor` decision token to **−0.75**. After exactly **+256** masked positions, neutral is essentially unchanged (**+11.5491 vs +11.4495** A−B), so the earlier large neutral shift came from readable trajectory rather than masked positional age. Yet the observer still flips the local decision more strongly toward sensor (**token gap −1.75**) while the complete sensor sentence loses (**A−B +0.52131**). The current boundary is therefore precise: **local decision control survives while continuation control fails on this prompt.**\n\nThe next discriminator is now smaller than the old distance sweep: score the +256 B continuation with the observer **tonic throughout**, **phasic through the sensor decision then off**, and **neutral throughout with B forced**. If phasic release restores the tail, AOC has found a real frozen-model reason to pulse an intervention instead of steering every downstream token. If neutral forced-B is equally weak, ordinary long-distance continuation/copying is the better explanation.\n\n### EATON — transient handoff as an explicit gating demonstration\n\n**EATON** extracts that timing idea into a tiny resident-state machine: an addressed operator writes context, crosses an early boundary, then either releases before the payload computation or remains tonically active. The frozen v0 receipt is mechanically clean—early accuracy is **1.000** in all arms; final accuracy is **1.000 transient**, **0.500 tonic**, **0.501953125 reset**, with **64/64** seed wins against each attacker and matched event/state invariants.\n\nBut this is deliberately cataloged as a **constructed gating demonstration, not a discovery**. The tonic failure is derivable directly from the chosen coefficients: during the payload tick the always-on writer gives the new payload a larger term than retained context, so resident memory takes the payload sign and the balanced task collapses to chance. The overwrite problem also has classical input-gating antecedents such as LSTM-style memory protection. EATON therefore earns a clean harness and a useful vocabulary—event → transient operator → resident residue → handoff—but not a claim that phasic control is generally superior. The non-hand-designed test remains AOC/Qwen.\n\nGenealogically, EATON sits where `SimpleNeuron`/`NSSN2` (rich resident state plus small travelling events), `FrequencyAddressedNonlinearModalCell` (addressed access to richer receiver dynamics), `OperatorTime` (history-conditioned effective operators), `ActiveVectorNN` (resident state versus sparse events), and `AdaptiveObserverCache` (persistent intent changing a frozen model's current read) meet. `AnotherOddThing` and `EvoX` remain adjacent rather than direct ancestors: they ask how to choose or search interventions/procedures, whereas EATON v0 only isolates the lifetime of an already-selected operator.\n\n{documentary_heading}'''
    readme = before + replacement + after
    readme = readme.replace(
        "Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, `WhatToLookAt`, and `AdaptiveObserverCache`.",
        "Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, `WhatToLookAt`, `AdaptiveObserverCache`, and `EATON`.",
    )
    readme_path.write_text(readme, encoding="utf-8")

    index_path = ROOT / "index.html"
    index = index_path.read_text(encoding="utf-8")
    index = re.sub(
        r'<div class="eyebrow">RECENT UPDATE · [^<]*</div>',
        '<div class="eyebrow">RECENT UPDATE · EATON transient handoff · AOC first-ask distance · Operator Time · SimpleNeuron/NSSN2</div>',
        index,
        count=1,
    )
    index_path.write_text(index, encoding="utf-8")


if __name__ == "__main__":
    main()
