#!/bin/bash

# Create neccessary directory, maybe move to docker file?
mkdir usr/local/var/postgres

# Run DB creation script. May need to specify python2?
./DB/DBInitialization.sh

# Run the DB populate script.
python  ./DB/DBPopulate.py

# Start the web app.
./flaskLocal.sh
