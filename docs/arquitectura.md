# Portafolio Profesional – José Miguel Noe Torres

## 🧱 Estructura general

Este es un proyecto Django que funciona como mi portafolio profesional. El objetivo es mostrar los proyectos que ya he desarrollado, con detalles técnicos, imágenes y enlaces funcionales.

### 🔧 Tecnologías utilizadas
- Python 3.11
- Django 5.2.4
- HTML + Bootstrap
- Panel de administración de Django

---

## 📦 Día 1 – Estructura inicial

Pasos realizados:

1. Crear entorno virtual:
   python -m venv venv
   .\venv\Scripts\activate

2. Instalar Django:
   pip install django

3. Crear carpeta para backend:
   mkdir backend

4. Crear el proyecto Django dentro de esa carpeta:
   django-admin startproject portafolio backend

5. Entrar a la carpeta y probar el servidor:
   cd backend
   python manage.py runserver

Resultado: proyecto Django creado con éxito. Página inicial visible en http://127.0.0.1:8000/

---

## 🧪 Día 2 – Migraciones iniciales y creación de app proyectos

1. Aplicar migraciones del sistema:
   python manage.py migrate

2. Crear app principal:
   python manage.py startapp proyectos

3. Registrar app en portafolio/settings.py:
   INSTALLED_APPS = [
       ...
       'proyectos',
   ]

Resultado: Django tiene su base de datos inicial creada y la app donde se cargará cada proyecto está registrada.

---

## 🧩 Día 3 – Modelo Project (vitrina de trabajos)

Se creó el modelo Project para representar cada proyecto real que ya he desarrollado. Este modelo será visible desde el panel de administración y cargado en la base de datos.

Archivo: proyectos/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=255)
    long_desc = models.TextField()
    technologies = models.CharField(max_length=200)
    github_url = models.URLField()
    demo_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

Este modelo representa:
- title: nombre del proyecto (ej: Campus360)
- short_desc: resumen en 1 línea
- long_desc: descripción completa para mostrar en la vista de detalle
- technologies: listado breve (ej: Django, React Native)
- github_url: enlace al repositorio real
- demo_url: demo en línea (opcional)
- image: imagen representativa del proyecto (se sube en admin)

---

## 📥 Próximos pasos técnicos

1. Aplicar el modelo a la base de datos:
   python manage.py makemigrations
   python manage.py migrate

2. Registrar el modelo en proyectos/admin.py:

   from django.contrib import admin  
   from .models import Project  

   admin.site.register(Project)

3. Crear superusuario para acceder al panel de administración:
   python manage.py createsuperuser

4. Ingresar a http://127.0.0.1:8000/admin/ con el usuario creado y cargar los proyectos reales como Campus360, StudyMate, etc.

---
