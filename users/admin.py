from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero', 'endereço', 'aniversario', 'ativo', 'academia', 'data_cadastro')
    search_fields = ('user__username', 'numero', 'academia__nome')
    list_filter = ('ativo', 'academia')
    ordering = ('-data_cadastro',)
