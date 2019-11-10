FROM ubuntu:16.04

RUN apt-get update 
RUN apt-get install -y build-essential python-pip python-dev
RUN pip install --upgrade pip

RUN mkdir -p /data/postgres
ADD . /data/postgres
RUN pip install -r requirements.txt

WORKDIR /opt/microservices
EXPOSE 5000

CMD start.sh