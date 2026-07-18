from conexao import conectar

def verificar_produto(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """ 
        SELECT COUNT(*) FROM produtos
        WHERE id = %s
    """
    cursor.execute(sql, (produto_id,))
    existe = cursor.fetchone()[0] > 0
    conexao.close()
    return existe


def registrar_compra(produto_id, quantidade):

    # verifica quantidade
    if quantidade <= 0:
        print('Quantidade de entrada deve ser maior que zero.')
        return


    if not verificar_produto(produto_id):
        print('Produto não encontrado. Verifique o ID.')
        return

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        UPDATE produtos
        SET quantidade = quantidade + %s
        WHERE id = %s 
    """
    cursor.execute(sql, (quantidade, produto_id))
    conexao.commit()
    print(f'Entrada registrada: +{quantidade} unidades no produto {produto_id}')
    conexao.close()


def registrar_venda(produto_id, quantidade):

    if quantidade <= 0:
        print('Quantidade de saída deve ser maior que zero.')
        return
    
    if not verificar_produto(produto_id):
        print('Produto não encontrado. Verifique o ID.')
        return

    conexao = conectar()
    cursor = conexao.cursor()

    # verifica se há quantidade suficiente no estoque
    # evita de ter estoque negativo
    sql_ = """ SELECT quantidade FROM produtos 
               WHERE id = %s """
    cursor.execute(sql_, (produto_id,))
    estoque_atual = cursor.fetchone()[0]

    if quantidade > estoque_atual:
        print('Erro: quantidade em estoque insuficiente!')
    else:
        sql = """
            UPDATE produtos
            SET quantidade = quantidade - %s
            WHERE id = %s
        """
        cursor.execute(sql, (quantidade, produto_id))
        conexao.commit()
        print(f'Venda registrada: -{quantidade} unidades no produto {produto_id}')
    conexao.close()