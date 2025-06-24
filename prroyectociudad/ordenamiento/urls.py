from django.urls import path
from . import views

urlpatterns = [
    path('parroquias/', views.listar_parroquias_barrios, name='listar_parroquias'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
]
