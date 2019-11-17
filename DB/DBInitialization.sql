/* This file is used to create a user named postgres, with a simple password and superuser permissions.
 It creates the required DB for the project. Any change here will need to be reflected in the supporting scripts.
 Author: Marc Christensen */

-- Check version for debugging purposes.
-- postgres -V

-- Create a user
CREATE ROLE postgres WITH LOGIN PASSWORD 'password';

-- Grant user permissions
ALTER ROLE postgres SUPERUSER;

-- Create database for application and assign postgres as owner.
CREATE DATABASE accidents_raw;
GRANT ALL PRIVILEGES ON DATABASE accidents_raw TO postgres;
