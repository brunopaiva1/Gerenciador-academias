"""
Modulo do administrador da academia
"""
from django.contrib import admin
from .models import Academia


@admin.register(Academia)
class AcademiaAdmin(admin.ModelAdmin):
    """
    Permissão de admin para a classe Academia
    """

    list_display = ("nome", "cidade", "estado", "telefone", "email")
    search_fields = ("nome", "cidade", "cnpj")
