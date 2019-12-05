# Crash Analysis Report System - Team Super Soft Tacos
Data science group project for MSCS 710L
Authors:
 - Marc Christensen
 - Danny Mulick
 - Brandi Coon
---
## Value Statement
- Our mission at C.A.R.S. is to use data modeling techniques in order to give various insights about the outcomes and trends of automobile accidents in the United States.

---
## Description of Project
 - Using publicly available automobile accident data from the NHTSA, we constructed a system that gives various insights into the trends of accidents in the United States.
 - Recent accident data (2015) was utilized to help provide us with useful information that is relevant today.
 - This system allows easy access to information for the public (and potentially private companies) to help make informed decisions.
 - The system will:
 	- Determine the likelihood of a fatal accident involving one or more fatalities based on vehicle make, model, and year.
  - Determine the likelihood of a fatal accident based on the age of vehicle.
  - Determine the likelihood of an accident based on the state the vehicle is located within the United States.

---
## Code Explanation
 - api/
   - This directory houses our entire API for the project, built through SwaggerHub and SwaggerUI.
 - DB/
   - Contains the scripts for building and populating the database from the data in Data/
 - Data/
   - The NHTSA ftp server serves up the various CSV's that have the data for the years chosen (2015, 2016, 2017).
 - Ipynb Files
   - The jupyter notebook files contain all of our data exploration and modeling for both supervised and unsupervised methods.
   
---
## Local Scripts
- flaskLocal - Source this script in order to stand up the flask server locally, it will have to be brought down in between changes and updates.
- notebookLocal - Source this script to bring up the Jupyter local notebook service.

---
## Local Deployment Process
  [DockerHub](https://hub.docker.com/repository/docker/marcchristensen/mscsproject)
  
- Docker-compose file can be used to generate all of the necessary containers for further customization.
- Dockerfile creates the custom container for the webservice.
- DB generation scripts can be used to populate the postgresql database once initially configured.
  
---
## SwaggerHub
 - [SwaggerHub](https://app.swaggerhub.com/apis/dannymulick1/CARS_Capping2019/1.0.2)
 
Version 1.2
