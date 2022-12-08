#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --env DJANGO_SETTINGS_MODULE=taskmanager.settings --socket :9000 --workers 4 --master --enable-threads --module taskmanager.wsgi