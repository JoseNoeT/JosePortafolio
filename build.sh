services:
  - type: web
    name: portafolio-josemiguel
    env: python
    rootDir: backend/
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn portafolio.wsgi:application
    preDeployCommand: python manage.py migrate
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: portafolio.settings
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
      - key: ALLOWED_HOSTS
        value: portafolio-josemiguel.onrender.com
      - key: PYTHON_VERSION
        value: 3.11
