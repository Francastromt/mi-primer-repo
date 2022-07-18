from django.shortcuts import render
from django.http import  HttpResponse
from datetime import datetime
from mi_app.models import  Inscripcion,Auto,Idioma
from mi_app.forms import BusquedaFormularioAuto, InscripcionUniversidad,MiAuto,MiIdioma

def mostrar_index(request):
    return render(request,"mi_app/index.html",{"mi_titulo":"Hola mi primer website!"})

def universidad_formulario(request):
    if request.method == "POST":
        miformulario = InscripcionUniversidad(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            orientacion = Inscripcion(nombre=informacion["nombre"],apellido=informacion["apellido"],edad=informacion["edad"],carrera=informacion["carrera"],horario=informacion["horario"])
            orientacion.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario = InscripcionUniversidad()

    return render(request,"mi_app/universidad.html",{"miformulario":miformulario})

def auto_formulario(request):
    if request.method == "POST":
        miformulario2 = MiAuto(request.POST)
        print(miformulario2)
        if miformulario2.is_valid:
            informacion2 = miformulario2.cleaned_data
            orientacion2 = Auto(marca=informacion2["marca"],modelo=informacion2["modelo"])
            orientacion2.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario2 = MiAuto()

    return render(request,"mi_app/auto.html",{"miformulario2":miformulario2})


def idioma_formulario(request):
    if request.method == "POST":
        miformulario3 = MiIdioma(request.POST)
        print(miformulario3)
        if miformulario3.is_valid:
            informacion3 = miformulario3.cleaned_data
            orientacion3 = Idioma(idioma=informacion3["idioma"],conocimiento=informacion3["conocimiento"])
            orientacion3.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario3 = MiIdioma()

    return render(request,"mi_app/idioma.html",{"miformulario3":miformulario3})


def busqueda_auto(request):
    
    busqueda_formulario = BusquedaFormularioAuto()

    if request.GET:
        autos = Auto.objects.filter(marca=busqueda_formulario["criterio"]).all()
        return render(request,"mi_app/busqueda_auto.html",{"autos":autos})
    
    return render(request,"mi_app/busqueda_auto.html",{"busqueda_formulario":busqueda_formulario})
