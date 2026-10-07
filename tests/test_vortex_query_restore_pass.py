from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class VortexQueryRestorePassTests(unittest.TestCase):
    def setUp(self):
        self.atlas = load_atlas(ROOT)
        self.node_ids = {node["id"] for node in self.atlas["nodes"]}
        self.edges = {(edge["source"], edge["target"], edge["type"]): edge for edge in self.atlas["edges"]}
        self.evidence_ids = {item["id"] for item in self.atlas["evidence"]}

    def test_vmn_line_is_on_the_wall(self):
        self.assertIn("vortex-query-restore", {item["id"] for item in self.atlas["passes"]})
        for node_id in ("VMN", "VMNClaude", "Vision"):
            self.assertIn(node_id, self.node_ids)

    def test_response_operator_and_vision_links_are_explicit(self):
        self.assertIn(("Kompressori", "VMN", "converges"), self.edges)
        self.assertIn(("Kompressori", "VMNClaude", "converges"), self.edges)
        self.assertIn(("VMNClaude", "Vision", "extracts"), self.edges)
        self.assertIn(("Tupsu", "Vision", "corrects"), self.edges)

    def test_measured_results_are_in_evidence_view(self):
        for evidence_id in (
            "vmn-state-code-and-memory-gate",
            "vmn-query-restore",
            "vmnclaude-query-line",
            "vision-eraser-gate",
        ):
            self.assertIn(evidence_id, self.evidence_ids)


if __name__ == "__main__":
    unittest.main()
