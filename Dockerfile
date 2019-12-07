FROM ubuntu:16.04

# Copy files from our project that are required.
COPY . /

# Update software and install dependencies
RUN apt-get update; apt update 
RUN apt install -y postgresql postgresql-contrib
RUN apt-get install -y python-pip python-dev python3-pip python3-dev build-essential libpq-dev python-psycopg2 curl file git ruby-full vim
RUN pip install --upgrade pip; pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Expose ports for webservice and postgresql
EXPOSE 5000
EXPOSE 5432

# Prepares environment for web app.
ENV FLASK_APP /app.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV DATABASE_URL postgresql://postgres:password@postgres:5432/accidents_raw

# Runs web app on localhost:5000 and populates the DB.
CMD ["/start.sh"]
