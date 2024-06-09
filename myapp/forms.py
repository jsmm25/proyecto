# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente, Reserva

class RegistroForm(UserCreationForm):
    # Agrega campos adicionales si es necesario
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ReservaForm(forms.ModelForm):
    # Agrega campos adicionales si es necesario
    class Meta:
        model = Reserva
        fields = '__all__'  # Puedes especificar los campos que deseas mostrar en el formulario
