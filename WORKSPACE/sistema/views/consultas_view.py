from django.http import HttpResponse
from django.shortcuts import render

def consultas_view(request):
    print("Consultas view rodou")
    return HttpResponse("Caminho do html das consultas")