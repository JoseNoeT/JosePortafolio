#!/usr/bin/env bash
set -o errexit

# Instalar dependencias desde la raíz del repo
pip install -r $RENDER_PROJECT_ROOT/requirements.txt

# Migrar y recolectar estáticos (ya estamos en backend)
python manage.py migrate
python manage.py collectstatic --noinput
