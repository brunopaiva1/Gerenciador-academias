from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from academia.api.serializers import AcademiaSerializer
from academia.models import Academia


class AcademiaViewSet(ModelViewSet):

    serializer_class = AcademiaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Academia.objects.all()
