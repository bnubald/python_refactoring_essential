#!/bin/bash
set -e

echo "Running ShippingApp for multiple orders..."
echo ""

for I in 1001 1002 1003; do
    echo "============================"
    echo "Running order ID: $I"
    echo "============================"

    python -m legacy_code.src.ShippingApp "$I"

    echo ""
done

echo "Done."
read -p "Press [enter] to continue..."
