from django.shortcuts import render
from .models import Project

def home(request):
    proyectos = Project.objects.all()
    return render(request, 'proyectos/home.html', {'proyectos': proyectos})
