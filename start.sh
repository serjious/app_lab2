#!/bin/sh

clear;
if python -m unittest -v unit.py
then
    echo "Running tandem.py..."
    python tandem.py
fi
