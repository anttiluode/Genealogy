from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class EatonPassTests(unittest.TestCase):
    def test_eaton_is_cataloged_as_a_bounded_gating_demonstration(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("eaton", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        self.assertIn("EATON", nodes)
        node = nodes["EATON"]
        self.assertEqual(node["status"], "ledger")
        self.assertEqual(node["usefulness"], "scientific")
        self.assertIn("1.000", node["survived"])
        self.assertIn("0.500", node["survived"])
        self.assertIn("analyt", node["killed"].lower())
        self.assertIn("gating", node["tags"])

    def test_eaton_links_resident_state_to_aoc_without_overclaiming(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("OperatorTime", "EATON", "converges"), edges)
        self.assertIn(("AdaptiveObserverCache", "EATON", "converges"), edges)
        self.assertIn(("ActiveVectorNN", "EATON", "converges"), edges)

        motif = {item["id"]: item for item in atlas["motifs"]}["transient-operator-handoff"]
        self.assertIn("EATON", motif["nodes"])
        self.assertIn("AdaptiveObserverCache", motif["nodes"])

    def test_eaton_evidence_keeps_the_claim_boundary_visible(self):
        atlas = load_atlas(ROOT)
        evidence = {item["id"]: item for item in atlas["evidence"]}
        self.assertIn("eaton-v0-gating-demo", evidence)
        item = evidence["eaton-v0-gating-demo"]
        self.assertEqual(item["result"], "supports")
        joined_limits = " ".join(item["limitations"]).lower()
        self.assertIn("analytic", joined_limits)
        self.assertIn("lstm", joined_limits)
        self.assertIn("qwen", joined_limits)


if __name__ == "__main__":
    unittest.main()
