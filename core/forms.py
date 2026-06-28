from django import forms
from .models import Paciente, Atendimento
import re

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'telefone', 'email']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf = re.sub(r'\D', '', cpf) # Remove pontos e traços temporariamente
        
        if len(cpf) != 11:
            raise forms.ValidationError("O CPF deve conter exatamente 11 dígitos numéricos.")
            
        # Guarda o CPF formatado de forma limpa no banco de dados
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Introduza o histórico médico / evolução clínica do paciente...'}),
        }