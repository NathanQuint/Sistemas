from django import forms
from sistema.models import Consulta


STATUS = [
    ('A', 'Agendada'),
    ('X', 'Cancelada'),
    ('C', 'Confirmada'),
    ('R', 'Realizada'),
]

class ConsultaForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[('', 'Selecione o estado da consulta')] + STATUS, 
        label='Status'
    )

    class Meta:
        model = Consulta
        fields = ['observacao','status']
        labels = {
            'observacao': 'Observação',
            'status': 'Status',
        }