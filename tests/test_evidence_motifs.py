from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceMotifTests(unittest.TestCase):
    def test_evidence_ledger_has_broader_family_coverage(self):
        evidence = json.loads((ROOT / "data/evidence.json").read_text(encoding="utf-8"))
        nodes = {item["node"] for item in evidence}
        for node in ("GeometricNeuronV24", "ReadWrite", "LentoOrava", "WorldModel", "Operaattori", "PhaseStigmergy", "FusionMachine"):
            self.assertIn(node, nodes)
        self.assertGreaterEqual(len(evidence), 12)

    def test_evidence_view_exposes_motif_aggregation(self):
        js = (ROOT / "assets/evidence.js").read_text(encoding="utf-8")
        self.assertIn("function buildMotifEvidenceSummary", js)
        self.assertIn("function renderMotifEvidence", js)
        self.assertIn("motif evidence", js.lower())


if __name__ == "__main__":
    unittest.main()
