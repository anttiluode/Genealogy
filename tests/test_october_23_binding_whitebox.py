"""October 19 SihtiStack and October 23 Binding/WhiteBox curation integrity."""
import unittest
from pathlib import Path
from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
P19 = "october-19-sihtistack-return-channel"
P23 = "october-23-binding-sol-claude-whitebox"


class Oct23BindingWhiteBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = load_atlas(ROOT)
        cls.nodes = {n["id"]: n for n in cls.a["nodes"]}
        cls.evidence = {e["id"]: e for e in cls.a["evidence"]}

    def test_curated_cards_dates_and_census(self):
        self.assertEqual(validate_atlas(self.a), [])
        self.assertEqual({n["id"] for n in self.a["nodes"] if n.get("pass_id") == P19}, {"SihtiStack"})
        self.assertEqual({n["id"] for n in self.a["nodes"] if n.get("pass_id") == P23}, {"BindingClaude", "BindingSol", "WhiteBox"})
        self.assertEqual(self.nodes["SihtiStack"]["era_order"], 136)
        self.assertEqual({self.nodes[n]["era_order"] for n in ("BindingClaude", "BindingSol", "WhiteBox")}, {147, 148, 149})
        names = {"SihtiStack", "BindingClaude", "BindingSol", "WhiteBox"}
        inventory = {r["name"]: r for r in self.a["repos"] if r["name"] in names}
        self.assertEqual(set(inventory), names)
        self.assertTrue(all(r["inventory_status"] == "reviewed" for r in inventory.values()))
        self.assertTrue(all(self.nodes[n]["url"] == inventory[n]["url"] for n in names))

    def test_negative_gates_are_visible_not_overwritten(self):
        self.assertIn("2/12", self.nodes["SihtiStack"]["killed"])
        self.assertIn("SihtiBrain", self.nodes["SihtiStack"]["killed"])
        self.assertIn("1/10", self.nodes["BindingClaude"]["killed"])
        self.assertIn("2/5", self.nodes["BindingSol"]["killed"])
        self.assertIn("11/12", self.nodes["WhiteBox"]["killed"])
        self.assertEqual(self.nodes["BindingSol"]["status"], "negative")
        self.assertIn("clean", self.nodes["WhiteBox"]["survived"])

    def test_evidence_and_motifs(self):
        ids = [
            "oct19-sihtistack-instrument-local-tests",
            "oct19-sihtistack-real-qwen-return-negative",
            "oct23-bindingclaude-frozen-discovery-and-settling",
            "oct23-bindingclaude-adaptation-negative",
            "oct23-bindingsol-communication-gates-failed",
            "oct23-whitebox-exact-boolean-parity-translation",
            "oct23-whitebox-km-query-cost-caveat",
        ]
        self.assertTrue(all(i in self.evidence for i in ids))
        self.assertEqual(self.evidence[ids[1]]["result"], "contradicts")
        self.assertEqual(self.evidence[ids[3]]["result"], "contradicts")
        self.assertEqual(self.evidence[ids[4]]["result"], "mixed")
        self.assertEqual(self.evidence[ids[5]]["result"], "supports")
        self.assertIn("SihtiBrain", self.evidence[ids[1]]["source"])
        edges = {(e["source"], e["target"]) for e in self.a["edges"]}
        for pair in (("SihtiBrain", "SihtiStack"), ("ClaudeRepo1", "BindingClaude"), ("BindingClaude", "WhiteBox"), ("Valikasi", "BindingSol")):
            self.assertIn(pair, edges)

    def test_landing_and_notes(self):
        page = (ROOT / "README.md").read_text(encoding="utf8")
        for path in (
            "docs/reviews/2026-10-23-binding-whitebox.md",
            "data/passes/october-19-sihtistack-return-channel.json",
            "data/passes/october-23-binding-and-whitebox.json",
        ):
            self.assertIn(path, page)
            self.assertTrue((ROOT / path).exists())


if __name__ == "__main__":
    unittest.main()
