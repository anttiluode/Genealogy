import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class GeometricNeuronSapolskyFractalPassTests(unittest.TestCase):
    def test_pass_is_enabled_and_contains_repo(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "geometric-neuron-sapolsky-fractal.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/geometric-neuron-sapolsky-fractal.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertIn("GeometricNeuronAndSapolskysFractal", nodes)

    def test_lineage_keeps_skew_and_reversal_sources_explicit(self):
        payload = read("passes/geometric-neuron-sapolsky-fractal.json")
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("GeometricNeuronV9", "GeometricNeuronAndSapolskysFractal", "inherits"), edges)
        self.assertIn(("AgainstTheGrain", "GeometricNeuronAndSapolskysFractal", "converges"), edges)

    def test_recent_update_mentions_repo(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("GeometricNeuronAndSapolskysFractal", html)


if __name__ == "__main__":
    unittest.main()
