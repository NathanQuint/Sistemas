from django.contrib import admin

from sistema import models


@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','cpf','endereco','telefone','ativo','data_cadastro',)


@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina','idade', 'cpf', 'endereco', 'telefone', 'ativo', 'data_cadastro',)


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma','turno','ativo', 'data_cadastro','observacao')