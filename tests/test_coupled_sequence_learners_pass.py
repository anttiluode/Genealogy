from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class CoupledSequenceLearnersPassTests(unittest.TestCase):
    def test_coupled_sequence_learners_is_on_wall_with_result_boundaries(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("CoupledSequenceLearners", nodes)

        node = nodes["CoupledSequenceLearners"]
        self.assertEqual(node["status"], "ledger")
        self.assertIn("+0.0662", node["killed"])
        self.assertIn("+0.10", node["killed"])
        self.assertIn("fresh listeners started 8/8", node["killed"].lower())
        self.assertIn("0.2388", node["survived"])

    def test_lineage_connects_predictive_and_communication_parents(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("PredictiveSusceptibility", "CoupledSequenceLearners", "extracts"), edges)
        self.assertIn(("The_Ping_And_The_Listener", "CoupledSequenceLearners", "corrects"), edges)
        self.assertIn(("KapeaKanava", "CoupledSequenceLearners", "inherits"), edges)

        for key in (
            ("PredictiveSusceptibility", "CoupledSequenceLearners", "extracts"),
            ("The_Ping_And_The_Listener", "CoupledSequenceLearners", "corrects"),
            ("KapeaKanava", "CoupledSequenceLearners", "inherits"),
        ):
            self.assertEqual(edges[key]["confidence"], "high")


if __name__ == "__main__":
    unittest.main()
