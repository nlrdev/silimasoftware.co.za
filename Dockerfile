FROM localhost:5000/python-silimasoftware:latest
RUN mkdir /usr/src/app
ADD ./website /usr/src/app
WORKDIR /usr/src/app
COPY ./_prod/settings.py /usr/src/app/config
COPY ./_prod/main.js /usr/src/app/static/js
