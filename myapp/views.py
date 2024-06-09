# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, ReservaForm  # Corrige la importación del formulario
from .models import Cliente, Reserva

def inicio(request):
    return render(request, 'myapp/inicio.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'myapp/lista_clientes.html', {'clientes': clientes})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'myapp/lista_reservas.html', {'reservas': reservas})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('hacer_reservacion')
    else:
        form = RegistroForm()

    return render(request, 'myapp/registro.html', {'form': form})

def hacer_reservacion(request):
    return render(request, 'myapp/hacer_reservacion.html')
