#!/bin/bash

# Install Ruby.
apt update

apt-get install -y build-essential libpq-dev python-psycopg2 curl file git ruby-full

# Install Linuxbrew.
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
echo 'export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"' >>~/.bash_profile
echo 'export MANPATH="/home/linuxbrew/.linuxbrew/share/man:$MANPATH"' >>~/.bash_profile
echo 'export INFOPATH="/home/linuxbrew/.linuxbrew/share/info:$INFOPATH"' >>~/.bash_profile

PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"

# Install postgresql.
brew install postgresql

# Start postgresql services everytime on startup.
pg_ctl -D /home/linuxbrew/.linuxbrew/var/postgres start

# Run DB creation script.
psql -U postgres postgres -f /DB/DBInitialization.sql

# Run the DB populate script.
python2 /DB/DBPopulate.py

# Change encodings for Flask to work.
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Start the web app.
/flaskLocal
