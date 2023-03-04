print(f'{"                         "}{"-"*15} LISTA DE COMPRAS {"-"*15}')
print(f'{"                                             "} OPÇÕES')

opções = print('[0] Nenhuma opção [1] Finalizar programa [2] Finalizar compras [3] Ver lista atual')

contadorProduto = preçoTotal = 0
nomesProdutos = []

while opções != 1:
    print("="*15)
    produto = str(input('Produto: ')).strip()
    contadorProduto += 1

    preço = float(input('Preço do produto: R$'))
    nomesProdutos.append([produto, str(f'R${preço:.2f}')])
    preçoTotal += preço

    opções = int(input('Opções: '))

    while opções > 3:
        print('Opção inválida, digite novamente.')
        opções = int(input('Opções: '))

    if opções == 2:
        print(f'Você comprou {contadorProduto} item(ns) num total de R${preçoTotal:.2f}') 
        parcelar = str(input('Deseja parcelar sua compra? [S/N]: ')).strip().upper()
        if "S" in parcelar:
            vezesParcela = int(input('Em quentas vezes deseja parcelar? '))
            print(f'A compra de R${preçoTotal:.2f} parcelada em {vezesParcela}x ficará por R${preçoTotal / vezesParcela:.2f}')
        continuar1 = str(input('Deseja continuar comprando? [S/N]: ')).strip().upper()
        if "N" in continuar1:
            break
        
    if opções == 3:
        print(f'{"-"*5} LISTA {"-"*5}')
        for c in nomesProdutos:
            contador = 1
            for p in c:
                print(p,end=' ')
                if contador == 2:
                    print('')
                contador += 1
        verPreços = str(input('Deseja ver os preços total das compras? [S/N]: ')).strip().upper()
        if "S" in verPreços:
            print(f'O preço atual das compras é de R${preçoTotal:.2f}')
        continuar2 = str(input('Deseja continuar comprando? [S/N]: ')).strip().upper()
        if "N" in continuar2:
            break
        
parcelar = str(input('Deseja parcelar sua compra? [S/N]: ')).strip().upper()
if "S" in parcelar:
    vezesParcela = int(input('Em quentas vezes deseja parcelar? '))
    print(f'A compra de R${preçoTotal:.2f} parcelada em {vezesParcela}x ficará por R${preçoTotal / vezesParcela:.2f}')