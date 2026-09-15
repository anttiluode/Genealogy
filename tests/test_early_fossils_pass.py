from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class EarlyFossilsPassTests(unittest.TestCase):
    def test_early_fossils_preserve_question_implementation_mismatch(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("early-adaptive-fossils", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        fossils = {
            "FractalBrain",
            "buginthemachine",
            "FractalBug",
            "TiniOnes",
            "MoireBrain",
            "FieldLatentBridge",
            "weirdfieldthingy",
            "Little_dude",
        }
        self.assertTrue(fossils.issubset(ids))

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        # Saturday's archive map explicitly audits these older receipts; this is
        # convergence/correction, not invented chronological inheritance.
        for source in fossils:
            matching = [
                edge for key, edge in edges.items()
                if key[0] == source and key[1] == "Saturday"
            ]
            self.assertTrue(matching, source)
            self.assertTrue(all(edge["confidence"] == "high" for edge in matching))

        little = next(node for node in atlas["nodes"] if node["id"] == "Little_dude")
        self.assertIn("parallel", little["survived"].lower())
        self.assertIn("dendritic", little["killed"].lower())

        bridge = next(node for node in atlas["nodes"] if node["id"] == "FieldLatentBridge")
        self.assertIn("fresh random", bridge["killed"].lower())

        brain = next(node for node in atlas["nodes"] if node["id"] == "FractalBrain")
        self.assertIn("hype", brain["killed"].lower())

    def test_closed_loop_creature_motif_keeps_embodiment_residue(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["closed-loop-creature"]
        self.assertTrue(
            {"buginthemachine", "FractalBug", "TiniOnes"}.issubset(set(motif["nodes"]))
        )

    def test_ai_projection_fossil_motif_marks_named_mechanisms_that_were_not_built(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["ai-projection-fossil"]
        self.assertTrue(
            {"FractalBrain", "FieldLatentBridge", "Little_dude"}.issubset(set(motif["nodes"]))
        )


if __name__ == "__main__":
    unittest.main()
