#!/bin/bash
yes | cp ./_prod/settings.py /usr/src/app/config
yes | cp ./_prod/main.js /usr/src/app/static/js
python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi:application  -b 0.0.0.0:80