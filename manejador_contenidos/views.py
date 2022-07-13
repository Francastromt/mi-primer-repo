from django.shortcuts import render

def mostrar_home(request):
    return render(request,"manejador_contenidos/home.html",{})

def mostrar_profile(request):
    return render(request,"manejador_contenidos/profile.html",{})
