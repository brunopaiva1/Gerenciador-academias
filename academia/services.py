from academia.models import Academia


def listar_academias():
    """
    Retorna todas as academias cadastradas.
    """
    return Academia.objects.all()
