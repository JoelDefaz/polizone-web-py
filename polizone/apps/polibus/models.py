from django.db import models

class Ruta(models.Model):
    ruta = models.CharField(max_length=200)
    paradas = models.TextField()  # TextField para manejar textos largos como una lista de paradas
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"Ruta: {self.ruta}, Paradas: {self.paradas}, Horario: {self.horario}"