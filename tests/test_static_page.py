from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StaticPageTests(unittest.TestCase):
    def test_page_has_expanded_views_and_no_external_dependencies(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for view in ("genealogy", "timeline", "corrections", "tools", "census", "survivors", "queue"):
            self.assertIn(f'data-view="{view}"', html)
        for element_id in ("coverage-bar", "pass-filter", "edge-filter", "era-strip", "focus-selected", "tools-content"):
            self.assertIn(f'id="{element_id}"', html)
        self.assertNotIn("https://cdn", html)
        self.assertNotIn("unpkg.com", html)

    def test_app_loads_base_data_and_modular_pass_index(self):
        js = (ROOT / "assets/app.js").read_text(encoding="utf-8")
        for path in ("data/repos.json", "data/nodes.json", "data/edges.json", "data/motifs.json", "data/passes/index.json"):
            self.assertIn(path, js)
        for function in ("renderTimeline", "renderCorrections", "renderTools", "renderEraStrip", "loadPasses"):
            self.assertIn(f"function {function}", js)
        self.assertIn("node.usefulness === 'practical'", js)

    def test_genealogy_graph_has_zoom_and_pan_controls(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        zoom_path = ROOT / "assets/zoom.js"
        zoom_js = zoom_path.read_text(encoding="utf-8") if zoom_path.exists() else ""
        for element_id in ("zoom-in", "zoom-out", "zoom-reset", "zoom-level"):
            self.assertIn(f'id="{element_id}"', html)
        self.assertIn('assets/zoom.js', html)
        for function in ("setupGraphViewport", "zoomGraph", "panGraph", "resetGraphViewport"):
            self.assertIn(f"function {function}", zoom_js)
        self.assertIn("addEventListener('wheel'", zoom_js)
        self.assertIn("addEventListener('pointermove'", zoom_js)

if __name__ == "__main__":
    unittest.main()
