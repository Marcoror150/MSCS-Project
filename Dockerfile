FROM ubuntu:16.04

RUN apt-get update; apt update 
RUN apt install -y postgresql postgresql-contrib
RUN apt-get install -y python-pip python-dev python3-pip python3-dev build-essential libpq-dev python-psycopg2 curl file git ruby-full vim
RUN pip install --upgrade pip; pip3 install --upgrade pip

# Copy files from our project that are required.
COPY . /

RUN pip3 install -r requirements.txt

EXPOSE 5000
EXPOSE 5432

ENV FLASK_APP /app.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
