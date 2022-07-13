from django.shortcuts import render
from django.http import  HttpResponse
from datetime import datetime
from mi_app.models import Familia,Curso,Estudiantes, Inscripcion
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario, InscripcionUniversidad

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo{fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

def mostrar_index(request):
    return render(request,"mi_app/index.html",{"mi_titulo":"Hola mi primer website!"})


def listar_cursos(request): #Vista
    context = {}
    context["cursos"] = Curso.objects.all() #Modelo
    return render(request,"mi_app/lista_cursos.html",context) #Template

   
def familia(request):
    context = {}
    context["familia"] = Familia.objects.all()
    return render(request,"mi_app/familia.html",context)

def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiantes.objects.all()
    return render(request,"mi_app/lista_estudiantes.html",context)


def formulario_curso(request):
    if request.method == "POST":
        pass
    else:
        mi_formulario = CursoFormulario(request.POST)
        return render(request,"mi_app/curso_formulario.html",{"mi_formulario":mi_formulario})


def formulario_busqueda(request):
    if request.GET:
        busqueda_curso = CursoBusquedaFormulario()
        criterio = busqueda_curso.cleaned_data
        cursos = Curso.objects.filter(nombre=criterio).all()
        return render(request,"mi_app/buscar.html",{"cursos":cursos})

    return render(request,"mi_app/buscar.html")

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