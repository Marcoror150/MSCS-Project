#!/bin/bash

# Install Ruby.
sudo apt update

sudo apt install ruby-full

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

sudo apt install libpq-dev python3-dev

# Install Linuxbrew, needs user interaction
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

# Install postgresql.
brew install postgresql

# Start postgresql services everytime on startup.
pg_ctl -D /home/linuxbrew/.linuxbrew/var/postgres start

# Run DB creation script.
psql -U postgres postgres -f ./DB/DBInitialization.sql

# Run the DB populate script.
python2 ./DB/DBPopulate.py

# Start the web app.
./flaskLocal.sh
