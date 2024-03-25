#!/bin/sh

set -e

echo "Generating Variable Fonts"
fontmake -g *.glyphs -o variable --round-instances --output-dir fonts
echo "Variable Fonts Succeedeed"

echo "========================"

echo "Generating Static Fonts"
fontmake -g *.glyphs -o ttf --round-instances --keep-direction -i --output-dir fonts
fontmake -g *.glyphs -o otf --round-instances --keep-direction -i --output-dir fonts
echo "Static Fonts Succeedeed"

echo "======================="

echo "Removing UFOs"
rm -rf master_ufo instance_ufo
echo "UFOs Removed"

echo "Generating Webfont"
fonts=$(ls ./fonts/*.ttf)
for f in $fonts
do
	sfnt2woff-zopfli "$f"
	woff2_compress "$f"
	echo "Finished"
done

echo "All task has completed"
