from django.db import models
from unittest.util import _MAX_LENGTH

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.camada}"

class Familia(models.Model):
    apellido_familia = models.CharField(max_length=50)
    cantidad_personas = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

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

