from django.contrib import admin
from django.urls import path
from mi_app.views import saludo,saludar_a,mostrar_index,listar_cursos,familia,listar_estudiantes,formulario_curso,formulario_busqueda,universidad_formulario


urlpatterns = [
    path("mi-pagina/",mostrar_index),
    path("saludar/",saludo),
    path("saludar/persona/<nombre>",saludar_a),
    path("listar-cursos/",listar_cursos),
    path("familia/",familia),
    path("listar_estudiantes/",listar_estudiantes),
    path("formulario/",formulario_curso),
    path("buscar/",formulario_busqueda),
    path("universidad/",universidad_formulario)
        ]