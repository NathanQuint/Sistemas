from django.contrib import admin

from sistema import models

@admin.register(models.Paciente) # Registrando a Classe Paciente no portal do Django
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'crm', 'ativo',)

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','paciente_id','medico_id', 'data_consulta',  'ativo', 'observacao', 'status',)