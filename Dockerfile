FROM python:3.11.0a2-bullseye
RUN mkdir /usr/src/app
ADD ./website /usr/src/app
WORKDIR /usr/src/app
RUN apt update -y && apt upgrade -y
RUN apt install -y libpq-dev gcc
RUN pip install --upgrade pip 
RUN pip install --upgrade -r requirements.txt 
