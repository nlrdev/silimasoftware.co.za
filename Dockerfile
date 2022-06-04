FROM localhost:5000/python-silimasoftware:latest
RUN mkdir /usr/src/app
ADD ./website /usr/src/app
WORKDIR /usr/src/app/_prod
RUN chmod u+x setup.bash
RUN ./setup.bash
WORKDIR /usr/src/app