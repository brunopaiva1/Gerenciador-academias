from django.db import models
from users.models import Usuario


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
