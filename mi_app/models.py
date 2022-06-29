from django.db import models
from unittest.util import _MAX_LENGTH

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Familia(models.Model):
    apellido_familia = models.CharField(max_length=50)
    cantidad_personas = models.IntegerField()

