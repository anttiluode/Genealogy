from pathlib import Path
import cmath
import math
import unittest

from scripts.validate_data import load_atlas, validate_atlas

ROOT = Path(__file__).resolve().parents[1]


def phase_image(phases, positions, k, common_offset=0.0):
    """Reference formula from Phi-Hologram.py, not a physiological forward model."""
    pixels = [(-0.7, -0.4), (0.0, 0.0), (0.6, 0.4), (1.1, -0.9)]
    values = []
    for x, y in pixels:
        z = sum(
            cmath.exp(1j * (phi - k * math.hypot(x - ex, y - ey) + common_offset))
            for phi, (ex, ey) in zip(phases, positions)
        )
        values.append(abs(z) ** 2)
    return values


class PhiHologramPhaseGaugePassTests(unittest.TestCase):
    def test_registered_once_with_honest_boundaries(self):
        atlas = load_atlas(ROOT)
        self.assertEqual([], validate_atlas(atlas))
        self.assertEqual(1, sum(n["id"] == "Phi-Hologram" for n in atlas["nodes"]))
        self.assertEqual(
            "reviewed",
            next(r["inventory_status"] for r in atlas["repos"] if r["name"] == "Phi-Hologram"),
        )
        self.assertIn("phi-hologram-phase-gauge", [p["id"] for p in atlas["passes"]])
        node = next(n for n in atlas["nodes"] if n["id"] == "Phi-Hologram")
        self.assertIn("unit amplitude", node["killed"])
        self.assertIn("read_raw_edf", node["killed"])
        self.assertIn("U(1)", node["survived"])

    def test_common_rotation_is_exact_observer_null_but_relative_rotation_is_not(self):
        phases = [0.12, -0.8, 1.1, 2.4]
        positions = [(-0.3, 0.9), (0.3, 0.9), (-0.7, 0.6), (0.4, -0.5)]
        for k in (1.0, 10.0, 50.0):
            base = phase_image(phases, positions, k)
            for offset in (-math.pi / 2, 0.7, math.pi / 2):
                rotated = phase_image(phases, positions, k, common_offset=offset)
                self.assertLess(max(abs(a - b) for a, b in zip(base, rotated)), 1e-12)
            one_changed = phases.copy()
            one_changed[0] += 0.7
            changed = phase_image(one_changed, positions, k)
            self.assertGreater(max(abs(a-b) for a, b in zip(base, changed)), 0.01)

    def test_convergence_is_motif_not_invented_lineage(self):
        atlas = load_atlas(ROOT)
        motif = next(m for m in atlas["motifs"] if m["id"] == "phase-hologram-observer-null")
        self.assertTrue(
            {"Phi-Hologram", "EEGTools", "phi-world-theory", "ResidentOperatorTomography"}
            .issubset(set(motif["nodes"]))
        )
        self.assertFalse(any(
            e["target"] == "Phi-Hologram" or e["source"] == "Phi-Hologram"
            for e in atlas["edges"]
        ))


if __name__ == "__main__":
    unittest.main()
