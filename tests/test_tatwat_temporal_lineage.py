from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class TATWATASTemporalLineageTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.nodes = {node["id"]: node for node in self.atlas["nodes"]}
        self.edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in self.atlas["edges"]
        }

    def test_tatwatasw_is_on_the_temporal_control_wall(self):
        self.assertIn("TATWATASW", self.nodes)
        node = self.nodes["TATWATASW"]
        self.assertIn("predictive field", node["claim"].lower())
        self.assertIn("dead time", node["survived"].lower())

    def test_plateau_only_sequence_claim_stays_negative(self):
        node = self.nodes["TATWATASW"]
        killed = node["killed"].lower()
        self.assertIn("plateau", killed)
        self.assertTrue("does not" in killed or "did not" in killed)
        self.assertTrue("sequence" in killed or "directional chain" in killed)

    def test_tatwatasw_connects_the_three_immediate_parent_questions(self):
        for source, edge_type in (
            ("FrequencyAndNeurons", "inherits"),
            ("KolmeOvea", "converges"),
            ("GATGRILS", "converges"),
        ):
            self.assertIn((source, "TATWATASW", edge_type), self.edges)


if __name__ == "__main__":
    unittest.main()
