#!/usr/bin/env bash
set -o errexit

# Instalar dependencias (ahora dentro de backend)
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
