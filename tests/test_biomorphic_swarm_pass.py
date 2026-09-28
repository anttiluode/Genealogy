import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class BiomorphicSwarmPassTests(unittest.TestCase):
    def test_pass_is_enabled_and_contains_repo(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "biomorphic-swarm.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/biomorphic-swarm.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertIn("BiomorphicSwarm", nodes)

    def test_lineage_and_sampling_boundary_are_explicit(self):
        payload = read("passes/biomorphic-swarm.json")
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("CabbageFarm", "BiomorphicSwarm", "inherits"), edges)
        self.assertIn(("WhatToLookAt", "BiomorphicSwarm", "converges"), edges)

        node = next(node for node in payload["nodes"] if node["id"] == "BiomorphicSwarm")
        self.assertIn("random placement", node["killed"].lower())
        self.assertIn("0.008", node["killed"])

    def test_recent_update_mentions_repo(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("BiomorphicSwarm", html)


if __name__ == "__main__":
    unittest.main()
