from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    puntos_totales = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.nacionalidad}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fundacion = models.DateField()
    campeonatos = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.pais}"

class Circuito(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    longitud_km = models.FloatField()
    record_vuelta = models.CharField(max_length=100)

    def __str__(self):

        return f"{self.nombre} --- {self.pais}"
    

class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.imagen}"