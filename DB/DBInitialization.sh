#!/bin/bash

# Install Ruby and Homebrew.
sudo apt update

sudo apt install ruby-full

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install postgresql.
brew install postgresql

# Start postgresql services everytime on startup.
pg_ctl -D /usr/local/var/postgres start && brew services start postgresql

# Check version for debugging purposes.
# postgres -V

# Sudo may be required to enter postgresql environment.
psql postgres

# Create a user
CREATE ROLE postgres WITH LOGIN PASSWORD 'password';

# Grant user permissions
ALTER ROLE postgres CREATEDB;

# Leave super user environment and enter postgres user environment.
\q
psql postgres -U postgres

# Create database for application and assign postgres as owner.
CREATE DATABASE accidents_raw;
GRANT ALL PRIVILEGES ON DATABASE accidents_raw TO postgres;

# Connect to the DB.
\connect accidents_raw