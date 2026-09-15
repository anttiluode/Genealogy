from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class MoireAppliedPassTests(unittest.TestCase):
    def test_moire_applied_pass_separates_working_artifact_from_dead_claims(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("moire-applied", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in ("moire-neural-network", "One_formula_three_domains", "MoireFormer"):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        edge = edges[("Geometric-Neuron", "MoireFormer", "extracts")]
        self.assertEqual(edge["confidence"], "high")
        self.assertIn(("Geometric-Neuron", "One_formula_three_domains", "extracts"), edges)

        early = next(node for node in atlas["nodes"] if node["id"] == "moire-neural-network")
        killed = early["killed"].lower()
        self.assertIn("restart", killed)
        self.assertIn("must oscillate", killed)

        synthesis = next(node for node in atlas["nodes"] if node["id"] == "One_formula_three_domains")
        self.assertIn("no-probe", synthesis["killed"].lower())
        self.assertIn("4%", synthesis["killed"])

        model = next(node for node in atlas["nodes"] if node["id"] == "MoireFormer")
        self.assertIn("137.9m", model["survived"].lower())
        self.assertIn("superiority", model["killed"].lower())

    def test_one_formula_is_a_synthesis_not_three_independent_proofs(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["one-formula-three-fates"]
        self.assertTrue(
            {"One_formula_three_domains", "Geometric-Neuron", "MoireFormer"}.issubset(
                set(motif["nodes"])
            )
        )


if __name__ == "__main__":
    unittest.main()
