"""Check weight metadata in the variable webfonts shipped in releases."""

from pathlib import Path
import unittest

from fontTools.ttLib import TTFont


WEBFONTS = Path(__file__).resolve().parents[1] / "fonts/webfonts/variable"


class VariableWebfontWeightsTest(unittest.TestCase):
    def test_default_weight_matches_os2(self):
        for suffix in (".woff", ".woff2"):
            paths = sorted(WEBFONTS.glob(f"*{suffix}"))
            self.assertTrue(paths, f"No {suffix} variable webfonts found")
            for path in paths:
                with self.subTest(font=path.name), TTFont(path) as font:
                    weight = next(
                        axis for axis in font["fvar"].axes if axis.axisTag == "wght"
                    )
                    self.assertEqual(
                        font["OS/2"].usWeightClass,
                        weight.defaultValue,
                        "OS/2 must describe the default variable instance",
                    )


if __name__ == "__main__":
    unittest.main()
