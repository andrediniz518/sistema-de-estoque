# Sistema de Estoque – FASE 1 (CRUD Básico) 

##  Descrição
Este projeto é um **sistema de estoque básico** desenvolvido em **Python** com integração ao **MySQL**.  
O objetivo da **FASE 1** é implementar o **CRUD completo** (Create, Read, Update, Delete) de produtos, utilizando apenas o **terminal** como interface.

---

##  Funcionalidades
- Inserir produto → cadastrar nome, quantidade e preço.  
- Listar produtos → visualizar todos os produtos cadastrados.  
- Atualizar produto → alterar quantidade ou preço de um produto pelo ID.  
- Deletar produto → remover produto pelo ID.  
- Menu interativo no terminal → opções numeradas para navegar entre as funcionalidades.

---

##  Estrutura do projeto

```text
sistema-de-estoque/
│── conexao.py        # Conexão com o banco de dados
│── estoque.py        # Funções CRUD
│── main.py           # Menu principal da aplicação
```

## Banco de Dados

Crie o banco de dados executando o seguinte script no MySQL:

```sql
CREATE DATABASE estoque;

USE estoque;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10,2)
);
```

---

## Configuração

Instale a biblioteca necessária:

```bash
pip install mysql-connector-python
```

Depois, configure o arquivo `conexao.py` com suas credenciais:

```python
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="estoque"
    )
```

---

## Como Executar

No terminal, execute:

```bash
python main.py
```

#  Demonstração

##  Inserir Produto
<img width="281" height="190" alt="estoque-1" src="https://github.com/user-attachments/assets/d102f4a1-555a-4739-9524-172277ce7300" />

##  Listar Produtos
<img width="403" height="307" alt="estoque-2" src="https://github.com/user-attachments/assets/e5f07871-89ab-4fa7-93bb-74fe83fd2269" />

##  Atualizar Produto
<img width="301" height="189" alt="estoque-3" src="https://github.com/user-attachments/assets/0f421f02-e4ad-491a-ba5b-b71e0a151604" />

## Autor

Desenvolvido por **André Diniz**.
