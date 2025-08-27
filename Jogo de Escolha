import random
from time import sleep

alen = random.randint(0, 10)  # pegando um numerro aleatorio
n = -1
tentativas = 0
print('-=-' * 18)
print('Estou com vontade de jogar um jogo... ')
print('-=-' * 18)

while n != alen:
    n = int(input('Escolha um numero entre 0 e 10 que eu pensei: ')) #escolhendo o numero
    tentativas += 1

    print('PROCESSANDO...')
    sleep(1)

    if n not in range(0,11):
        print('Ai não tem graça digite um numero que eu pedi')

    elif n > alen:
        print('Tente um numero mais baixo')
    elif n < alen:
        print('Tente um numero mais alto')



print('Como você acertou o meu numero?')
print(f'Mesmo assim você precisou de {tentativas} tentativas')
