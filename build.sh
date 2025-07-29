#!/usr/bin/env bash
set -o errexit

# Ya estamos dentro de /backend gracias al rootDir
pip install -r ../requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
