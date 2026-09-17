from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class NSSN2PassTests(unittest.TestCase):
    def test_nssn2_is_a_curated_developmental_turning_point(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}

        self.assertIn("NSSN2", nodes)
        node = nodes["NSSN2"]
        self.assertEqual(node["status"], "ledger")
        self.assertIn("development", node["tags"])
        self.assertIn("negative-result", node["tags"])
        self.assertIn("prediction", node["claim"].lower())
        self.assertIn("frozen", node["killed"].lower())

    def test_nssn2_extends_not_so_simple_neuron_into_development(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}

        self.assertIn(("NotSoSimpleNeuron", "NSSN2", "extends"), edges)

    def test_nssn2_pass_is_first_class(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("nssn2-development", pass_ids)


if __name__ == "__main__":
    unittest.main()
