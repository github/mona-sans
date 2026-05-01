# Build process

### MonaSansVF Build (via Glyphs.app)

Mona Sans VF is exported from the Glyphs interface directly into the /fonts directory. This is the easiest way to distribute multiple cuts of the variable font.

1. Open MonaSans.glyphs project in Glyphs.app
2. Use File > Export > Variable Font
3. Save the exported variable font into the `/fonts` directory.

Running `build.sh` will try to move them to the right place, if you don't put them there already.

### Google Fonts Build (`build.sh`)

The `build.sh` script handles building font files that meet Google Fonts specifications and requirements, and builds into the `/googlefonts` folder. It also checks to make sure the other fonts are in the right place.

```bash
sh sources/build.sh
```

You'll need gftools and ttfautohint installed. Which you can do via:

```bash
pip3 install gftools
brew install ttfautohint
```

