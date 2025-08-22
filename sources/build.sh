#!/bin/bash
# build.sh - Font building script for Mona Sans

set -e  # Exit on any error

# Check if running from the correct directory
if [ ! -f "sources/config.yaml" ]; then
  echo "Error: Please run this script from the root of the repository."
  exit 1
fi

echo "Starting Mona Sans Google Fonts build process..."

# Check for required tools
command -v gftools >/dev/null 2>&1 || { echo "Error: gftools is required but not installed. Aborting."; exit 1; }
command -v ttfautohint >/dev/null 2>&1 || { echo "Warning: ttfautohint not found. Install for best hinting results."; }

# build googlefonts
gftools builder sources/config.yaml

echo "Google's Font files available in the 'fonts/googlefonts' directory"

# clear static fonts
rm -rf fonts/static/*
rm -rf fonts/webfonts/static/*

# move static fonts
mv fonts/googlefonts/otf* fonts/static/otf
mv fonts/googlefonts/ttf* fonts/static/ttf
mv fonts/googlefonts/webfonts/* fonts/webfonts/static/
rm -rf fonts/googlefonts/webfonts/

# pull google variable fonts out of folder
mv fonts/googlefonts/variable/* fonts/googlefonts/
rm -rf fonts/googlefonts/variable/