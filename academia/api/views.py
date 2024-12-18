"""
views da academia
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from academia.api.serializers import AcademiaSerializer
from academia.models import Academia


class AcademiaViewSet(ModelViewSet):
    """
    Criação da view Academia
    """

    serializer_class = AcademiaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Academia.objects.all()
