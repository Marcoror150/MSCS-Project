/* This file is used to create a user named postgres, with a simple password and superuser permissions.
 It creates the required DB for the project. Any change here will need to be reflected in the supporting scripts.
 Author: Marc Christensen */

-- Otherwise just give the postgres user a password.
ALTER USER postgres WITH PASSWORD 'password';

-- Create database for application and assign postgres as owner.
CREATE DATABASE accidents_raw;
GRANT ALL PRIVILEGES ON DATABASE accidents_raw TO postgres;
