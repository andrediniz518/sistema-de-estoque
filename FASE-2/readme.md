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

### 6. Interface melhorada

- Tabelas organizadas com `tabulate`.
- Mensagens de feedback claras (sucesso, erro, alerta).

## 📂 Dependências

Instale os pacotes necessários:

```bash
pip install mysql-connector-python tabulate datetime
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
- Interface amigável e com tabelas.


# Demonstração

## Novos Campos Relatórios e Movimentação de estoque
<img width="272" height="156" alt="FASE-2 IMG 1" src="https://github.com/user-attachments/assets/108935ab-24d5-4524-939c-373df68027b5" />

## Campo listar produtos melhorado com tabelas
<img width="345" height="562" alt="FASE-2 IMG 4" src="https://github.com/user-attachments/assets/0f7a7fdc-0199-4b58-9b3c-36786160ccf0" />

## Relatórios
<img width="280" height="99" alt="FASE-2 IMG 2" src="https://github.com/user-attachments/assets/2e1bc510-85eb-4d3b-aef9-31c51409b87a" />

## Movimentação de estoque
<img width="283" height="74" alt="FASE-2 IMG 3" src="https://github.com/user-attachments/assets/b1054b69-03b5-462e-be82-f647bf573ae2" />


## 📌 Próximos passos (FASE 3)

- Login de usuários com permissões (admin, operador).
- Exportação de relatórios (CSV/Excel).
- Histórico de movimentações para rastrear entradas e saídas.
- Interface gráfica ou versão web.


# Autor

Desenvolvido por **André Diniz**
