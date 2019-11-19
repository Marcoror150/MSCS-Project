FROM ubuntu:16.04

RUN apt-get update 
RUN apt-get install -y python-pip python-dev python3-pip python3-dev
RUN pip install --upgrade pip
RUN pip3 install --upgrade pip

# Create directories we need.
RUN mkdir -p /data/postgres
RUN mkdir -p /usr/local/var/postgres

# Copy files from our project that are absolutely needed.
COPY ./app /app
COPY ./DB /DB
COPY ./Data /Data
COPY ./start.sh /start.sh
COPY ./requirements.txt /requirements.txt
COPY ./flaskLocal /flaskLocal

RUN pip3 install -r requirements.txt

EXPOSE 5000

RUN /start.sh
