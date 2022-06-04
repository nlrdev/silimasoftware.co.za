FROM python:3.11.0a2-bullseye
RUN mkdir /usr/src/app
ADD ./website /usr/src/app
ADD ./_prod/settings.py /usr/src/app/config
ADD ./_prod/main.js /usr/src/app/static/js
WORKDIR /usr/src/app
RUN apt update -y && apt upgrade -y
RUN apt install -y libpq-dev gcc
RUN pip install --upgrade pip 
RUN pip install --upgrade -r requirements.txt 
