#!/bin/sh
set -e
#source ../env/bin/activate

vf=MonaSans[slnt,wdth,wght].ttf

echo "Build VF"

gftools builder config.yaml

echo "slice Upright"

fonttools varLib.instancer ../fonts/variable/$vf slnt=0 --output ../fonts/variable/MonaSans[wdth,wght].ttf --update-name-table

echo "slice Italic"

fonttools varLib.instancer ../fonts/variable/$vf slnt=-12 --output ../fonts/variable/MonaSans-Italic[wdth,wght].ttf --update-name-table

echo "Complete"
