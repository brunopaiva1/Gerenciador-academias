"""
modulo das apps do usuario
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    classe de usuário config
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
