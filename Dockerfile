FROM python:3.8-slim-buster
MAINTAINER OLEKSANDR LAVRUSENKO

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser user
USER user