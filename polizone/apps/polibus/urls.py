from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.polibus_view, name='polibus'),
    path('add_ruta/', views.add_ruta, name='add_ruta'),
]