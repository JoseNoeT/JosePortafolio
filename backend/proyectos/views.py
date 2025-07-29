from django.shortcuts import render , get_object_or_404
from .models import Project

def home(request):
    proyectos = Project.objects.all()
    return render(request, 'proyectos/home.html', {
        'proyectos': proyectos
    })

def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Project, id=id)
    return render(request, 'proyectos/detalle.html', {'proyecto': proyecto})


def sobre_mi(request):
    return render(request, 'proyectos/sobre_mi.html')
