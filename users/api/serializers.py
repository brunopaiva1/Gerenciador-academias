from rest_framework import serializers
from users.models import Usuario, Cliente, Funcionario


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Criaçaõ do serializer para Usuario
    """
    class Meta:
        """
        Criação da Classe Meta
        """
        model = Usuario
        fields = "__all__"


class FuncionarioSerializer(serializers.ModelSerializer):
    """
    Criação do serializer para Funcionario
    """
    class Meta:
        """
        Criação da Classe Meta
        """
        model = Funcionario
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    """"
    Criação do serializer de Cliente
    """
    class Meta:
        """
        Criação da Classe Meta
        """
        model = Cliente
        fields = "__all__"
