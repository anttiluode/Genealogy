from __future__ import annotations

import json
import sys
from pathlib import Path

KNOWN_STATUSES = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
KNOWN_USEFULNESS = {"none", "conceptual", "scientific", "practical"}
KNOWN_CONFIDENCE = {"low", "medium", "high"}
KNOWN_EDGE_TYPES = {"inherits", "forks", "rediscovery", "corrects", "extracts", "converges"}
KNOWN_EVIDENCE_RESULTS = {"supports", "contradicts", "mixed", "inconclusive"}
KNOWN_MOTIF_RELATIONS = {"supports", "limits", "documents"}
KNOWN_QUESTION_STATES = {"open", "partially-resolved", "resolved"}
FORBIDDEN_QUESTION_KEYS = {"score", "probability", "winner", "ranking", "rank"}


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _load_passes(data: Path) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    index_path = data / "passes" / "index.json"
    if not index_path.exists():
        return [], [], [], []
    entries = _read_json(index_path)
    passes, nodes, edges, motifs = [], [], [], []
    for entry in entries:
        if not entry.get("enabled", True):
            continue
        path = data / "passes" / entry["path"]
        payload = _read_json(path)
        pass_id = payload["id"]
        passes.append({
            "id": pass_id,
            "title": payload.get("title", pass_id),
            "summary": payload.get("summary", ""),
            "order": payload.get("order", 999),
            "reviewed_at": payload.get("reviewed_at", ""),
            "path": entry["path"],
        })
        for node in payload.get("nodes", []):
            item = dict(node)
            item.setdefault("pass_id", pass_id)
            nodes.append(item)
        edges.extend(dict(edge, pass_id=edge.get("pass_id", pass_id)) for edge in payload.get("edges", []))
        motifs.extend(dict(motif, pass_id=motif.get("pass_id", pass_id)) for motif in payload.get("motifs", []))
    return passes, nodes, edges, motifs


def load_atlas(root: Path) -> dict:
    data = root / "data"
    base_nodes = _read_json(data / "nodes.json")
    for node in base_nodes:
        node.setdefault("pass_id", "foundation")
        node.setdefault("era", "Foundation atlas")
        node.setdefault("era_order", 0)
    passes, pass_nodes, pass_edges, pass_motifs = _load_passes(data)
    return {
        "repos": _read_json(data / "repos.json"),
        "nodes": base_nodes + pass_nodes,
        "edges": _read_json(data / "edges.json") + pass_edges,
        "motifs": _read_json(data / "motifs.json") + pass_motifs,
        "evidence": _read_json(data / "evidence.json"),
        "evidence_motif_relations": _read_json(data / "evidence_motif_relations.json"),
        "questions": _read_json(data / "questions.json"),
        "passes": [
            {"id": "foundation", "title": "Foundation atlas", "summary": "The first cross-family curated slice.", "order": 0, "reviewed_at": "2026-09-15", "path": None}
        ] + passes,
    }


def _dupes(values):
    seen = set()
    dupes = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return sorted(dupes)


