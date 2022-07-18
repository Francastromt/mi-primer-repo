from django import forms

#entregable
class InscripcionUniversidad(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    carrera = forms.CharField()
    horario = forms.CharField()

class MiAuto(forms.Form):
    marca = forms.CharField()
    modelo = forms.IntegerField()

class MiIdioma(forms.Form):
    idioma = forms.CharField()
    conocimiento = forms.CharField()

class BusquedaFormularioAuto(forms.Form):
    criterio = forms.CharField()
