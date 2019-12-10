FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /usr/src/app

ENV DATABASE_URL postgresql://postgres:password@postgres:5432/accidents_raw

EXPOSE 8080
EXPOSE 5432

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server", "--host=0.0.0.0"]