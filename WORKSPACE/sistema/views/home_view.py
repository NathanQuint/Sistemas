from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    print("Home rodou")
    return HttpResponse("Caminho home html")