from users.models import Usuario, Funcionario, Cliente


def listar_usuarios():
    """
    Retorna todos os usuários cadastrados.
    """
    return Usuario.objects.all()


def listar_funcionarios(filtros=None):
    """
    Retorna os funcionários com base nos filtros aplicados.
    """
    if filtros:
        return Funcionario.objects.filter(**filtros)
    return Funcionario.objects.all()


def listar_clientes(filtros=None):
    """
    Retorna os clientes com base nos filtros aplicados.
    """
    if filtros:
        return Cliente.objects.filter(**filtros)
    return Cliente.objects.all()
