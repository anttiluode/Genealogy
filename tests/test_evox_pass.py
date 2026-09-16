from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class EvoXPassTests(unittest.TestCase):
    def test_evox_is_cataloged_with_its_two_source_lines(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("evox", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("EvoX", nodes)
        node = nodes["EvoX"]
        self.assertEqual(node["status"], "ledger")
        self.assertEqual(node["usefulness"], "scientific")
        self.assertIn("active", node["survived"].lower())
        self.assertIn("4/5", node["survived"])

        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("GAx", "EvoX", "converges"), edges)
        self.assertIn(("AnotherOddThing", "EvoX", "converges"), edges)

    def test_evox_records_the_canonical_limit_without_overclaiming(self):
        atlas = load_atlas(ROOT)
        node = {node["id"]: node for node in atlas["nodes"]}["EvoX"]
        self.assertIn("causal", node["killed"].lower())
        self.assertIn("not", node["killed"].lower())
        self.assertIn("active-probing", node["tags"])
        self.assertIn("mechanism-selection", node["tags"])


if __name__ == "__main__":
    unittest.main()
