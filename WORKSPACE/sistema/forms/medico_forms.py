from django import forms
from sistema.models import Medico

ESPECIALIDADES = [
    ('CARDIOLOGIA', 'Cardiologia')
    ('DERMATOLOGIA', 'Dermatologia'),
    ('GINECOLOGIA', 'Ginecologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('OFTALMOLOGIA', 'Oftalmologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]


class MedicoForm(forms.ModelForm):
    especialidade = forms.ChoiceField(
        choices=[('','Selecione uma especialidade')] + ESPECIALIDADES,
        label='Especialidade'
    )


    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone','crm', 'especialidade',]
        #criacao_data e ativo nao aparecerem, são preenchidos automaticamente
        labels = {
            'nome': 'Nome',
            'sobrenome' : 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'crm': 'CRM',
            'especialidade': 'Especialidade',
        }