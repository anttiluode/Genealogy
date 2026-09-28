import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class FlyBenchSmarfly2PassTests(unittest.TestCase):
    def test_artificial_ethology_pass_is_enabled_and_contains_both_repos(self):
        index = read("passes/index.json")
        self.assertTrue(any(row["path"] == "artificial-ethology-flybench.json" and row["enabled"] for row in index))

        payload = read("passes/artificial-ethology-flybench.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertTrue({"Smarfly2", "FlyBench"} <= nodes)

        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("ReturnToTimeWindow", "Smarfly2", "inherits"), edges)

    def test_recent_update_mentions_smarfly2_and_flybench(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Smarfly2", html)
        self.assertIn("FlyBench", html)


if __name__ == "__main__":
    unittest.main()
