FROM localhost:5000/python-silimasoftware:latest
RUN mkdir /usr/src/app
ADD ./website /usr/src/app
WORKDIR /usr/src/app
RUN yes | cp ./_prod/settings.py /usr/src/app/config
RUN yes | cp ./_prod/main.js /usr/src/app/static/js
RUN chmod +x ./setup.sh
ENTRYPOINT ./setup.sh