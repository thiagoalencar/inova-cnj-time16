FROM python:3.7-slim-buster

ENV DEBIAN_FRONTEND="noninteractive"

RUN export DEBIAN_FRONTEND=noninteractive \
    && echo "America/Sao_Paulo" > /etc/timezone \
    && mkdir /home/flask-api \
    && apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install gcc \
    && apt-get -y install libpq-dev \
    && apt-get -y install libaio-dev \
    && mkdir -p /opt/data/api \
    && apt-get clean all 

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /home/flask-api/

COPY ./flask-api .

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait wait
RUN chmod +x wait

COPY migrate.sh migrate.sh
RUN chmod +x migrate.sh

EXPOSE 5002
