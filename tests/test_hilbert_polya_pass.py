from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


class HilbertPolyaPassTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)

    def test_pass_is_integrated_and_atlas_remains_valid(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertIn(
            "october-25-hilbert-polya-delay-network",
            {p["id"] for p in self.atlas["passes"]},
        )

    def test_card_keeps_unproved_operator_gap_visible(self):
        nodes = {n["id"]: n for n in self.atlas["nodes"]}
        paper = nodes["HilbertPolyaReintepretation"]
        self.assertEqual(paper["status"], "ledger")
        self.assertIn("self-adjoint", paper["killed"])
        self.assertIn("explicit-formula", paper["killed"])
        self.assertIn("June 2026", paper["era"])

    def test_links_are_conceptual_and_receipt_is_limited(self):
        edges = {
            (e["source"], e["target"], e["type"]): e
            for e in self.atlas["edges"]
        }
        for older in ("PrimeCrystalVST", "BirthOfClockfield"):
            self.assertIn(
                (older, "HilbertPolyaReintepretation", "converges"), edges
            )
        receipts = {e["id"]: e for e in self.atlas["evidence"]}
        receipt = receipts["hilbert-polya-truncated-poc-explicit-formula"]
        self.assertEqual(receipt["result"], "mixed")
        self.assertIn("not independently rerun", receipt["design"])


if __name__ == "__main__":
    unittest.main()
