import random,time
print('Bora jogar Jokenpô')
jokenpo = str(input('Faça sua jogada: ')).lower().strip()
time.sleep(1)
print('Jo' ,end='')
time.sleep(1)
print('ken',end='')
time.sleep(1)
print('pô\n' ,end='')
time.sleep(1)

maquina = random.choice(['pedra','papel','tesoura'])


print('{:=^20}'.format(':-:'))
print('Você escolheu {}'.format(jokenpo))
print('Ele escolheu {}'.format(maquina))
print('{:=^20}'.format(':-:'))

if jokenpo == maquina :
    print('Empate')

elif jokenpo == 'pedra'   and maquina == 'tesoura' or \
     jokenpo == 'papel'   and maquina == 'pedra'   or \
     jokenpo == 'tesoura' and maquina == 'papel' :
    print('Parabens você teve a sorte de ganhar de mim')


elif jokenpo == 'tesoura' and maquina == 'pedra' or \
     jokenpo == 'pedra'   and maquina == 'papel' or \
     jokenpo == 'papel'   and maquina == 'tesoura' :
    print('HAHAHAHAHAAHAHAH VOCÊ NUMCA VAI GANHAR')

elif jokenpo == 'spock' :
    print('COMO É POSSIVEL VOCÊ CONHECER ESSA MAGIA ANTIGA')


else:
    print('Você sabe que jogo é esse? digita pedra papel ou tesoura ;-;')