def _find_forbidden_question_keys(value, prefix="") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            if key.lower() in FORBIDDEN_QUESTION_KEYS:
                found.append(path)
            found.extend(_find_forbidden_question_keys(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            path = f"{prefix}[{index}]"
            found.extend(_find_forbidden_question_keys(child, path))
    return found


def validate_atlas(atlas: dict) -> list[str]:
    errors: list[str] = []
    nodes = atlas.get("nodes", [])
    edges = atlas.get("edges", [])
    motifs = atlas.get("motifs", [])
    evidence = atlas.get("evidence", [])
    evidence_motif_relations = atlas.get("evidence_motif_relations", {})
    questions = atlas.get("questions", [])
    repos = atlas.get("repos", [])
    passes = atlas.get("passes", [])

    node_ids = [node.get("id") for node in nodes]
    for value in _dupes(node_ids):
        errors.append(f"duplicate node id: {value}")
    ids = set(node_ids)

    pass_ids = [item.get("id") for item in passes]
    for value in _dupes(pass_ids):
        errors.append(f"duplicate pass id: {value}")
    known_passes = set(pass_ids)

    for node in nodes:
        node_id = node.get("id", "<missing>")
        if node.get("status") not in KNOWN_STATUSES:
            errors.append(f"unknown status for {node_id}: {node.get('status')}")
        if node.get("usefulness") not in KNOWN_USEFULNESS:
            errors.append(f"unknown usefulness for {node_id}: {node.get('usefulness')}")
        if node.get("confidence") not in KNOWN_CONFIDENCE:
            errors.append(f"unknown confidence for {node_id}: {node.get('confidence')}")
        if node.get("pass_id") not in known_passes:
            errors.append(f"unknown pass for {node_id}: {node.get('pass_id')}")
        if not isinstance(node.get("era_order", 0), int):
            errors.append(f"non-integer era_order for {node_id}")

    edge_keys = []
    for edge in edges:
        key = (edge.get("source"), edge.get("target"), edge.get("type"))
        edge_keys.append(key)
        if edge.get("type") not in KNOWN_EDGE_TYPES:
            errors.append(f"unknown edge type: {edge.get('type')}")
        if edge.get("confidence") not in KNOWN_CONFIDENCE:
            errors.append(f"unknown edge confidence: {edge.get('confidence')}")
        if edge.get("source") not in ids:
            errors.append(f"dangling edge source: {edge.get('source')}")
        if edge.get("target") not in ids:
            errors.append(f"dangling edge target: {edge.get('target')}")
        if edge.get("pass_id") and edge.get("pass_id") not in known_passes:
            errors.append(f"unknown edge pass: {edge.get('pass_id')}")
    for value in _dupes(edge_keys):
        errors.append(f"duplicate edge: {value}")

    motif_ids = [m.get("id") for m in motifs]
    for value in _dupes(motif_ids):
        errors.append(f"duplicate motif id: {value}")
    motif_map = {motif.get("id"): motif for motif in motifs if motif.get("id")}
    for motif in motifs:
        for node_id in motif.get("nodes", []):
            if node_id not in ids:
                errors.append(f"motif {motif.get('id')} references unknown node: {node_id}")

    evidence_ids = [item.get("id") for item in evidence]
    for value in _dupes(evidence_ids):
        errors.append(f"duplicate evidence id: {value}")
    known_evidence = set(evidence_ids)
    if not isinstance(evidence_motif_relations, dict):
        errors.append("evidence motif relations must be an object")
        evidence_motif_relations = {}

    for item in evidence:
        evidence_id = item.get("id", "<missing>")
        if not isinstance(item.get("id"), str) or not item.get("id"):
            errors.append("evidence record missing id")
        if item.get("node") not in ids:
            errors.append(f"evidence {evidence_id} references unknown node: {item.get('node')}")
        if item.get("result") not in KNOWN_EVIDENCE_RESULTS:
            errors.append(f"unknown evidence result for {evidence_id}: {item.get('result')}")
        for field in ("claim", "design", "source"):
            if not isinstance(item.get(field), str) or not item.get(field).strip():
                errors.append(f"evidence {evidence_id} missing {field}")
        for field in ("metrics", "controls", "limitations", "motifs"):
            if not isinstance(item.get(field, []), list):
                errors.append(f"evidence {evidence_id} has non-list {field}")
        relations = evidence_motif_relations.get(evidence_id, {})
        if not isinstance(relations, dict):
            errors.append(f"evidence {evidence_id} motif relations must be an object")
            relations = {}
        if isinstance(item.get("motifs", []), list):
            for motif_id in item.get("motifs", []):
                motif = motif_map.get(motif_id)
                if motif is None:
                    errors.append(f"evidence {evidence_id} references unknown motif: {motif_id}")
                elif item.get("node") not in motif.get("nodes", []):
                    errors.append(f"evidence {evidence_id} links node {item.get('node')} to unrelated motif: {motif_id}")
                relation = relations.get(motif_id)
                if relation not in KNOWN_MOTIF_RELATIONS:
                    errors.append(f"evidence {evidence_id} missing/unknown motif relation for {motif_id}: {relation}")
            for motif_id in relations:
                if motif_id not in item.get("motifs", []):
                    errors.append(f"evidence {evidence_id} has relation for untagged motif: {motif_id}")
        sample = item.get("sample")
        if sample is not None:
            if not isinstance(sample, dict):
                errors.append(f"evidence {evidence_id} has invalid sample")
            else:
                if not isinstance(sample.get("unit"), str) or not sample.get("unit"):
                    errors.append(f"evidence {evidence_id} sample missing unit")
                count = sample.get("count")
                if not isinstance(count, (int, float)) or isinstance(count, bool) or count <= 0:
                    errors.append(f"evidence {evidence_id} sample has invalid count")
        for field in ("held_out", "external_data"):
            if field in item and not isinstance(item[field], bool):
                errors.append(f"evidence {evidence_id} has non-boolean {field}")

    for evidence_id in evidence_motif_relations:
        if evidence_id not in known_evidence:
            errors.append(f"motif relations reference unknown evidence: {evidence_id}")

    if not isinstance(questions, list):
        errors.append("questions ledger must be an array")
        questions = []
    question_ids = [item.get("id") for item in questions if isinstance(item, dict)]
    for value in _dupes(question_ids):
        errors.append(f"duplicate question id: {value}")

    for item in questions:
        if not isinstance(item, dict):
            errors.append("question record must be an object")
            continue
        question_id = item.get("id", "<missing>")
        if not isinstance(item.get("id"), str) or not item.get("id").strip():
            errors.append("question record missing id")
        if not isinstance(item.get("title"), str) or not item.get("title").strip():
            errors.append(f"question {question_id} missing title")
        if item.get("state") not in KNOWN_QUESTION_STATES:
            errors.append(f"question {question_id} has unknown state: {item.get('state')}")

        for key in _find_forbidden_question_keys(item):
            errors.append(f"question {question_id} contains forbidden field: {key}")

        question_motifs = item.get("motifs", [])
        if not isinstance(question_motifs, list) or not question_motifs:
            errors.append(f"question {question_id} must reference at least one motif")
            question_motifs = []
        for motif_id in question_motifs:
            if motif_id not in motif_map:
                errors.append(f"question {question_id} references unknown motif: {motif_id}")

        question_evidence = item.get("evidence", [])
        if not isinstance(question_evidence, list) or not question_evidence:
            errors.append(f"question {question_id} must reference at least one evidence record")
            question_evidence = []
        for evidence_id in question_evidence:
            if evidence_id not in known_evidence:
                errors.append(f"question {question_id} references unknown evidence: {evidence_id}")

        explanations = item.get("competing_explanations", [])
        if not isinstance(explanations, list) or len(explanations) < 2 or any(not isinstance(value, str) or not value.strip() for value in explanations):
            errors.append(f"question {question_id} needs at least two competing explanations")

        known = item.get("known", [])
        if not isinstance(known, list) or not known or any(not isinstance(value, str) or not value.strip() for value in known):
            errors.append(f"question {question_id} needs non-empty known evidence statements")

        if not isinstance(item.get("missing_discriminator"), str) or not item.get("missing_discriminator", "").strip():
            errors.append(f"question {question_id} missing discriminator")

        experiment = item.get("candidate_experiment")
        if not isinstance(experiment, dict):
            errors.append(f"question {question_id} missing candidate experiment")
        else:
            if not isinstance(experiment.get("design"), str) or not experiment.get("design", "").strip():
                errors.append(f"question {question_id} candidate experiment missing design")
            if not isinstance(experiment.get("cost"), str) or not experiment.get("cost", "").strip():
                errors.append(f"question {question_id} candidate experiment missing cost")
            outcomes = experiment.get("outcomes", [])
            if not isinstance(outcomes, list) or len(outcomes) < 2:
                errors.append(f"question {question_id} candidate experiment needs at least two outcomes")
            else:
                for outcome in outcomes:
                    if not isinstance(outcome, dict) or not isinstance(outcome.get("if"), str) or not outcome.get("if", "").strip() or not isinstance(outcome.get("then"), str) or not outcome.get("then", "").strip():
                        errors.append(f"question {question_id} has invalid candidate experiment outcome")

        resolution_evidence = item.get("resolution_evidence", [])
        if resolution_evidence is None:
            resolution_evidence = []
        if not isinstance(resolution_evidence, list):
            errors.append(f"question {question_id} resolution evidence must be a list")
            resolution_evidence = []
        for evidence_id in resolution_evidence:
            if evidence_id not in known_evidence:
                errors.append(f"question {question_id} resolution evidence references unknown evidence: {evidence_id}")
        if item.get("state") == "resolved" and not resolution_evidence:
            errors.append(f"question {question_id} is resolved without resolution evidence")
        if item.get("state") != "resolved" and resolution_evidence:
            errors.append(f"question {question_id} has resolution evidence while state is not resolved")

        notes = item.get("notes", [])
        if not isinstance(notes, list) or any(not isinstance(value, str) for value in notes):
            errors.append(f"question {question_id} has invalid notes")

    repo_names = [repo.get("name") for repo in repos]
    for value in _dupes(repo_names):
        errors.append(f"duplicate repository name: {value}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    atlas = load_atlas(root)
    errors = validate_atlas(atlas)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(
        f"atlas data: OK ({len(atlas['nodes'])} nodes across {len(atlas['passes'])} passes; "
        f"{len(atlas['evidence'])} empirical evidence records; {len(atlas['questions'])} unresolved questions)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
