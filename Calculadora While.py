num  = int(input('Digite o 1ª numero: '))
num2 = int(input('Digite o 2ª numero: '))
escolha = 0

while escolha != 5 :
    print('-=-' * 6,'CALCULADORA', '-=-'*6)
    escolha = int(input(' [1]Somar\n [2]Multiplicar\n [3]Maior\n [4]Novos Numeros\n [5]Sair\n Escolha: '))

    if escolha == 1:
        print('{}+{}={}'.format(num,num2,(num+num2)))
    elif escolha == 2:
        print('{}x{}={}'.format(num,num2,(num*num2)))
    elif escolha == 3:
        if num > num2:
            print(f'{num} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num}')
    elif escolha == 4:
        num = int(input('Digite o 1ª numero: '))
        num2 = int(input('Digite o 2ª numero: '))

print('Saindo da CALCULADORA')



