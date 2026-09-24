from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class RytmiTransformerToXLineageTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.nodes = {node["id"]: node for node in self.atlas["nodes"]}
        self.edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in self.atlas["edges"]
        }

    def test_rytmi_is_on_the_temporal_control_wall(self):
        self.assertIn("Rytmi", self.nodes)
        node = self.nodes["Rytmi"]
        survived = node["survived"].lower()
        killed = node["killed"].lower()
        self.assertIn("80", survived)
        self.assertIn("dead time", survived)
        self.assertIn("one-shot", killed)
        self.assertTrue("not" in killed or "has not" in killed)
        self.assertIn("plateau", killed)

    def test_transformertox_is_on_the_temporal_control_wall(self):
        self.assertIn("TransformerToX", self.nodes)
        node = self.nodes["TransformerToX"]
        claim = node["claim"].lower()
        survived = node["survived"].lower()
        killed = node["killed"].lower()
        self.assertIn("address", claim)
        self.assertIn("write", claim)
        self.assertIn("zero", survived)
        self.assertIn("gate 1", killed)
        self.assertIn("not", killed)
        self.assertIn("static", killed)

    def test_rytmi_inherits_tatwatasw_and_converges_with_anotheroddthing(self):
        self.assertIn(("TATWATASW", "Rytmi", "inherits"), self.edges)
        self.assertIn(("AnotherOddThing", "Rytmi", "converges"), self.edges)

    def test_transformertox_has_bounded_temporal_translation_edges(self):
        self.assertIn(("TATWATASW", "TransformerToX", "converges"), self.edges)
        self.assertIn(("AnotherOddThing", "TransformerToX", "converges"), self.edges)


if __name__ == "__main__":
    unittest.main()
