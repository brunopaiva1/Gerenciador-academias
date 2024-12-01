from django.db import models
from users.models import Usuario


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
