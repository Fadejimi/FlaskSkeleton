#!/bin/bash

echo "Adding environment..."
virtualenv env 

echo "Activating environment..."
. env/bin/activate

echo "Installing dependencies..."
# Add dependant packages here
easy_install Flask