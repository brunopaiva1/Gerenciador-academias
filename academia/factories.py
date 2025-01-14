import factory
from faker import Faker
from users.models import Usuario, Funcionario, Cliente
from academia.models import Academia

# Instância do Faker para gerar dados fictícios
fake = Faker()


class AcademiaFactory(factory.django.DjangoModelFactory):
    """
    Factory para criar objetos do modelo Academia.
    """

    class Meta:
        model = Academia

    nome = factory.Faker("company")
    endereco = factory.Faker("address")
    cnpj = factory.Faker("ean", length=13)
    telefone = factory.Faker("phone_number")


class UsuarioFactory(factory.django.DjangoModelFactory):
    """
    Factory para criar objetos do modelo Usuario.
    """

    class Meta:
        model = Usuario

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall("set_password", "senha123")
    is_active = True


class FuncionarioFactory(factory.django.DjangoModelFactory):
    """
    Factory para criar objetos do modelo Funcionario.
    """

    class Meta:
        model = Funcionario

    usuario = factory.SubFactory(UsuarioFactory)
    cargo = factory.Iterator(["Gerente", "Recepcionista", "Instrutor"])
    salario = factory.Faker("pydecimal", left_digits=4, right_digits=2,
                            positive=True)
    academia = factory.SubFactory(AcademiaFactory)
    ativo = True


class ClienteFactory(factory.django.DjangoModelFactory):
    """
    Factory para criar objetos do modelo Cliente.
    """

    class Meta:
        model = Cliente

    usuario = factory.SubFactory(UsuarioFactory)
    plano = factory.Iterator(["Mensal", "Semestral", "Anual"])
    ativo = True
    academia = factory.SubFactory(AcademiaFactory)
