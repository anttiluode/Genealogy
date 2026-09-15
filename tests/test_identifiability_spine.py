from pathlib import Path
import unittest

from scripts.validate_data import load_atlas

ROOT = Path(__file__).resolve().parents[1]


class IdentifiabilitySpineTests(unittest.TestCase):
    def test_late_august_identifiability_spine_keeps_explicit_parentage(self):
        atlas = load_atlas(ROOT)
        pass_ids = {item["id"] for item in atlas["passes"]}
        self.assertIn("identifiability-spine", pass_ids)

        ids = {node["id"] for node in atlas["nodes"]}
        for node_id in (
            "Monday",
            "Tuesday",
            "yrotisopeRweN",
            "Twensday",
            "T-800NNP",
            "KyberDyyni1",
            "MovingProblem",
            "AlgoSchalgo",
        ):
            self.assertIn(node_id, ids)

        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        for source, target in (
            ("Monday", "Tuesday"),
            ("Tuesday", "yrotisopeRweN"),
            ("yrotisopeRweN", "Twensday"),
            ("Twensday", "T-800NNP"),
            ("T-800NNP", "KyberDyyni1"),
            ("KyberDyyni1", "MovingProblem"),
        ):
            edge = edges[(source, target, "inherits")]
            self.assertEqual(edge["confidence"], "high")

        self.assertNotIn(("MovingProblem", "AlgoSchalgo", "inherits"), edges)
        self.assertNotIn(("AlgoSchalgo", "MovingProblem", "inherits"), edges)

    def test_active_observation_threads_converge_on_child_and_thirdway(self):
        atlas = load_atlas(ROOT)
        edges = {
            (edge["source"], edge["target"], edge["type"]): edge
            for edge in atlas["edges"]
        }
        for source in ("MovingProblem", "AlgoSchalgo"):
            self.assertEqual(edges[(source, "Child", "converges")]["confidence"], "high")
            self.assertEqual(edges[(source, "ThirdWay", "converges")]["confidence"], "high")

        moving = next(node for node in atlas["nodes"] if node["id"] == "MovingProblem")
        self.assertIn("-1.0000", moving["survived"])
        self.assertIn("procrustes", moving["killed"].lower())

        algo = next(node for node in atlas["nodes"] if node["id"] == "AlgoSchalgo")
        self.assertIn("0.91675", algo["survived"])
        self.assertIn("repeatability", algo["killed"].lower())

        motifs = {motif["id"]: motif for motif in atlas["motifs"]}
        self.assertTrue(
            {"MovingProblem", "AlgoSchalgo", "Child", "ThirdWay"}.issubset(
                set(motifs["identifiability-before-credit"]["nodes"])
            )
        )


if __name__ == "__main__":
    unittest.main()
