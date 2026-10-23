"""October 23 Confusing Friday: missing image and creative cards stay honest."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
P = "october-23-confusing-friday-image-and-ghost"

class ConfusingFridayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = load_atlas(ROOT)
        cls.nodes = {n["id"]: n for n in cls.a["nodes"]}
        cls.evidence = {e["id"]: e for e in cls.a["evidence"]}

    def test_cards_census_and_validation(self):
        self.assertEqual(validate_atlas(self.a), [])
        self.assertEqual(
            {n["id"] for n in self.a["nodes"] if n.get("pass_id") == P},
            {"SihtiGraphModel", "DoDis", "GhostYou"},
        )
        names = {"SihtiGraphModel", "DoDis", "GhostYou", "WhiteBox", "BindingClaude", "BindingSol"}
        inventory = {r["name"]: r for r in self.a["repos"] if r["name"] in names}
        self.assertEqual(set(inventory), names)
        self.assertTrue(all(v["inventory_status"] == "reviewed" for v in inventory.values()))
        self.assertEqual(self.nodes["GhostYou"]["usefulness"], "practical")
        self.assertEqual({self.nodes[n]["era_order"] for n in ("SihtiGraphModel", "DoDis", "GhostYou")}, {150, 151, 152})

    def test_negative_controls_and_uncertainty_preserved(self):
        self.assertIn("-3.035", self.nodes["SihtiGraphModel"]["killed"])
        self.assertIn("0 shared tiles", self.nodes["SihtiGraphModel"]["killed"])
        self.assertIn("0.01438", self.nodes["DoDis"]["killed"])
        self.assertIn("not independently parsed", self.nodes["DoDis"]["killed"])
        self.assertIn("not evidence", self.nodes["GhostYou"]["killed"])
        self.assertEqual(self.evidence["oct23-dodis-v2-visible-local-address-awaits-outcome-audit"]["result"], "inconclusive")
        self.assertEqual(self.evidence["oct23-ghostyou-finished-webcam-toy"]["result"], "inconclusive")

    def test_edges_evidence_and_follow_up(self):
        edges = {(e["source"], e["target"], e["type"]) for e in self.a["edges"]}
        for pair in (("SihtiGraphModel","DoDis","inherits"),("WhiteBox","SihtiGraphModel","converges"),("SihtiImageModel","DoDis","converges")):
            self.assertIn(pair,edges)
        self.assertTrue(all(eid in self.evidence for eid in (
            "oct23-sihtigraphmodel-retention-dependent-surrogate",
            "oct23-sihtigraphmodel-v1-v2-limit",
            "oct23-dodis-first-bird-completion-and-shuffle",
            "oct23-dodis-v2-visible-local-address-awaits-outcome-audit",
            "oct23-ghostyou-finished-webcam-toy",
        )))
        self.assertIn("oct23-local-visible-context-as-content-address", {q["id"] for q in self.a["questions"]})
        for path in ("docs/reviews/2026-10-23-confusing-friday.md", "data/passes/october-23-confusing-friday.json"):
            self.assertTrue((ROOT/path).is_file())
            self.assertIn(path, (ROOT/"README.md").read_text(encoding="utf8"))
        self.assertIn("Confusing Friday", (ROOT/"README.md").read_text(encoding="utf8"))

if __name__ == "__main__":
    unittest.main()
