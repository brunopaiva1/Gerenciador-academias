from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'plano', 'data_inicio_plano', 'data_fim_plano', 'ativo', 'academia')
    search_fields = ('user__username', 'plano', 'academia__nome')
    list_filter = ('plano', 'academia', 'ativo')
    ordering = ('-data_inicio_plano',)
