from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

#entregable
class InscripcionUniversidad(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    carrera = forms.CharField()
    horario = forms.CharField()
