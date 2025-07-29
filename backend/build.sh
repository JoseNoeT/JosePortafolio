#!/usr/bin/env bash
set -o errexit

pip install -r backend/requirements.txt
python backend/manage.py migrate
python backend/manage.py collectstatic --noinput
