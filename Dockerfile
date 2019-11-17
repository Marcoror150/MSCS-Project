FROM ubuntu:16.04

RUN apt-get update 
RUN apt-get install -y build-essential python-pip python-dev
RUN pip install --upgrade pip

# Create directories we need.
RUN ["mkdir -p /data/postgres", "mkdir usr/local/var/postgres"]

# Copy files from our project that are absolutely needed.
COPY ./app /app
COPY ./DB /DB
COPY ./Data /Data
COPY ./requirements.txt /requirements.txt
COPY ./flaskLocal.sh /flaskLocal.sh

RUN pip install -r requirements.txt

CMD start.sh

EXPOSE 5000
