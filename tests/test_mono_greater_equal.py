from pathlib import Path
import re
import unittest


class GreaterEqualLigatureTest(unittest.TestCase):
    def test_all_masters_mirror_less_equal_horizontally(self):
        glyph = (
            Path(__file__).resolve().parents[1]
            / "sources/MonaSansMono.glyphspackage/glyphs/greater_equal.liga.glyph"
        ).read_text()
        components = re.findall(r"\{\s*ref = less_equal\.liga;\s*(.*?)\s*\}", glyph, re.S)

        self.assertEqual(len(components), 6)
        self.assertTrue(all(component == "scale = (-1,1);" for component in components))


if __name__ == "__main__":
    unittest.main()
