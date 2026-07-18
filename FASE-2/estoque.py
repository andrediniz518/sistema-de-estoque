from conexao import conectar

def inserir_produtos(nome, quantidade, preco, 
                    fornecedor, data_lancamento, categoria, sku):
    conn = conectar()
    cursor = conn.cursor()
    sql = """ 
        INSERT INTO produtos
        (nome, quantidade, preco,
        fornecedor, data_lancamento, categoria, sku)
        values
        (%s, %s, %s, %s, %s, %s, %s)
    """  
    valores = (nome, quantidade, preco, fornecedor,
    data_lancamento, categoria, sku,)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    sql = """ 
        SELECT * FROM produtos
    """
    cursor.execute(sql)
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    conn.close()


def atualizar_produto(id, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """ 
        UPDATE produtos
        set quantidade = %s, preco = %s
        WHERE id = %s
    """
    valores = (quantidade, preco, id)
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


def deletar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        DELETE FROM produtos
        where id = %s
    """
    cursor.execute(sql, (id,))
    conexao.commit()
    conexao.close()