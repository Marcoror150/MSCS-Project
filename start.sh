#!/bin/bash

# Run the DB populate script.
python2 /DB/DBPopulate.py

# Start the web service.
python3 -m flask run --host=0.0.0.0