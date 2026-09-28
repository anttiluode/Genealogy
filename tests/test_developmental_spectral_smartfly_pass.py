import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(path):
    return json.loads((DATA / path).read_text(encoding="utf-8"))


class DevelopmentalSpectralSmartflyPassTests(unittest.TestCase):
    def test_smartfly_is_explicit_parent_of_smarfly2(self):
        payload = read("passes/artificial-ethology-flybench.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertIn("Smartfly", nodes)

        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("Smartfly", "Smarfly2", "corrects"), edges)

    def test_developmental_spectral_neuron_pass_is_enabled_and_linked(self):
        index = read("passes/index.json")
        self.assertTrue(
            any(
                row["path"] == "developmental-spectral-neuron.json" and row["enabled"]
                for row in index
            )
        )

        payload = read("passes/developmental-spectral-neuron.json")
        nodes = {node["id"] for node in payload["nodes"]}
        self.assertIn("DevelopmentalSpectralNeuron", nodes)

        edges = {(edge["source"], edge["target"], edge["type"]) for edge in payload["edges"]}
        self.assertIn(("GrowingAnttisNeuron", "DevelopmentalSpectralNeuron", "converges"), edges)
        self.assertIn(("PhaseStigmergy", "DevelopmentalSpectralNeuron", "converges"), edges)

    def test_recent_update_mentions_developmental_spectral_neuron_and_smartfly(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("DevelopmentalSpectralNeuron", html)
        self.assertIn("Smartfly", html)


if __name__ == "__main__":
    unittest.main()
