from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'salario', 'data_admissao', 'academia', 'ativo')
    search_fields = ('user__username', 'cargo', 'academia__nome')
    list_filter = ('cargo', 'academia', 'ativo')
    ordering = ('-data_admissao',)
