from django.shortcuts import render, redirect
from templates import *

def getHome(request):
    return render(request, 'home/home.html')