from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class TemporalNeurobiologyPassTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.node_ids = {node["id"] for node in self.atlas["nodes"]}
        self.edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in self.atlas["edges"]}

    def test_recent_temporal_control_repos_are_on_the_wall(self):
        self.assertIn("temporal-control-neurobiology", {item["id"] for item in self.atlas["passes"]})
        for node_id in ("KolmeOvea", "FrequencyAndNeurons", "GATGRILS"):
            self.assertIn(node_id, self.node_ids)

    def test_kolmeovea_branches_to_clock_physics_and_learned_instrument(self):
        self.assertIn(("KolmeOvea", "FrequencyAndNeurons", "inherits"), self.edges)
        self.assertIn(("KolmeOvea", "GATGRILS", "converges"), self.edges)

    def test_frequency_question_stays_upstream_not_fake_gatgrils_ancestry(self):
        direct = {
            (edge["source"], edge["target"])
            for edge in self.atlas["edges"]
            if edge["source"] == "FrequencyAndNeurons" and edge["target"] == "GATGRILS"
        }
        self.assertEqual(direct, set())


if __name__ == "__main__":
    unittest.main()
