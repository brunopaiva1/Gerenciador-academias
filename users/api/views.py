"""
views da api do usuario
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from users.api.serializers import UsuarioSerializer, ClienteSerializer
from users.api.serializers import FuncionarioSerializer
from users.models import Usuario, Cliente, Funcionario


class UsuarioViewSet(ModelViewSet):
    """
    ViewSet para operações de leitura e atualização de Usuários.
    """
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'put']

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao listar usuários.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({'erro': 'Usuário não encontrado.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'erro': 'Erro ao buscar usuário.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao atualizar usuário.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FuncionarioViewSet(ModelViewSet):
    """
    ViewSet para operações de CRUD de Funcionários.
    """
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()
    filterset_fields = ['cargo', 'ativo', 'academia']

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao listar funcionários.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({'erro': 'Funcionário não encontrado.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'erro': 'Erro ao buscar funcionário.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao criar funcionário.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClienteViewSet(ModelViewSet):
    """
    ViewSet para operações de CRUD de Clientes.
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    filterset_fields = ['plano', 'ativo', 'academia']

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao listar clientes.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({'erro': 'Cliente não encontrado.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'erro': 'Erro ao buscar cliente.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
            return Response({'erro': 'Erro ao criar cliente.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
