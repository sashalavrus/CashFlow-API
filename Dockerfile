FROM python:3.8-alpine
MAINTAINER OLEKSANDR LAVRUSENKO

ENV PYTHONUNBUFFERED 1
COPY ./req.txt ./req.txt
RUN apk add  --no-cache --virtual .tmp-build-deps build-base\
        gcc libc-dev linux-headers gcc musl-dev libffi-dev openssl-dev python3-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /req.txt --no-binary :all:
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user