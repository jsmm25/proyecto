# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('lista_reservas/', views.lista_reservas, name='lista_reservas'),
    path('hacer_reservacion/', views.hacer_reservacion, name='hacer_reservacion'),
    # Otras rutas que puedas tener en tu aplicación...
]
