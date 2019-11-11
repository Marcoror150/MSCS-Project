#!/bin/bash

# Run DB creation script. May need to specify python2?
./DB/DBInitialization.sh

# Run the DB populate script.
python  ./DB/DBPopulate.py

# Start the web app.
source flaskLocal
