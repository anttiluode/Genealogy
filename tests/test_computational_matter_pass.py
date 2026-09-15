from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class ComputationalMatterPassTests(unittest.TestCase):
    def test_computational_matter_pass_keeps_mechanisms_separate(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("computational-matter", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "TheClutch",
            "Entrain",
            "BlockNeuron",
            "DifferentMachine",
            "Nollas",
            "Saturday",
        ):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }

        # Saturday is a consolidation node, not a fake chronological parent of Sunday.
        self.assertNotIn(("Saturday", "Sunday", "inherits"), edges)
        for source in ("Entrain", "BlockNeuron", "DifferentMachine", "Nollas"):
            self.assertEqual(
                edges[(source, "Saturday", "converges")]["confidence"],
                "high",
            )

        # Entrain explicitly imports the Clutch surprise gate.
        self.assertEqual(
            edges[("TheClutch", "Entrain", "inherits")]["confidence"],
            "high",
        )

        entrain = next(node for node in atlas["nodes"] if node["id"] == "Entrain")
        self.assertIn("0.974", entrain["survived"])
        self.assertIn("euler", entrain["killed"].lower())

        block = next(node for node in atlas["nodes"] if node["id"] == "BlockNeuron")
        self.assertIn("latch", block["killed"].lower())
        self.assertIn("persistent", block["survived"].lower())

        different = next(node for node in atlas["nodes"] if node["id"] == "DifferentMachine")
        self.assertIn("locally discoverable", different["survived"].lower())

        nollas = next(node for node in atlas["nodes"] if node["id"] == "Nollas")
        self.assertIn("transport", nollas["survived"].lower())
        self.assertIn("tolman", nollas["killed"].lower())

    def test_computational_matter_motif_names_distinct_storage_and_execution_layers(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["computational-matter-stack"]
        self.assertTrue(
            {"Entrain", "BlockNeuron", "DifferentMachine", "Nollas", "Saturday"}.issubset(
                set(motif["nodes"])
            )
        )


if __name__ == "__main__":
    unittest.main()
