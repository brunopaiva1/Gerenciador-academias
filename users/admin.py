"""
django admin do usuario
"""
from django.contrib import admin
from .models import Usuario, Cliente, Funcionario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """
    Permissão de admin para a classe Usuario
    """

    list_display = (
        "user",
        "numero",
        "endereco",
        "aniversario",
        "ativo",
        "academia",
        "data_cadastro",
    )
    search_fields = ("user__username", "numero", "academia__nome")
    list_filter = ("ativo", "academia")
    ordering = ("-data_cadastro",)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    """
    Permissão de admin para a classe Funcionaro
    """

    list_display = ("user", "cargo", "salario", "data_admissao", "academia", "ativo")
    search_fields = ("user__username", "cargo", "academia__nome")
    list_filter = ("cargo", "academia", "ativo")
    ordering = ("-data_admissao",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Permissão de admin para a classe Cliente
    """

    list_display = (
        "user",
        "plano",
        "data_inicio_plano",
        "data_fim_plano",
        "ativo",
        "academia",
    )
    search_fields = ("user__username", "plano", "academia__nome")
    list_filter = ("plano", "academia", "ativo")
    ordering = ("-data_inicio_plano",)
