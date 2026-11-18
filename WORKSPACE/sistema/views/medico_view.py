from django.shortcuts import render
from django.http import HttpResponse


#View responsavel pela tela inicial do medico
def medico_view(request):
    print('Pagina medico rodou')
    return HttpResponse('Página Inicial do medico')