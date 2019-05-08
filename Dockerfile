# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# requirements for installing pyscopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

RUN ldconfig

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "-b", "0.0.0.0:8080", "hello_world.wsgi:application"]
