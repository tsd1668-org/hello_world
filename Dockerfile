# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8080", "hello_world.wsgi:application"]
