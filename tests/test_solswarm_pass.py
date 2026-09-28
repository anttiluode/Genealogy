import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class SolSwarmPassTests(unittest.TestCase):
    def test_pass_is_enabled_and_contains_repo(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "solswarm.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/solswarm.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertIn("SolSwarm", nodes)

    def test_operator_sampling_lineage_and_negative_boundary_are_explicit(self):
        payload = read("passes/solswarm.json")
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("BiomorphicSwarm", "SolSwarm", "extracts"), edges)
        self.assertIn(("GAx", "SolSwarm", "converges"), edges)
        self.assertIn(("OperatorTime", "SolSwarm", "converges"), edges)

        node = next(node for node in payload["nodes"] if node["id"] == "SolSwarm")
        self.assertIn("1.0723", node["survived"])
        self.assertIn("2.25", node["survived"])
        self.assertIn("does not beat uniform", node["killed"].lower())
        self.assertIn("7.49", node["killed"])
        self.assertIn("3.25", node["killed"])

    def test_recent_update_mentions_repo(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("SolSwarm", html)


if __name__ == "__main__":
    unittest.main()
