from django.shortcuts import render, redirect
from .models import Parroquia,Barrio
from .forms import ParroquiaForm, BarrioForm

def listar_parroquias_barrios(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'listar_parroquias.html', {'parroquias': parroquias})

def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'listar_barrios.html', {'barrios': barrios})

def crear_parroquia(request):
    form = ParroquiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_parroquias')
    return render(request, 'crear_parroquia.html', {'form': form})

def crear_barrio(request):
    form = BarrioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_barrios')
    return render(request, 'crear_barrio.html', {'form': form})

