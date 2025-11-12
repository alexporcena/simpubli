from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('aleatorio/', views.aleatorio, name='aleatorio'),
    path('comparar/', views.comparar, name='comparar'),
]
