import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


def test_current_temporal_self_pass_is_enabled_and_connected():
    index = read("passes/index.json")
    assert any(row["path"] == "self-and-other-in-time.json" and row["enabled"] for row in index)

    payload = read("passes/self-and-other-in-time.json")
    nodes = {node["id"] for node in payload["nodes"]}
    assert "SelfAndOtherObjectsInTime" in nodes

    edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
    assert ("AnotherOddThing", "SelfAndOtherObjectsInTime", "converges") in edges
    assert ("ReadWrite", "SelfAndOtherObjectsInTime", "converges") in edges
    assert ("ArtificialCortex", "SelfAndOtherObjectsInTime", "converges") in edges


def test_v20_exposes_whorl_curation_provenance():
    payload = read("passes/geometric-ladder.json")
    node = next(node for node in payload["nodes"] if node["id"] == "GeometricNeuron_V20")
    assert "whorl_field.py" in node["survived"]
    assert "ArtificialCortex/the_whorl" in node["survived"]

    edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
    assert ("ArtificialCortex", "GeometricNeuron_V20", "extracts") in edges


def test_recent_repos_are_in_census():
    repos = {row["name"] for row in read("repos.json")}
    assert "WhatToLookAt" in repos
    assert "SelfAndOtherObjectsInTime" in repos
