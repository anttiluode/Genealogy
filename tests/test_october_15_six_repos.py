from pathlib import Path
import unittest
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS = "october-15-grown-operators-symmetry-and-writer-controls"
NAMES = ("SilliSalaatti", "Noether-Ledger", "SymmetrySihti", "Unruh", "GrowingMatrix", "Limasieni")
EVIDENCE = ("oct15-silli-frozen-reader-writer-ablation", "oct15-noether-discrete-gauge-identity", "oct15-symmetry-sihti-projectors-and-currents", "oct15-unruh-driven-slow-closure", "oct15-growingmatrix-routing-and-material", "oct15-growingmatrix-planar-attention-limit", "oct15-limasieni-two-port-expressivity", "oct15-limasieni-content-biased-recall",)

class OctoberFifteenLineageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)

    def test_full_atlas_valid(self):
        self.assertEqual([], validate_atlas(self.atlas))

    def test_six_missing_repos_now_have_unique_reviewed_nodes(self):
        nodes = self.atlas["nodes"]
        repos = {r["name"]:r for r in self.atlas["repos"]}
        ids = [n["id"] for n in nodes]
        for name in NAMES:
            self.assertEqual(ids.count(name), 1, name)
            self.assertEqual(next(n for n in nodes if n["id"] == name)["pass_id"], PASS)
            self.assertEqual(repos[name]["inventory_status"], "reviewed")
            self.assertEqual(repos[name]["url"], f"https://github.com/anttiluode/{name}")

    def test_distinct_scientific_lines_and_direct_links(self):
        motifs = {m["id"]:set(m["nodes"]) for m in self.atlas["motifs"]}
        self.assertTrue({"Limasieni", "GrowingMatrix"}.issubset(motifs["oct15-input-output-geometry"]))
        self.assertTrue({"SymmetrySihti", "Noether-Ledger"}.issubset(motifs["oct15-symmetry-conserved-ledgers"]))
        self.assertIn("SilliSalaatti", motifs["oct15-writer-calibration-and-budget"])
        edges = {(x["source"],x["target"]) for x in self.atlas["edges"]}
        for pair in (("Unruh","GrowingMatrix"),("Limasieni","GrowingMatrix"),
                     ("Noether-Ledger","SymmetrySihti"),("PhaseGraphFastWeightCell","SilliSalaatti")):
            self.assertIn(pair,edges)

    def test_evidence_candidly_preserves_negative_results(self):
        evidence = {e["id"]:e for e in self.atlas["evidence"]}
        nodes = {n["id"]:n for n in self.atlas["nodes"]}
        for identifier in EVIDENCE:
            self.assertIn(identifier, evidence)
            e = evidence[identifier]
            self.assertTrue(e["metrics"])
            self.assertTrue(e["controls"])
            self.assertTrue(e["limitations"])
            self.assertEqual(set(e["motifs"]),set(self.atlas["evidence_motif_relations"][identifier]))
        self.assertIn("No replacement passes",nodes["SilliSalaatti"]["killed"])
        self.assertIn("far from zero-KL",nodes["GrowingMatrix"]["killed"])
        self.assertIn("end-to-end backprop",nodes["Limasieni"]["killed"])

    def test_question_has_matched_cost_discriminator(self):
        q = next(x for x in self.atlas["questions"] if x["id"] == "oct15-spatial-growth-to-content-conditioned-operator")
        self.assertEqual(q["state"],"open")
        self.assertIn("QK",q["missing_discriminator"])
        self.assertGreaterEqual(len(q["competing_explanations"]),2)

if __name__ == "__main__":
    unittest.main()
