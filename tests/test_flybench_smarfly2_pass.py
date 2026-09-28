import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


def test_artificial_ethology_pass_is_enabled_and_contains_both_repos():
    index = read("passes/index.json")
    assert any(row["path"] == "artificial-ethology-flybench.json" and row["enabled"] for row in index)

    payload = read("passes/artificial-ethology-flybench.json")
    nodes = {node["id"] for node in payload["nodes"]}
    assert {"Smarfly2", "FlyBench"} <= nodes

    edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
    assert ("ReturnToTimeWindow", "Smarfly2", "inherits") in edges


def test_recent_update_mentions_smarfly2_and_flybench():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "Smarfly2" in html
    assert "FlyBench" in html
