from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cafeteria_view, name='cafeteria'), 
]