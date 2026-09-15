from __future__ import annotations

import json
import sys
from pathlib import Path

KNOWN_STATUSES = {"idea-mine", "experiment", "negative", "ledger", "tool", "survivor", "active"}
KNOWN_USEFULNESS = {"none", "conceptual", "scientific", "practical"}
KNOWN_CONFIDENCE = {"low", "medium", "high"}
KNOWN_EDGE_TYPES = {"inherits", "forks", "rediscovery", "corrects", "extracts", "converges"}


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_atlas(root: Path) -> dict[str, list[dict]]:
    data = root / "data"
    return {
        "repos": _read_json(data / "repos.json"),
        "nodes": _read_json(data / "nodes.json"),
        "edges": _read_json(data / "edges.json"),
        "motifs": _read_json(data / "motifs.json"),
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
    repos = atlas.get("repos", [])

    node_ids = [node.get("id") for node in nodes]
    for value in _dupes(node_ids):
        errors.append(f"duplicate node id: {value}")
    ids = set(node_ids)

    for node in nodes:
        node_id = node.get("id", "<missing>")
        if node.get("status") not in KNOWN_STATUSES:
            errors.append(f"unknown status for {node_id}: {node.get('status')}")
        if node.get("usefulness") not in KNOWN_USEFULNESS:
            errors.append(f"unknown usefulness for {node_id}: {node.get('usefulness')}")
        if node.get("confidence") not in KNOWN_CONFIDENCE:
            errors.append(f"unknown confidence for {node_id}: {node.get('confidence')}")

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
    for value in _dupes(edge_keys):
        errors.append(f"duplicate edge: {value}")

    for motif in motifs:
        for node_id in motif.get("nodes", []):
            if node_id not in ids:
                errors.append(f"motif {motif.get('id')} references unknown node: {node_id}")

    repo_names = [repo.get("name") for repo in repos]
    for value in _dupes(repo_names):
        errors.append(f"duplicate repository name: {value}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_atlas(load_atlas(root))
    if errors:
        for error in errors:
            print(error)
        return 1
    print("atlas data: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
