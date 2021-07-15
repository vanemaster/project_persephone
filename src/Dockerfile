FROM redis:alpine
WORKDIR /redis
COPY redis.conf /usr/local/etc/redis/redis.conf

# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/projectpersephone/project_persephone/projectpersephone

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN apk add --no-cache --upgrade bash

RUN pip install --upgrade cython

# install dependencies
RUN pip install --upgrade pip
RUN pip install flask SQLAlchemy

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/projectpersephone/project_persephone/projectpersephone/entrypoint.sh"]