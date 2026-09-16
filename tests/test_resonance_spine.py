from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class ResonanceSpineTests(unittest.TestCase):
    def test_missing_resonance_repos_are_curated(self):
        atlas = load_atlas(ROOT)
        nodes = {node["id"]: node for node in atlas["nodes"]}
        expected = {
            "HeadAsResonator",
            "HeadAsResonator2",
            "SpectralArchipelagoModelOfBrain",
            "SpectralIslandsV2",
            "SpectralIslandsV3",
            "SpectralNeuron",
        }
        self.assertTrue(expected.issubset(nodes))

        self.assertIn("0.954", nodes["HeadAsResonator"]["survived"])
        self.assertIn("transfer", nodes["HeadAsResonator"]["claim"].lower())
        self.assertIn("not", nodes["HeadAsResonator2"]["killed"].lower())
        self.assertIn("skew", nodes["SpectralIslandsV3"]["survived"].lower())
        self.assertIn("3.1", nodes["SpectralNeuron"]["survived"])
        self.assertIn("amplitude", nodes["SpectralNeuron"]["killed"].lower())

    def test_documentary_edges_are_preserved(self):
        atlas = load_atlas(ROOT)
        edges = {(edge["source"], edge["target"], edge["type"]) for edge in atlas["edges"]}
        self.assertIn(("HeadAsResonator", "HeadAsResonator2", "inherits"), edges)
        self.assertIn(("SpectralArchipelagoModelOfBrain", "SpectralIslandsV2", "inherits"), edges)
        self.assertIn(("GeometricNeuronV8", "SpectralIslandsV3", "corrects"), edges)

    def test_resonance_is_split_into_distinct_objects(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        self.assertIn("resonance-is-three-different-objects", motifs)
        motif = motifs["resonance-is-three-different-objects"]
        for node_id in ("HeadAsResonator", "SpectralIslandsV3", "SpectralNeuron"):
            self.assertIn(node_id, motif["nodes"])
        text = motif["description"].lower()
        self.assertIn("transfer", text)
        self.assertIn("skew", text)
        self.assertIn("frequency", text)


if __name__ == "__main__":
    unittest.main()
