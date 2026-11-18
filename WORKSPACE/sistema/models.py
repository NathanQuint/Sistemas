from django.db import models #ORM do Django para delcarar modelos no banco de dados.
from django.utils import timezone # Util pra gerar data/hora atual do projeto 

# Modelo que representa um Paciente.
# Atributos=> Nome, sobrenome, email, telefone, data de cadastro, mensagem, ativo(True/False).
# CharField = Limite 255 caracteres
# TextField = Limite > 255 caracteres
class Paciente(models.Model):
    nome = models.CharField(max_length=25) #Nome do paciente
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente
    email = models.EmailField() #Email do paciente
    telefone = models.CharField(max_length=20) # Telefone do paciente
    cpf = models.CharField(max_length=11)
    data_cadastro = models.DateTimeField(default = timezone.now) # Data/hora do cadastro
    mensagem = models.TextField(blank=True) # Campo opcional. Livre para mensagem
    ativo = models.BooleanField(default=True) #Campo de exclusão Logica.

    def __str__(self):
        return f'{self.nome}, {self.sobrenome}'


class Medico(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    data_criacao = models.DateTimeField(default= timezone.now)
    telefone = models.CharField(max_length=20)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=70)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome}, {self.sobrenome}'

    # Modelo que representa uma consulta
    # id, id do paciente, ido do medico, horario/data, obs, status
class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # Chave estrangeira
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # Chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) # Data/hora Consulta
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )
