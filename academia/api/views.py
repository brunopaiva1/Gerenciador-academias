"""
views da academia
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from academia.api.serializers import AcademiaSerializer
from academia.models import Academia


class AcademiaViewSet(ModelViewSet):
    """
    ViewSet para operações de CRUD de Academias.
    """

    serializer_class = AcademiaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Academia.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao listar academias.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({'erro': 'Academia não encontrada.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'erro': 'Erro ao buscar academia.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao criar academia.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao atualizar academia.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao deletar academia.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)