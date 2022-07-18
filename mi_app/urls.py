from django.contrib import admin
from django.urls import path
from mi_app.views import busqueda_auto,idioma_formulario, mostrar_index,universidad_formulario,auto_formulario

#entregable
urlpatterns = [
    path("mi-pagina/",mostrar_index),
    path("universidad/",universidad_formulario),
    path("auto/",auto_formulario),
    path("idioma/",idioma_formulario),
    path("busqueda_auto/",busqueda_auto)
        ]