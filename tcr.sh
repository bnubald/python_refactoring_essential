#!/bin/bash
# Test and commit or revert
git add .
python -m unittest discover && git commit -m "It works!" || git reset --hard
