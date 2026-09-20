"""RegionalAttractorExplorer EEG curation."""

import unittest
from pathlib import Path

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class RegionalAttractorExplorerTests(unittest.TestCase):
    def test_regional_attractor_explorer_is_curated_as_eeg_ledger(self):
        atlas = load_atlas(ROOT)
        node = next(n for n in atlas["nodes"] if n["id"] == "RegionalAttractorExplorer")
        self.assertEqual(node["family"], "eeg-instruments")
        self.assertEqual(node["status"], "ledger")
        self.assertIn("PLV", node["killed"])
        self.assertIn("pilot-field", node["survived"].lower())

        repos = {r["name"]: r for r in atlas["repos"]}
        self.assertEqual(repos["RegionalAttractorExplorer"]["inventory_status"], "reviewed")

    def test_audit_evidence_is_on_negative_result_wall(self):
        atlas = load_atlas(ROOT)
        evidence = {e["id"]: e for e in atlas["evidence"]}
        self.assertEqual(evidence["regional-attractor-historical-plv-audit"]["result"], "contradicts")
        self.assertEqual(evidence["regional-attractor-p1-group-null"]["result"], "contradicts")

        motifs = {m["id"]: m for m in atlas["motifs"]}
        self.assertIn("RegionalAttractorExplorer", motifs["negative-results"]["nodes"])
        self.assertIn("RegionalAttractorExplorer", motifs["instrument-survives-interpretation"]["nodes"])


if __name__ == "__main__":
    unittest.main()
