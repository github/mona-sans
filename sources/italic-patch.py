import glob
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord

if __name__ == "__main__":

    for font_path in glob.glob("../fonts/variable/*Italic*.ttf"):
        with open(font_path, "rb") as f:
            print("Fix italic style linking in {}".format(font_path))
            ttFont = TTFont(f)
            ttFont["post"].italicAngle = -12
            ttFont["hhea"].caretSlopeRise = 1000
            ttFont["hhea"].caretSlopeRun = 213
            ttFont["name"].setName("MonaSansItalic", 25, 3, 1, 0x409)
            ttFont["name"].setName("ExtraLight", 261, 3, 1, 0x409)
            ttFont["name"].setName("Regular", 263, 3, 1, 0x409)
            ttFont["name"].setName("ExtraLight", 261, 1, 0, 0)
            ttFont["name"].setName("Regular", 263, 1, 0, 0)
            ttFont.save(font_path)
