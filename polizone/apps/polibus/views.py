from django.shortcuts import render, redirect
from .models import Ruta
from .forms import RutaForm
from templates import *

def polibus_view(request):
    rutas = Ruta.objects.all()
    context = {
        'rutas': rutas,
    }
    return render(request, 'polibus/rutas.html', context)

def add_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva ruta en la base de datos
            return redirect('polibus')  # Redirige a la lista de rutas
    else:
        form = RutaForm()

    return render(request, 'polibus/add_rutas.html', {'form': form})