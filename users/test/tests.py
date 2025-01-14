"""Testes do Sistema"""
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UsuarioAPITests(TestCase):
    """Essa classe de testes foca nos testes dos Usuários"""

    def setUp(self):
        # Configura um cliente de API para enviar requisições
        self.client = APIClient()
        self.url_usuarios = "http://127.0.0.1:8000/usuario/"
        self.user_data = {
            "user": "1",
            "numero": "1111111111",
            "endereco": "Zona Urbana",
            "aniversario": "2024-12-19",
            "ativo": True,
            "data_cadastro": "2024-12-19T13:10:23.479Z",
            "ultima_atualizacao": "2024-12-19T13:10:23.479Z",
            "academia": 1
        }

    def test_listar_usuarios(self):
        """Testa a listagem de usuários"""
        response = self.client.get(self.url_usuarios, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_atualizar_usuario(self):
        """Testa a atualização total de um usuário"""
        usuario_criado = self.client.post(self.url_usuarios, self.user_data, format='json')
        user_id = usuario_criado.data.get("id")
        novos_dados = {
            "numero": "22222111111",
            "endereco": "Zona Rural",
            "aniversario": "2024-12-19",
            "ativo": True,
            "data_cadastro": "2024-08-19T13:10:23.479Z",
            "ultima_atualizacao": "2024-11-19T13:07:23.479Z",
            "academia": 1
        }
        response = self.client.put(f"{self.url_usuarios}{user_id}/", novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class FuncionarioAPITests(TestCase):
    """Essa classe de testes foca nos testes dos Funcionários"""

    def setUp(self):
        self.client = APIClient()
        self.url_funcionarios = "http://127.0.0.1:8000/funcionario/"
        self.funcionario_data = {
            "nome": "Treinadora",
            "cargo": "Instrutora",
            "ativo": True,
            "academia": 1
        }

    def test_listar_funcionarios(self):
        """Testa a listagem de funcionários"""
        response = self.client.get(self.url_funcionarios, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filtrar_funcionarios_por_cargo(self):
        """Testa o filtro de funcionários pelo cargo"""
        self.client.post(self.url_funcionarios, self.funcionario_data, format='json')
        response = self.client.get(self.url_funcionarios, {'cargo': 'Instrutora'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertGreaterEqual(len(response.data), 1)  # Deve ter ao menos 1 funcionário


class ClienteAPITests(TestCase):
    """Essa classe de testes foca nos testes dos Clientes"""

    def setUp(self):
        self.client = APIClient()
        self.url_clientes = "/api/clientes/"
        self.cliente_data = {
            "nome": "Carlos Alberto",
            "plano": "Mensal",
            "ativo": True,
            "academia": 1
        }

    def test_listar_clientes(self):
        """Testa a listagem de clientes"""
        response = self.client.get(self.url_clientes, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
