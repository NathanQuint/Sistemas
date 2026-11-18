from django.contrib import admin
from django.urls import path, include

import sistema.views
import sistema.urls





# VIEWS -> sempre retornam alguma coisa, sao funções, trabalham com REQUEST -> RESPONSE
# View responsavel pela tela inicial do medico



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(sistema.urls.py)), #Preciso chamar as urls do app sistema
    # path("") Preciso chamar as urls do app portal

]



# MVT (MVC)








# www.vollmed.online/
# www.vollmed.online/login
# www.vollmed.online/

# Medico
# www.vollmed.online/medico/id -> Perfil do medico
# www.vollmed.online/medico/id/alterar -> Altera cadastro medico

# www.vollmed.online/medico/id/consultas

# Paciente
# www.vollmed.online/paciente/id -> Perfil do paciente
# www.vollmed.online/paciente/id/alterar -> Altera cadastro paciente

# www.vollmed.online/paciente/id/consultas/cadastrar
# www.vollmed.online/paciente/id/consultas/id/ -> ver,alterar,deletar.


# Secretario/SUPERUSER

# www.vollmed.online/secretario/id -> Perfil do secretario
# www.vollmed.online/secretario/id/alterar -> Altera cadastro secretario

# www.vollmed.online/secretario/id/consultas/cadastrar
# www.vollmed.online/secretario/id/consultas/id/ -> ver,alterar,deletar.


# Consulta

