from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='atendimentos', verbose_name="Paciente")
    data_atendimento = models.DateTimeField(auto_now_add=True, verbose_name="Data do Atendimento")
    descricao = models.TextField(verbose_name="Descrição do Atendimento / Evolução Clínica")

    def __str__(self):
        return f"Atendimento de {self.paciente.nome} em {self.data_atendimento.strftime('%d/%m/%Y')}"