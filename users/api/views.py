from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.api.serializers import UsuarioSerializer, ClienteSerializer, FuncionarioSerializer

from users.models import Usuario, Cliente, Funcionario


class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'put']


class FuncionarioViewSet(ModelViewSet):

    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()


class ClienteViewSet(ModelViewSet):

    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
