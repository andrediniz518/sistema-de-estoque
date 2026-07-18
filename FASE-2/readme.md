# 📦 Sistema de Estoque – FASE 2

## 🚀 Objetivo

Evoluir o sistema de estoque da FASE 1 para uma versão mais robusta, com novos campos, relatórios, movimentação de estoque, validações e interface melhorada.

## 📂 Alterações realizadas

### 1. Banco de dados

Adição de novos campos na tabela produtos:

- fornecedor
- data_lancamento
- categoria
- sku

### 2. Cadastro de produto

Função `inserir_produto()` atualizada para receber os novos campos.

Implementação de validações:

- Quantidade ≥ 0 e inteira
- Preço ≥ 0 e numérico
- Data válida no formato AAAA-MM-DD
- Nome, fornecedor, categoria e SKU não podem ser vazios

### 3. Relatórios

- Relatório de estoque baixo
- Relatório por fornecedor
- Relatório de lançamentos recentes
- Saída formatada com `tabulate`

### 4. Movimentação de estoque

- Função `registrar_entrada()` → adiciona quantidade ao estoque (valida quantidade > 0 e ID existente).
- Função `registrar_saida()` → subtrai quantidade do estoque (valida quantidade > 0, ID existente e evita estoque negativo).

### 5. Menu do terminal

Menu principal atualizado com opções para relatórios e movimentação.

Uso de `colorama` para cores diferenciadas em cada opção.

### 6. Interface melhorada

- Cores aplicadas com `colorama`.
- Tabelas organizadas com `tabulate`.
- Mensagens de feedback claras (sucesso, erro, alerta).

## 📂 Dependências

Instale os pacotes necessários:

```bash
pip install mysql-connector-python tabulate colorama
```

## 📂 Estrutura de arquivos

```text
estoque.py         # Funções CRUD + validações
relatorios.py      # Funções de relatórios
movimentacao.py    # Funções de entrada e saída
main_terminal.py   # Menu principal com integração
conexao.py         # Conexão com MySQL
```

## ✅ Resultado da FASE 2

- Sistema robusto e confiável.
- Evita dados inválidos no banco.
- Relatórios claros e organizados.
- Movimentação de estoque funcional e segura.
- Interface amigável com cores e tabelas.

## 📌 Próximos passos (FASE 3)

- Login de usuários com permissões (admin, operador).
- Exportação de relatórios (CSV/Excel).
- Histórico de movimentações para rastrear entradas e saídas.
- Interface gráfica ou versão web.
