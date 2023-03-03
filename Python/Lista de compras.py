print(f'{"                         "}{"-"*15} LISTA DE COMPRAS {"-"*15}')
print(f'{"                                             "} OPÇÕES')
opções = print('[0] Nenhuma opção [1] Finalizar programa [2] Finalizar compras [3] Ver lista atual')
contProduto = contPreço = 0
conjuntoProdutos = []
while opções != 1:
    print("="*15)
    produto = str(input('Produto: ')).strip()
    contProduto += 1
    conjuntoProdutos.append(produto)
    preço = float(input('Preço do produto: R$'))
    contPreço += preço
    opções = int(input('Opções: '))
    while opções > 3:
        print('Opção inválida, digite novamente.')
        opções = int(input('Opções: '))
    if opções == 2:
        print(f'Você comprou {contProduto} item(ns) num total de R${contPreço:.2f}') 
        parcelar = str(input('Deseja parcelar sua compra? [S/N]: ')).strip().upper()
        if "S" in parcelar:
            vezesParcela = int(input('Em quentas vezes deseja parcelar? '))
            print(f'A compra de R${contPreço:.2f} parcelada em {vezesParcela}x ficará por R${contPreço / vezesParcela:.2f}')
        continuar1 = str(input('Deseja continuar comprando? [S/N]: ')).strip().upper()
        if "N" in continuar1:
            break
    if opções == 3:
        print(f'{"-"*5} LISTA {"-"*5}')
        for c in conjuntoProdutos:
            print(c)
        verPreços = str(input('Deseja ver os preços das compras? [S/N]: ')).strip().upper()
        if "S" in verPreços:
            print(f'O preço atual das compras é de R${contPreço:.2f}')
        continuar2 = str(input('Deseja continuar comprando? [S/N]: ')).strip().upper()
        if "N" in continuar2:
            break
parcelar = str(input('Deseja parcelar sua compra? [S/N]: ')).strip().upper()
if "S" in parcelar:
    vezesParcela = int(input('Em quentas vezes deseja parcelar? '))
    print(f'A compra de R${contPreço:.2f} parcelada em {vezesParcela}x ficará por R${contPreço / vezesParcela:.2f}')