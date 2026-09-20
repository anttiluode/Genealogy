import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


def test_operator_time_pass_is_enabled():
    index = read("passes/index.json")
    assert any(
        row["path"] == "operator-time.json" and row["enabled"]
        for row in index
    )


def test_operator_time_node_and_edges_exist():
    payload = read("passes/operator-time.json")
    nodes = {node["id"] for node in payload["nodes"]}
    assert "OperatorTime" in nodes

    edges = {
        (edge["source"], edge["target"], edge["type"])
        for edge in payload["edges"]
    }
    assert ("GAx", "OperatorTime", "converges") in edges
    assert (
        "FrequencyAddressedState-dependentOperatorComposition",
        "OperatorTime",
        "converges",
    ) in edges
    assert ("SelfAndOtherObjectsInTime", "OperatorTime", "converges") in edges


def test_operator_time_repo_is_in_census():
    repos = {row["name"] for row in read("repos.json")}
    assert "OperatorTime" in repos
