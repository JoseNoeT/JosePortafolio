import os
from pathlib import Path
import dj_database_url

# 📂 BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Seguridad y entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')  # Valor por defecto solo para desarrollo
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS if host]

# 📦 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectos',
]

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 📡 Rutas y WSGI
ROOT_URLCONF = 'portafolio.urls'
WSGI_APPLICATION = 'portafolio.wsgi.application'

# 🛢️ Base de datos: Postgres en Render (automática si DATABASE_URL existe)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# 🖼️ Plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Plantillas globales (no usadas por ahora)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'proyectos.context_processors.global_context',  # Si usas variables globales como {{ now }}
            ],
        },
    },
]

# 🌍 Internacionalización
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# 📁 Archivos estáticos (para Render con WhiteNoise)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 📁 Archivos multimedia (Render no guarda archivos persistentes)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 🆔 ID por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
