from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class AnotherOddThingPassTests(unittest.TestCase):
    def test_pass_places_project_in_resident_intervention_learning_spine(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("another-odd-thing", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("AnotherOddThing", nodes)
        node = nodes["AnotherOddThing"]
        self.assertEqual(node["status"], "ledger")
        self.assertIn("resident", node["survived"].lower())
        self.assertIn("two-timescale", node["killed"].lower())

        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        for source in ("AnttisNeuron", "GrowingAnttisNeuron", "ActiveVectorNN", "FusionMachine"):
            self.assertIn((source, "AnotherOddThing", "converges"), edges)
            self.assertEqual(edges[(source, "AnotherOddThing", "converges")]["confidence"], "high")

    def test_pass_connects_recurring_mechanisms_without_inventing_ancestry(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        self.assertIn("resident-operator-addressed-intervention", motifs)
        self.assertIn("local-state-selects-update-regime", motifs)

        resident_nodes = set(motifs["resident-operator-addressed-intervention"]["nodes"])
        self.assertTrue({"AnotherOddThing", "GeometricNeuronV24", "ReadWrite", "ActiveVectorNN"}.issubset(resident_nodes))

        local_nodes = set(motifs["local-state-selects-update-regime"]["nodes"])
        self.assertTrue({"AnotherOddThing", "AnttisNeuron", "GrowingAnttisNeuron"}.issubset(local_nodes))

        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}
        self.assertNotIn(("ReadWrite", "AnotherOddThing", "inherits"), edges)
        self.assertNotIn(("GeometricNeuronV24", "AnotherOddThing", "inherits"), edges)


if __name__ == "__main__":
    unittest.main()
