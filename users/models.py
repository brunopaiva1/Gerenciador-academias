from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=12)
    endereço = models.CharField(max_length=150)
    aniversario = models.DateField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    academia = models.ForeignKey('academia.Academia', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Cliente(Usuario):

    plano = models.CharField(max_length=50)
    data_inicio_plano = models.DateField()
    data_fim_plano = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.user.username} - Cliente"


class Funcionario(Usuario):

    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()
    horario_trabalho_inicio = models.TimeField()
    horario_trabalho_fim = models.TimeField()

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f"{self.user.username} - Funcionário"
