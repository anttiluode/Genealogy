from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class EvidenceLayerTests(unittest.TestCase):
    def test_evidence_is_loaded_and_references_curated_nodes(self):
        atlas = load_atlas(ROOT)
        self.assertIn("evidence", atlas)
        self.assertGreaterEqual(len(atlas["evidence"]), 3)
        node_ids = {node["id"] for node in atlas["nodes"]}
        evidence_ids = [item["id"] for item in atlas["evidence"]]
        self.assertEqual(len(evidence_ids), len(set(evidence_ids)))
        for item in atlas["evidence"]:
            self.assertIn(item["node"], node_ids)
            self.assertIn(item["result"], {"supports", "contradicts", "mixed", "inconclusive"})
            self.assertTrue(item["claim"])
            self.assertTrue(item["design"])
            self.assertTrue(item["source"])
            self.assertIsInstance(item.get("controls", []), list)
            self.assertIsInstance(item.get("limitations", []), list)

    def test_validator_accepts_repository_evidence_dataset(self):
        atlas = load_atlas(ROOT)
        self.assertEqual(validate_atlas(atlas), [])

    def test_static_atlas_exposes_evidence_view_and_node_evidence(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
        self.assertIn('data-view="evidence"', html)
        self.assertIn('id="evidence-content"', html)
        self.assertIn("data/evidence.json", js)
        self.assertIn("function renderEvidence", js)
        self.assertIn("Empirical evidence", js)
        self.assertIn("atlas.evidence", js)


if __name__ == "__main__":
    unittest.main()
