#!/bin/bash

# Run DB creation script.
python2 ./DB/DBInitialization.sh

# Run the DB populate script.
python2 ./DB/DBPopulate.py

# Start the web app.
./flaskLocal.sh
