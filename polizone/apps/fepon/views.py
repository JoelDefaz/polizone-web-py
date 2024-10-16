from django.shortcuts import render, redirect
from templates import *

def fepon_view(request):
    asociaciones = [
        {
            'nombre': 'Asociación de Estudiantes',
            'descripcion': 'Grupo que representa los intereses de los estudiantes.'
        },
        {
            'nombre': 'Club de Robótica',
            'descripcion': 'Promueve el aprendizaje y la práctica de la robótica.'
        },
    ]
    return render(request, 'fepon/fepon.html',{'asociaciones': asociaciones})
