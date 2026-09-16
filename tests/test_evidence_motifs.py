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

    def test_evidence_motif_relations_are_explicit_and_known(self):
        evidence = json.loads((ROOT / "data/evidence.json").read_text(encoding="utf-8"))
        motifs = json.loads((ROOT / "data/motifs.json").read_text(encoding="utf-8"))
        relations = json.loads((ROOT / "data/evidence_motif_relations.json").read_text(encoding="utf-8"))
        known = {item["id"] for item in motifs}
        tagged = 0
        for item in evidence:
            item_relations = relations.get(item["id"], {})
            for motif_id in item.get("motifs", []):
                self.assertIn(motif_id, known)
                self.assertIn(motif_id, item_relations)
                self.assertIn(item_relations[motif_id], {"supports", "limits", "documents"})
                tagged += 1
        self.assertGreaterEqual(tagged, len(evidence))

    def test_evidence_view_exposes_motif_aggregation(self):
        js = (ROOT / "assets/evidence.js").read_text(encoding="utf-8")
        self.assertIn("data/evidence_motif_relations.json", js)
        self.assertIn("function buildMotifEvidenceSummary", js)
        self.assertIn("function renderMotifEvidence", js)
        self.assertIn("function motifRelation", js)
        self.assertIn("motif evidence", js.lower())


if __name__ == "__main__":
    unittest.main()
