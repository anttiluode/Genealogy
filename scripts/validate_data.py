from __future__ import annotations

import json
import sys
from pathlib import Path

KNOWN_STATUSES = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
KNOWN_USEFULNESS = {"none", "conceptual", "scientific", "practical"}
KNOWN_CONFIDENCE = {"low", "medium", "high"}
KNOWN_EDGE_TYPES = {"inherits", "forks", "rediscovery", "corrects", "extracts", "converges"}
KNOWN_EVIDENCE_RESULTS = {"supports", "contradicts", "mixed", "inconclusive"}


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


def load_atlas(root: Path) -> dict[str, list[dict]]:
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


def validate_atlas(atlas: dict[str, list[dict]]) -> list[str]:
    errors: list[str] = []
    nodes = atlas.get("nodes", [])
    edges = atlas.get("edges", [])
    motifs = atlas.get("motifs", [])
    evidence = atlas.get("evidence", [])
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
    for motif in motifs:
        for node_id in motif.get("nodes", []):
            if node_id not in ids:
                errors.append(f"motif {motif.get('id')} references unknown node: {node_id}")

    evidence_ids = [item.get("id") for item in evidence]
    for value in _dupes(evidence_ids):
        errors.append(f"duplicate evidence id: {value}")
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
        for field in ("metrics", "controls", "limitations"):
            if not isinstance(item.get(field, []), list):
                errors.append(f"evidence {evidence_id} has non-list {field}")
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
        f"{len(atlas['evidence'])} empirical evidence records)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
