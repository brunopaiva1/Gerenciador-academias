## 1. SISTEMA DE GERENCIAMENTO DE ACADEMIA

O **Sistema de Reserva de Academia** é uma aplicação para gerenciar academias, clientes e funcionários. Permite cadastrar, editar e listar informações, além de aplicar controle de acesso e permissões de usuários.

## 2. APPS

### 2.1. **academia**
- **Objetivo**: Gerenciar informações das academias.
- **Principais Componentes**:
  - **Modelo**: `Academia` (nome, endereço, CNPJ, horários, mensalidade, etc.).
  - **ViewSet**: `AcademiaViewSet` para listar, criar, editar e excluir academias.

### 2.2. **users**
- **Objetivo**: Gerenciar clientes, funcionários e usuários.
- **Principais Componentes**:
  - **Modelos**: 
    - `Usuario`: Base para Cliente e Funcionário.
    - `Cliente`: Contém informações de plano e validade.
    - `Funcionario`: Contém informações de cargo, salário e horário de trabalho.
  - **ViewSets**: `UsuarioViewSet`, `ClienteViewSet`, `FuncionarioViewSet` para listar, criar, editar e excluir dados.

## 3. Changelog e Melhorias Futuras

### Melhorias a serem implementadas:
1. **Tratamento de Exceções**:
   - Personalizar mensagens de erro (404, 500, etc.).
   - Validar dados de entrada e exibir mensagens claras.

2. **Novas Funcionalidades**:
   - **Reserva de Horários**: Permitir que clientes reservem horários de acesso à academia.
   - **Relatórios**: Gerar relatórios de frequência e desempenho.
   - **Notificações**: Alertar clientes sobre o vencimento de planos.

