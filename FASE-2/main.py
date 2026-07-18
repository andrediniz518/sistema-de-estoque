from estoque import *
from relatorios import *
from movimentacao import *
from datetime import datetime


while True:
    print('\n=== SISTEMA DE ESTOQUE ===')
    print('1 - Inserir Produto')
    print('2 - Listar Produtos')
    print('3 - Atualizar Produto')
    print('4 - Deletar Produto')
    print('5 - Relatórios')
    print('6 - Movimentação de estoque')
    print('7 - Sair')

    while True:
        try:
            opc = int(input('Escolha uma opção: '))
            break
        except ValueError:
            print('Insira um valor válido!')

    if opc == 1:

        # Validação de nome 
        while True:
            nome = input('Nome do produto: ').strip()
            if len(nome)==0:
                print('O nome não pode estar vazio.')
            elif len(nome) > 100:
                print('O nome não pode ter mais que 100 caracter')
            else:
                break

        # Validação de quantidade
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                if quantidade <= 0:
                    print('Quantidade não pode ser negativa.')
                else:
                    break
            except ValueError:
                print('Digite um númerio inteiro válido.')

        # Validação de preço
        while True:
            try:
                preco = float(input('Preço: '))
                if preco < 0:
                    print('Preço não pode ser negativo.')
                else:
                    break
            except ValueError:
                print('Digite um valor numérico válido (ex.: 19.90).')

        # Validação de fornecedor
        while True:
            fornecedor = input('Fornecedor: ').strip()
            if len(fornecedor)==0:
                print('O nome do fornecedor não pode ser vazio.')
            elif len(fornecedor) > 100:
                print('O nome do forneceor não pode ultrapassar de 100 caracter')
            else:
                break

        # Validaçao da data de lançamento
        while True:
            data_lancamento = input('Data de lançamento (AAAA-MM-DD): ')
            try:
                datetime.strptime(data_lancamento, "%Y-%m-%d")
                break
            except ValueError:
                print('Data inválida. Use o formato AAAA-MM-DD.')
        
        # Validação de categoria
        while True:
            categoria = input('Categoria: ').strip()
            if len(categoria)==0:
                print('Nome da categoria não pode ser vazia.')
            elif len(categoria) > 50:
                print('Nome da categoria não pode ser maior que 50 caractere.')
            else:
                break

        # Validação de sku
        while True:
            sku = input('Sku: ').strip()
            if len(sku) == 0:
                print('Nome da categoria não pode ser vazia')
            elif len(sku) > 50:
                print('Sku não pode ser maior que 50 caractere.')
            else:
                break

        inserir_produtos(nome, quantidade, preco, fornecedor, data_lancamento, categoria, sku)
        print('Produto cadastrado com sucesso!')
    elif opc == 2:
        print('Produtos cadastrados')
        listar_produtos()
    elif opc == 3:
        id = int(input('ID do produto a atualizar: '))
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        atualizar_produto(id, quantidade, preco)
        print('Produto atualizado com sucesso!')
    elif opc == 4:
        id = int(input('ID do produto  a deletar: '))
        deletar_produto(id)
        print('Produto deletado com sucesso!')
    elif opc == 5:
        print("\n=== RELATÓRIOS ===")
        print("1 - Estoque baixo")
        print("2 - Por fornecedor")
        print("3 - Lançamentos recentes")
        sub = int(input("Escolha relatório: "))
        if sub == 1:
            relatorio_estoque_baixo()
        elif sub == 2:
            fornecedor = input("Digite o fornecedor: ")
            relatorio_por_fornecedor(fornecedor)
        elif sub == 3:
            relatorio_lancamentos_recentes()
        else:
            print('Opção inválida!')
    elif opc == 6:
        print("\n=== MOVIMENTAÇÃO DE ESTOQUE ===")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        sub = int(input("Escolha movimentação: "))
        if sub > 2:
            print('Opção inválida!')
        else:
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            if sub == 1:
                registrar_compra(produto_id, quantidade)
            elif sub == 2:
                registrar_venda(produto_id, quantidade)
    elif opc == 7:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida! Tente novamente.')

