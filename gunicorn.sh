#!/bin/sh
python manage.py collectstatic --noinput --clear
/usr/local/bin/gunicorn config.wsgi -b unix:/sockets/webapp.sock -w 4 --chdir=/app
