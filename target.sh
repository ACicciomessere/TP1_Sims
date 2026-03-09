#!/bin/bash

# Script to visualize a specific particle using previously generated data from run.sh.
# It assumes output.txt and particles.txt exist in the project root.

if [ ! -f "output.txt" ] || [ ! -f "particles.txt" ]; then
    echo "Data files not found. Please execute ./run.sh first to generate them."
    exit 1
fi

# the python script will prompt for the target id interactively
python3 python/visualize.py
