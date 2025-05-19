#!/bin/bash
# build.sh - Font building script for Mona Sans

set -e  # Exit on any error

echo "Starting Mona Sans build process..."

# Check for required tools
command -v gftools >/dev/null 2>&1 || { echo "Error: gftools is required but not installed. Aborting."; exit 1; }
command -v ttfautohint >/dev/null 2>&1 || { echo "Warning: ttfautohint not found. Install for best hinting results."; }

# build
gftools builder sources/config.yaml

echo "Font files available in the 'googlefonts' directory"