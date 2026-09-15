from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class MeasurementDisciplinePassTests(unittest.TestCase):
    def test_measurement_discipline_pass_keeps_kills_and_instrument_audits(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("measurement-discipline", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "RajapintaFable",
            "Visertaja",
            "Vino",
            "ArrowField",
            "Eromitta",
            "Kaiku",
            "Ristikko",
            "KYY",
            "GeometricNeuronPlusField",
            "TransientWaveCompiler",
        ):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        self.assertEqual(edges[("Nollas", "Visertaja", "inherits")]["confidence"], "high")
        self.assertEqual(edges[("Visertaja", "Vino", "inherits")]["confidence"], "high")
        self.assertEqual(edges[("GeometricNeuronV21", "Vino", "converges")]["confidence"], "high")
        self.assertEqual(edges[("ArrowField", "Eromitta", "inherits")]["confidence"], "high")
        self.assertEqual(edges[("Kaiku", "Ristikko", "inherits")]["confidence"], "high")
        self.assertEqual(
            edges[("GeometricNeuronPlusField", "TransientWaveCompiler", "inherits")]["confidence"],
            "high",
        )
        self.assertEqual(edges[("TransientWaveCompiler", "KYY", "converges")]["confidence"], "high")

        vino = next(node for node in atlas["nodes"] if node["id"] == "Vino")
        self.assertIn("gru", vino["killed"].lower())
        self.assertIn("skew", vino["survived"].lower())

        eromitta = next(node for node in atlas["nodes"] if node["id"] == "Eromitta")
        self.assertIn("5", eromitta["survived"])
        self.assertIn("instrument", eromitta["killed"].lower())

        kaiku = next(node for node in atlas["nodes"] if node["id"] == "Kaiku")
        self.assertIn("instrument", kaiku["killed"].lower())

        twc = next(node for node in atlas["nodes"] if node["id"] == "TransientWaveCompiler")
        self.assertIn("0.280", twc["killed"])
        self.assertIn("identifi", twc["survived"].lower())

    def test_method_motif_connects_preregistration_to_negative_capability(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["registered-kills-and-instrument-audits"]
        self.assertTrue(
            {"ArrowField", "Eromitta", "Kaiku", "Ristikko", "KYY", "TransientWaveCompiler"}.issubset(
                set(motif["nodes"])
            )
        )

    def test_receiver_as_instrument_motif_crosses_wave_and_observability_lines(self):
        atlas = load_atlas(ROOT)
        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        motif = motifs["receiver-is-part-of-computation"]
        self.assertTrue(
            {"Kaiku", "Ristikko", "GeometricNeuronV24", "ReadWrite"}.issubset(set(motif["nodes"]))
        )


if __name__ == "__main__":
    unittest.main()
