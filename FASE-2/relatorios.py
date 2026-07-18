from conexao import conectar
from tabulate import tabulate

def relatorio_estoque_baixo():
    # Mostra produtos com estoque abaixo de 5 unidades.
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """ 
        SELECT id, nome, quantidade, preco FROM produtos 
        WHERE quantidade < 5
    """ 
    cursor.execute(sql)
    resultados = cursor.fetchall()
    print('\n=== RELATÓRIO: ESTOQUE BAIXO ===')
    print(tabulate(resultados, headers=["ID", "Nome", "Qtd", "Preço"], tablefmt="grid"))
    conexao.close()


def relatorio_por_fornecedor(fornecedor):
    # Mostra os produtos de um determinado fornecedor
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """ 
        SELECT id, nome, quantidade, preco FROM produtos
        WHERE fornecedor = %s
    """
    cursor.execute(sql, (fornecedor,))
    resultados = cursor.fetchall()
    print(f'\n=== RELATÓRIO: PRODUTOS DO FORNECEDOR {fornecedor} ===')
    print(tabulate(resultados, headers=["ID", "Nome", "Qtd", "Preço"], tablefmt="grid"))
    conexao.close()

def relatorio_lancamentos_recentes():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """ 
        SELECT id, nome, data_lancamento 
        FROM produtos 
        WHERE data_lancamento >= CURDATE() - INTERVAL 30 DAY
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    if resultados:
        print("\n=== RELATÓRIO: LANÇAMENTOS RECENTES ===")
        print(tabulate(resultados, headers=["ID", "Nome", "Data"], tablefmt="grid"))
    else:
        print('Nenhum resultado encontrado.')
    conexao.close()