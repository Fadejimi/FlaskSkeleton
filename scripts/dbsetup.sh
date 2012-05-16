#!/bin/bash

echo "Deleting Database"
rm -rf ../skeleton.db

echo "Initializing Database"
curl -0 http://localhost:5000/generate
echo ""

echo "Insert"
./scripts/initial_insert.sh

echo "Requirements"
./scripts/list.sh
