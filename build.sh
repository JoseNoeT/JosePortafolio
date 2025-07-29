#!/usr/bin/env bash
set -o errexit

# Entrar en la carpeta donde está manage.py
cd backend

# Instalar dependencias
pip install -r ../requirements.txt

# Migrar base de datos
python manage.py migrate

# Recolectar estáticos
python manage.py collectstatic --noinput
