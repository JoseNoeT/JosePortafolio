#!/usr/bin/env bash
set -o errexit

# Instalar dependencias (subimos un nivel porque requirements.txt está en la raíz del repo)
pip install -r ../requirements.txt

# Migrar la base de datos
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
