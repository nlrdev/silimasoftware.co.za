#!/bin/bash
python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi:application  -b 0.0.0.0:80