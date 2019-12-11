# Crash Analysis Report System - Team Super Soft Tacos
Data science group project for MSCS 710L
Authors:
 - Marc Christensen
 - Danny Mulick
 - Brandi Coon
 
---

### Version 1.2

---

## Value Statement
- Our mission at C.A.R.S. is to use data modeling techniques in order to give various insights about the outcomes and trends of automobile accidents in the United States.

---

## Description of Project
 - Using publicly available automobile accident data from the NHTSA, the system gives various insights into the trends of accidents in the United States.
 - Recent accident data was utilized to help provide useful information that is relevant today.
 - This system allows easy access to information for the public (and potentially private companies) to help make informed decisions.
 - The system will:
   - Determine the likelihood of a fatal accident involving one or more fatalities based on the vehicle's make, model, and year.
   - Determine the likelihood of a fatal accident based on the age of the vehicle.
   - Determine the likelihood of an accident based on the state the vehicle is located within the United States.

---

## Code Explanation
 - api/
   - This directory houses our entire API for the project, built through SwaggerHub and SwaggerUI.
 - DB/
   - Contains the scripts for building and populating the database from the data found in the Data/ directory.
 - Data/
   - The NHTSA ftp server serves up the various CSV's that have the data for the years chosen (2015, 2016, 2017).
 - Ipynb Files
   - The Jupyter notebook files contain all of our data exploration and modeling for both supervised and unsupervised methods. 

---

## Local Scripts
- /flaskLocal - Source this script in order to stand up the flask server locally, it will have to be brought down in between changes and updates.
- /notebookLocal - Source this script to bring up the Jupyter local notebook service.
- /DB/DBInitialization.sql - This SQL script provides basic commands to assign a password to the postgres user and create the basic DB.
- /DB/DBPopulate.py - This python script creates and populates the tables used in the app, if the user would like to manipulate the data.
- /DB/DBCalls.py - This python script provides basic functions to interact with the database.

---

## Local Deployment Process
  [DockerHub Image](https://hub.docker.com/repository/docker/marcchristensen/mscsproject)
  
- Dockerfile creates the custom container for the webservice.
- Docker-compose file can be used to generate all of the necessary containers for further customization.
- DB generation scripts can be used to populate the postgresql database once initially configured.
- `docker-compose up` in the root directory will bring the application online and expose the web application on port 5000 

---

## Cloud Deployment Process
- Follow these instructions to deploy the app to AWS: [AWS Instructions](https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/) using the same DockerHub image found above.
  - If these instructions are no longer helpful, offical AWS instructions should be used.

---

## SwaggerHub API Definition
 - [SwaggerHub](https://app.swaggerhub.com/apis/dannymulick1/CARS_Capping2019/1.0.2)
 
---