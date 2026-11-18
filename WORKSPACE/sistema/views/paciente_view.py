from django.http import HttpResponse # Utilizado qnd n se tem html pronto. Feito pra testar se a função esta rodando corretamente
from django.shortcuts import render

from sistema.models import Paciente

def index_paciente(request):
    return render(
        request, 
        'index.html',
        )


#View responsavel por listar todos os pacientes
# def listarPaciente(request):
#     pacientes = Paciente.objects.all() # -> [obj1,obj2,obj3]

#     context = {
#         'pacientes': pacientes,
#     }


#     return render(
#         request,
#         'paciente/listar.html',
#         context,
#         )










# GLOBAL -> A uma página inteira
# PARTIALS -> Uma parte da página(header, footer, aside, formulario)

# SPA

# MVT -> Template/golba/base.hmtl