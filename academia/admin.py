from django.contrib import admin

from .models import Academia

@admin.register(Academia)
class AcademiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'telefone', 'email')
    search_fields = ('nome', 'cidade', 'cnpj')
