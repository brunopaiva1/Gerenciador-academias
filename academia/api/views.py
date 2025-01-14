from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from academia.api.serializers import AcademiaSerializer
from academia.services import listar_academias


class AcademiaViewSet(ModelViewSet):
    """
    Criação da view Academia
    """

    serializer_class = AcademiaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        """
        Sobrescreve o método para usar a camada de serviços.
        """
        return listar_academias()
