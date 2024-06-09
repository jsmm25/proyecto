# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    # Otros campos relevantes para el modelo Cliente

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Otros campos relevantes para el modelo Reserva

    def __str__(self):
        return f"Reserva de {self.cliente} el {self.fecha}"
