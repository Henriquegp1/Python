print('{:=^40}'.format('LOJAS HENRY'))
produto = float(input('Digite o valor das suas compras: '))
print('Qual sera a forma de pagamento digite o numero corespondente \n[ 1 ] A vista no dinheiro\n[ 2 ] A vista no cartão')
print('[ 3 ] Em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')

num = int(input('Qual a Forma: '))

if num == 1 :
    print('A vista no dinheiro de {:.2f}R$'.format(produto))
    print('O valor da compra com 10% de desconto ficou {}R$'.format(produto-(produto*0.10)))
elif num == 2 :
    print('A vista no dinheiro de {:.2f}R$'.format(produto))
    print('O valor da compra com 5% de desconto ficou {}R$'.format(produto-(produto*0.05)))
elif num == 3 :
    print('A vista no dinheiro de {:.2f}R$'.format(produto))
    print('O valor da compra em 2x ficou {}R$'.format(produto))
elif num == 4 :
    vezes = int(input('Em quantas vezes no catão'))
    print('A vista no dinheiro de {:.2f}R$ em {}x'.format(produto,vezes))
    print('O valor da compra em {}X com 20% de juros ficou {}R$'.format(vezes,produto+(produto*0.20)))
else :
    print('Escolha uma opção valida')


