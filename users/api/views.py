from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.api.serializers import UsuarioSerializer, ClienteSerializer
from users.api.serializers import FuncionarioSerializer

from users.models import Usuario, Cliente, Funcionario


class UsuarioViewSet(ModelViewSet):
    """
    Criação da view de Usuario
    """
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'put']


class FuncionarioViewSet(ModelViewSet):
    """
    Criação da view de Funcionario
    """
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()
    filterset_fields = ['cargo', 'ativo', 'academia']


class ClienteViewSet(ModelViewSet):
    """
    Criação da view de Cliente
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    filterset_fields = ['plano', 'ativo', 'academia']
