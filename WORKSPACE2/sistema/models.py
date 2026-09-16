from django.db import models
from django.utils import timezone # Util pra gerar data/hora atual do projeto 


class Aluno(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.nome}'

class Professor(models.Model):
    nome = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=30)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.nome}'


class Turma(models.Model):
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.CharField(max_length=30)
    turno = models.CharField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.turma}'