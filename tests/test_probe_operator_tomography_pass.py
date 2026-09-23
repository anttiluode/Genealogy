from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class ProbeOperatorTomographyPassTests(unittest.TestCase):
    def test_pass_adds_the_probe_to_operator_line(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("probe-operator-tomography", pass_ids)

        nodes = {node["id"]: node for node in atlas["nodes"]}
        for node_id in (
            "HeadAsResonator",
            "SilentPing",
            "PingToWord",
            "ResidentOperatorTomography",
        ):
            self.assertIn(node_id, nodes)

        self.assertEqual(nodes["SilentPing"]["status"], "ledger")
        self.assertIn("transplant", nodes["SilentPing"]["survived"].lower())
        self.assertIn("known-answer", nodes["SilentPing"]["killed"].lower())

        self.assertEqual(nodes["PingToWord"]["status"], "ledger")
        self.assertIn("source", nodes["PingToWord"]["survived"].lower())
        self.assertIn("gauge", nodes["PingToWord"]["killed"].lower())

        self.assertEqual(nodes["ResidentOperatorTomography"]["status"], "ledger")
        self.assertIn("gauge", nodes["ResidentOperatorTomography"]["survived"].lower())
        self.assertIn("toy", nodes["ResidentOperatorTomography"]["killed"].lower())

    def test_line_connects_old_probe_work_to_gauge_aware_tomography(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in atlas["edges"]}
        self.assertIn(("HeadAsResonator", "PingToWord", "converges"), edges)
        self.assertIn(("ReadWrite", "SilentPing", "converges"), edges)
        self.assertIn(("OperatorTime", "SilentPing", "converges"), edges)
        self.assertIn(("EATON", "ResidentOperatorTomography", "converges"), edges)
        self.assertIn(("PingToWord", "ResidentOperatorTomography", "converges"), edges)

        motif = {item["id"]: item for item in atlas["motifs"]}["probe-defined-operator-coordinate"]
        for node_id in (
            "HeadAsResonator",
            "ReadWrite",
            "SilentPing",
            "PingToWord",
            "EATON",
            "OperatorTime",
            "ResidentOperatorTomography",
        ):
            self.assertIn(node_id, motif["nodes"])

    def test_frozen_results_are_in_the_evidence_ledger(self):
        atlas = load_atlas(ROOT)
        evidence = {item["id"]: item for item in atlas["evidence"]}
        for evidence_id in (
            "silent-ping-v0",
            "ping-to-word-v0",
            "resident-operator-tomography-v0",
        ):
            self.assertIn(evidence_id, evidence)
            self.assertIn("probe-defined-operator-coordinate", evidence[evidence_id]["motifs"])

        silent = evidence["silent-ping-v0"]
        self.assertEqual(silent["result"], "supports")
        self.assertIn("transplant", " ".join(silent["controls"]).lower())

        word = evidence["ping-to-word-v0"]
        self.assertEqual(word["result"], "supports")
        self.assertIn("classical", " ".join(word["limitations"]).lower())

        rot = evidence["resident-operator-tomography-v0"]
        self.assertEqual(rot["result"], "supports")
        self.assertIn("gauge", rot["claim"].lower())
        self.assertIn("toy", " ".join(rot["limitations"]).lower())


if __name__ == "__main__":
    unittest.main()
