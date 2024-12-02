from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from cliente.api.serializers import ClienteSerializer
from cliente.models import Cliente


class ClienteVewSet(ModelViewSet):

    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
