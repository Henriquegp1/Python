import datetime
sexo = str(input('Digite seu genero: ')).lower().strip()
if sexo == 'masculino' :
    nasc = int(input('Digite o ano do seu nascimento: '))

    atual =datetime.datetime.now().year
    alistamento = atual - nasc
    falta = 18 - alistamento
    print('Quem nasceu em {} tem {} em {}'.format(nasc,alistamento,atual))

    if alistamento < 18 :
        print('Ainda não chegou a sua vez faltam {} anos'.format(falta))
        print('Seu alistamento será em {}'.format(falta + atual))
    elif alistamento == 18 :
        print('Chegou sua vez de se alistar no exercito brasileiro')
    else:
        print('Já passou da hora de se alistar ')
        if alistamento-18 == 1 :
            print('jâ passou {} ano do seu alistamento'.format(alistamento-18))
            print('Seu alistamento foi em {}'.format(atual - falta))
        else:
            print('jâ passou {} anos do seu alistamento'.format(alistamento - 18))
            print('Seu alistamento foi em {}'.format(atual - falta))
elif sexo == 'feminino' :
    print('Você não é obrigada a se alistar')
else:
    print('Digite o que foi pedido ')




