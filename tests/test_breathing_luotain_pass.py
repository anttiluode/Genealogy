import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class BreathingLuotainPassTests(unittest.TestCase):
    def test_pass_is_enabled_and_contains_all_three_repositories(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "breathing-luotain.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/breathing-luotain.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertEqual(
            {"Breathing-Qwen", "Breathing-QwenClaude", "Luotain"},
            nodes,
        )

    def test_negative_boundaries_and_surviving_results_are_preserved(self):
        payload = read("passes/breathing-luotain.json")
        nodes = {node["id"]: node for node in payload["nodes"]}

        breathing = nodes["Breathing-Qwen"]
        self.assertIn("93.75%", breathing["survived"])
        self.assertIn("Gate 1C", breathing["killed"])
        self.assertIn("not run", breathing["killed"].lower())
        self.assertIn("temperature", breathing["killed"].lower())

        claude = nodes["Breathing-QwenClaude"]
        self.assertIn("75%", claude["survived"])
        self.assertIn("did not beat", claude["killed"].lower())
        self.assertIn("72%", claude["killed"])

        luotain = nodes["Luotain"]
        self.assertIn("99.53%", luotain["survived"])
        self.assertIn("9,086", luotain["survived"])
        self.assertIn("1,278", luotain["killed"])

    def test_lineage_distinguishes_convergence_from_ancestry(self):
        payload = read("passes/breathing-luotain.json")
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("AdaptiveObserverCache", "Breathing-Qwen", "converges"), edges)
        self.assertIn(("Breathing-Qwen", "Breathing-QwenClaude", "converges"), edges)
        self.assertIn(("ReadWrite", "Luotain", "converges"), edges)

    def test_recent_update_mentions_all_three(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Breathing-Qwen", html)
        self.assertIn("Breathing-QwenClaude", html)
        self.assertIn("Luotain", html)


if __name__ == "__main__":
    unittest.main()
