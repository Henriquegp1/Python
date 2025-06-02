print('-=-' * 25)
print('Digite 3 valores e com eles vou te falar se é possivel formar um triangulo!')
print('-=-' * 25)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Essas retas conseguem formar um triangulo')
    if r1 == r2 and r2 == r3 :
        print('Ele é um triangulo equilatero')
    elif r1 == r2 or r2 == r3 or r1 == r3 :
        print('Ele é um triangulo Isósceles')
    else :
        print('Ele é um tricangulo escaleno')

else :
    print('Essas retas nao conseguem formar um triangulo')
