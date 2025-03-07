#!/bin/sh

echo 'Applying migrations...'
python manage.py migrate --no-input

echo 'Running collecstatic...'
python manage.py collectstatic --no-input
echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:8000
