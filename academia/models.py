from django.db import models


class Academia(models.Model):
    """
    Criação dos campos da api de academia
    """
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    mensalidade_padrao = models.DecimalField(max_digits=10, decimal_places=2,
                                             blank=True, null=True)

    def __str__(self):
        return f'Academia {self.nome}'

    class Meta:
        """
        Criação da classe meta
        """
        app_label = 'academia'
        verbose_name = 'Academia'
        verbose_name_plural = 'Academias'
