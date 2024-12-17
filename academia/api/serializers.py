"""
Serializers da academia
"""
from rest_framework.serializers import ModelSerializer
from academia.models import Academia


class AcademiaSerializer(ModelSerializer):
    """
    Criação do Serializer para a Academia
    """

    class Meta:
        """
        Criação da Classe Meta
        """

        model = Academia
        fields = "__all__"
