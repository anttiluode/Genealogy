from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-17-sihti-image-model2"
EVIDENCE = (
    "oct17-sim2-real-layout-ridge-fill",
    "oct17-sim2-global-layout-frozen-gates",
    "oct17-sim2-stochastic-texture-followup",
)


class SihtiImageModel2PassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_atlas_valid(self):
        self.assertEqual(validate_atlas(self.atlas), [])

    def test_successor_has_one_node_and_is_reviewed(self):
        node = [n for n in self.atlas["nodes"] if n["id"] == "SihtiImageModel2"]
        self.assertEqual(len(node), 1)
        self.assertEqual(node[0]["pass_id"], PASS_ID)
        inventory = {r["name"]: r for r in self.atlas["repos"]}
        self.assertEqual(inventory["SihtiImageModel2"]["inventory_status"], "reviewed")
        self.assertIn("G1", node[0]["killed"])
        self.assertIn("JPEG", node[0]["killed"])

    def test_lineage_is_explicit_inheritance_not_inferred_unification(self):
        edges = [e for e in self.atlas["edges"] if e["target"] == "SihtiImageModel2"]
        self.assertEqual(len(edges), 1)
        self.assertEqual((edges[0]["source"], edges[0]["type"]), ("SihtiImageModel", "inherits"))

    def test_all_evidence_is_auditable_and_keeps_failed_gates(self):
        evidence = {r["id"]: r for r in self.atlas["evidence"]}
        for evidence_id in EVIDENCE:
            self.assertIn(evidence_id, evidence)
            self.assertTrue(evidence[evidence_id]["controls"])
            self.assertTrue(evidence[evidence_id]["limitations"])
            self.assertIn("363b1dda2073868f93d9687818c2cf1c0337031e", evidence[evidence_id]["source"])
        main = evidence[EVIDENCE[1]]
        self.assertIn("G1 failed", main["limitations"][0])
        stochastic = evidence[EVIDENCE[2]]
        self.assertTrue(any("fails" in entry.lower() for entry in stochastic["limitations"]))

    def test_question_remains_open_and_limited(self):
        question = {q["id"]: q for q in self.atlas["questions"]}["oct17-learned-layout-vs-coherent-detail"]
        self.assertEqual(question["state"], "open")
        self.assertEqual(set(question["evidence"]), set(EVIDENCE))


if __name__ == "__main__":
    unittest.main()
