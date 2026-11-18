from django.urls import path
from sistema.views import *

urlpatterns = [
    path('paciente/', index_paciente), # vollmed.com/paciente
    # path('paciente/novo/',), # vollmed.com/paciente/novo
    # path('paciente/perfil/<int:paciente_id>/',), # vollmed.com/paciente/perfil/<int:paciente_id>
    # path('paciente/listagem/', listarPaciente), # vollmed.com/paciente/listagem
]

