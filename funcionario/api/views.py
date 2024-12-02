from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from funcionario.api.serializers import FuncionarioSerializer
from funcionario.models import Funcionario


class FuncionarioViewSet(ModelViewSet):

    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()
