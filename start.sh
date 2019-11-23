#!/bin/bash

# Install Additional requirements.
apt update

# apt-get install -y build-essential libpq-dev python-psycopg2 curl file git ruby-full

# Start postgresql service.
service postgresql start

# su - postgres

# Run DB creation script.
# psql -U postgres /DB/DBInitialization.sql

# Run the DB populate script.
# python2 /DB/DBPopulate.py

# # Change encodings for Flask to work.
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# # Start the web app.
# /flaskLocal
