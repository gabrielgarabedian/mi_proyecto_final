from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Gabriel"})

def index2(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", {"nombre":nombre, "apellido": apellido})