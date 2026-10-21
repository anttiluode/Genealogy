"""October 21 Jäännös: preserve preregistered GPT-2 KILL and its narrow positive result."""
import json
from pathlib import Path
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]
PASS_ID = "october-21-jaannos-gpt2-residue-routing"
MOTIF = "oct21-jaannos-residue-is-not-decision-value"
EVIDENCE = {
    "oct21-jaannos-gpt2-band-reconstruction",
    "oct21-jaannos-gpt2-fixed-kill",
    "oct21-jaannos-local-beats-shuffle-not-fixed",
}


class JaannosGPT2GenealogyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = load_atlas(ROOT)
        cls.receipt = json.loads(
            (ROOT / "data/audits/jaannos-gpt2-2026-10-21.json").read_text(encoding="utf-8")
        )

    def test_genealogy_is_valid_and_repo_is_reviewed(self):
        self.assertEqual(validate_atlas(self.atlas), [])
        self.assertIn(PASS_ID, {p["id"] for p in self.atlas["passes"]})
        self.assertEqual([n["id"] for n in self.atlas["nodes"]
                          if n.get("pass_id") == PASS_ID], ["Jaannos"])
        inventory = [r for r in self.atlas["repos"] if r["name"] == "Jaannos"]
        self.assertEqual(len(inventory), 1)
        self.assertEqual(inventory[0]["inventory_status"], "reviewed")

    def test_receipt_really_is_full_real_gpt2_with_frozen_kill(self):
        receipt = self.receipt
        self.assertEqual(receipt["verdict"], "KILL")
        self.assertEqual(receipt["args"]["model"], "gpt2")
        self.assertFalse(receipt["args"]["smoke"])
        self.assertEqual(receipt["args"]["device"], "cuda")
        self.assertEqual(receipt["args"]["eval_seqs"], 16)
        self.assertEqual(receipt["args"]["seq_len"], 512)
        self.assertEqual(receipt["ranks"], [256] + [64] * 8)
        self.assertLess(receipt["max_recon_rel_err"], 1e-10)

    def test_both_negative_and_surviving_allocation_signals(self):
        table = self.receipt["table_top1_agreement"]
        for budget in ("0.6", "0.7", "0.8", "0.9"):
            self.assertGreater(table["fixed"][budget], table["local_sketch"][budget])
            self.assertGreater(table["fixed"][budget], table["local_exact"][budget])
            self.assertGreater(table["local_sketch"][budget], table["random_matched"][budget])
        node = next(n for n in self.atlas["nodes"] if n["id"] == "Jaannos")
        self.assertEqual(node["status"], "negative")
        self.assertIn("KILL", node["killed"])
        self.assertIn("outperform", node["killed"] + " outperform")
        self.assertIn("randomly", node["survived"])
        self.assertIn("not", node["killed"].lower())
        self.assertIn("speedup", node["killed"].lower())

    def test_evidence_and_conceptual_connections(self):
        evidence = {e["id"]: e for e in self.atlas["evidence"]}
        self.assertTrue(EVIDENCE.issubset(evidence))
        self.assertEqual(evidence["oct21-jaannos-gpt2-fixed-kill"]["result"],
                         "contradicts")
        for evid in EVIDENCE:
            self.assertEqual(evidence[evid]["node"], "Jaannos")
            self.assertIn("jaannos-gpt2-2026-10-21.json", evidence[evid]["source"])
        motifs = {m["id"]: m for m in self.atlas["motifs"]}
        self.assertIn(MOTIF, motifs)
        self.assertIn("Jaannos", motifs[MOTIF]["nodes"])
        edges = {(e["source"],e["target"],e["type"]) for e in self.atlas["edges"]}
        self.assertIn(("SihtiBrain", "Jaannos", "converges"),edges)
        self.assertIn(("GeometricNeuronV24","Jaannos","converges"),edges)


if __name__ == "__main__":
    unittest.main()
