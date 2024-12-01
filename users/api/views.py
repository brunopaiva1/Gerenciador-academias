from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UsuarioSerializer

from users.models import Usuario

class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'put']
