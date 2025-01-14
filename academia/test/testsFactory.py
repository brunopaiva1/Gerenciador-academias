import pytest
from academia.factories import FuncionarioFactory, ClienteFactory
from academia.factories import AcademiaFactory
from users.models import Funcionario


@pytest.mark.django_db
def test_funcionario_creation():
    """
    Teste básico para criação de funcionário
    """
    funcionario = FuncionarioFactory.create()
    assert funcionario.cargo in ["Gerente", "Recepcionista", "Instrutor"]
    assert funcionario.ativo is True

 
@pytest.mark.django_db
def test_funcionario_inativo():
    """
    Teste para verificar a inatividade de um funcionário
    """
    funcionario = FuncionarioFactory.create(ativo=False)
    assert funcionario.ativo is False


@pytest.mark.django_db
def test_funcionario_associado_academia():
    """
    Teste para verificar se um funcionário pertence a uma academia
    """
    academia = AcademiaFactory.create(nome="Academia Top Fitness")
    funcionario = FuncionarioFactory.create(academia=academia)
    assert funcionario.academia.nome == "Academia Top Fitness"


@pytest.mark.django_db
def test_funcionario_unique_cargo():
    """
    Teste para verificar se funcionários possuem cargos únicos
    """
    gerente = FuncionarioFactory.create(cargo="Gerente")
    instrutor = FuncionarioFactory.create(cargo="Instrutor")
    assert gerente.cargo != instrutor.cargo


@pytest.mark.django_db
def test_cliente_creation_with_plano():
    """
    Teste para criação de cliente associado a um plano
    """
    cliente = ClienteFactory.create(plano="Mensal")
    assert cliente.plano == "Mensal"
    assert cliente.ativo is True


@pytest.mark.django_db
def test_funcionarios_ativos_count():
    """
    Teste para verificar funcionários ativos na base
    """
    FuncionarioFactory.create_batch(5, ativo=True)
    FuncionarioFactory.create_batch(2, ativo=False)
    assert Funcionario.objects.filter(ativo=True).count() == 5


@pytest.mark.django_db
def test_funcionario_creation_no_exceptions():
    """
    Teste para verificar que uma exceção não é levantada na criação de
    funcionário
    """
    try:
        FuncionarioFactory.create()
    except Exception as e:
        pytest.fail(f"Ocorreu uma exceção inesperada: {e}")
