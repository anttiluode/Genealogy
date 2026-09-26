from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class PredictiveSusceptibilitySynthesisPassTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.node_ids = {node["id"] for node in self.atlas["nodes"]}
        self.nodes = {node["id"]: node for node in self.atlas["nodes"]}
        self.edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in self.atlas["edges"]
        }

    def test_synthesis_repos_are_on_the_wall(self):
        self.assertIn(
            "predictive-susceptibility-synthesis",
            {item["id"] for item in self.atlas["passes"]},
        )
        for node_id in ("The_Ping_And_The_Listener", "PredictiveSusceptibility"):
            self.assertIn(node_id, self.node_ids)

    def test_lineage_runs_from_experiments_to_ping_to_predictive_susceptibility(self):
        for source in ("ResonaattoriAivo", "FridayRepo", "KapeaKanava"):
            self.assertIn((source, "The_Ping_And_The_Listener", "extracts"), self.edges)
        self.assertIn(
            ("The_Ping_And_The_Listener", "PredictiveSusceptibility", "inherits"),
            self.edges,
        )

    def test_predictive_susceptibility_is_also_a_practical_probe(self):
        node = self.nodes["PredictiveSusceptibility"]
        self.assertEqual(node["status"], "tool")
        self.assertEqual(node["usefulness"], "practical")
        self.assertIn("susceptibility_probe.py", node["survived"])
        self.assertIn("constructed", node["killed"].lower())


if __name__ == "__main__":
    unittest.main()
