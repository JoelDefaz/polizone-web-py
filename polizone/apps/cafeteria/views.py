from django.shortcuts import render, redirect
from templates import *

def cafeteria_view(request):
    menu_items = [
        {
            'nombreMenu': 'Café',
            'descripcionMenu': 'Café caliente recién hecho',
            'tipoMenu': 'Bebida',
            'precio': 1.50
        },
        {
            'nombreMenu': 'Sandwich',
            'descripcionMenu': 'Sandwich de jamón y queso',
            'tipoMenu': 'Alimento',
            'precio': 2.50
        },
    ]
    return render(request, 'cafeteria/cafeteria.html',{'menu_items': menu_items})