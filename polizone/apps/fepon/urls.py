from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fepon_view, name='fepon'), 
]