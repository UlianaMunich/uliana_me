#!/bin/sh
python manage.py collectstatic --noinput --clear
/usr/local/bin/gunicorn config.wsgi -b 0.0.0.0:$PORT -w 4 --chdir=/app
