from estoque import *


while True:

    print('\n=== SISTEMA DE ESTOQUE ===')
    print('1 - Inserir Produto')
    print('2 - Listar Produtos')
    print('3 - Atualizar Produto')
    print('4 - Deletar Produto')
    print('5 - Sair')

    while True:
        try:
            opc = int(input('Escolha uma opção: '))
            break
        except ValueError:
            print('Insira um valor válido!')


    if opc == 1:
        nome = input('Nome do produto: ')
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        inserir_produtos(nome, quantidade, preco)
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
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida! Tente novamente.')

