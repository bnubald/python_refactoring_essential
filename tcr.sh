#!/bin/bash
# Test and commit or revert
git add .
python3 -m unittest discover && git commit -m "It works!" || git reset --hard
