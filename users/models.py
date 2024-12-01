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
