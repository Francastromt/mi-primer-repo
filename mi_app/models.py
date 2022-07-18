from django.db import models
from unittest.util import _MAX_LENGTH

#entregable
class Inscripcion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

class Auto(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.IntegerField()

class Idioma(models.Model):
    idioma = models.CharField(max_length=40)
    conocimiento = models.CharField(max_length=40)

