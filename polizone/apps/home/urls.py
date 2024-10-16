from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getHome, name='home'), 
    path('cafeteria/', include('apps.cafeteria.urls')),
    path('polibus/', include('apps.polibus.urls')),
    path('fepon/', include('apps.fepon.urls')),
]