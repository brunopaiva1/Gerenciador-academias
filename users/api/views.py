from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.api.serializers import UsuarioSerializer, ClienteSerializer, FuncionarioSerializer
from users.services import listar_usuarios, listar_funcionarios, listar_clientes


class UsuarioViewSet(ModelViewSet):
    """
    Criação da view de Usuario
    """

    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "put"]

    def get_queryset(self):
        """
        Usa a camada de serviços para obter os usuários.
        """
        return listar_usuarios()


class FuncionarioViewSet(ModelViewSet):
    """
    Criação da view de Funcionario
    """

    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["cargo", "ativo", "academia"]

    def get_queryset(self):
        """
        Usa a camada de serviços para obter os funcionários com base nos filtros.
        """
        filtros = {key: self.request.query_params[key] for key in self.filterset_fields if key in self.request.query_params}
        return listar_funcionarios(filtros)


class ClienteViewSet(ModelViewSet):
    """
    Criação da view de Cliente
    """

    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["plano", "ativo", "academia"]

    def get_queryset(self):
        """
        Usa a camada de serviços para obter os clientes com base nos filtros.
        """
        filtros = {key: self.request.query_params[key] for key in self.filterset_fields if key in self.request.query_params}
        return listar_clientes(filtros)
