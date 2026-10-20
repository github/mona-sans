import re
import unittest
from pathlib import Path

GLYPHS = Path(__file__).resolve().parents[1] / "sources" / "MonaSansMono.glyphspackage" / "glyphs"

LIGATURES = ["equal_equal.liga", "hyphen_hyphen.liga", "exclam_equal.liga"]

LAYER = re.compile(r'layerId = "?([^;"]+)"?;\n(.*?)^width = (\d+);', re.S | re.M)
COMPONENT = re.compile(r"(?:pos = \((-?\d+),(-?\d+)\);\n)?ref = ([^;]+);(?:\nscale = \(([\d.]+),[\d.]+\);)?")
NODE = re.compile(r"^\((-?\d+),(-?\d+),", re.M)


def layers(name):
    text = (GLYPHS / f"{name}.glyph").read_text()
    return {m.group(1): (m.group(2), int(m.group(3))) for m in LAYER.finditer(text)}


def xs(name, layer_id):
    """All x coordinates of the glyph outline, with components placed."""
    body = layers(name)[layer_id][0]
    out = [int(m.group(1)) for m in NODE.finditer(body)]
    for dx, _, ref, sx in COMPONENT.findall(body):
        out += [x * float(sx or 1) + int(dx or 0) for x in xs(ref, layer_id)]
    return out


class MonoLigatureExtent(unittest.TestCase):
    def test_ink_spans_both_cells(self):
        # A ligature glyph sits in the second cell, so its outline must reach
        # back into the first cell as well as across the second one.
        for name in LIGATURES:
            for layer_id, (_, width) in layers(name).items():
                points = xs(name, layer_id)
                self.assertLess(min(points), -width // 2, f"{name} {layer_id}")
                self.assertGreater(max(points), width // 2, f"{name} {layer_id}")

    def test_exclam_equal_draws_its_slash(self):
        # != is == plus a slash, so every layer needs a contour of its own.
        for layer_id, (body, _) in layers("exclam_equal.liga").items():
            self.assertIn("nodes = (", body, layer_id)


if __name__ == "__main__":
    unittest.main()
