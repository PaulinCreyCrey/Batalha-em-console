#CODIGO DO PAULO VITOR

import random

import classes

###Programa###

while True:

    print('*****************Bem Vindo Ao Campo de Batalha!!!*****************\n')

### Jogador 1 ###
    nome1 = input('Digite o nome do jogador 1: ')

    print('\nEscolha uma classe:\n'
    '------------------------------\n'
    '1- Bárbaro\n'
    '2- Mago\n'
    '3- Ladino\n'
    '4- Bardo\n'
    '5- Guerreiro\n'
    '------------------------------')

    classe1 = int(input('\nInsira o valor desejado: '))

    if classe1 == 1:
        classe1 = 'Bárbaro'

    elif classe1 == 2:
        classe1 = 'Mago'

    elif classe1 == 3:
        classe1 = 'Ladino'

    elif classe1 == 4:
        classe1 = 'Bardo'

    elif classe1 == 5:
        classe1 = 'Guerreiro'

    else:
        print('\nOpção Invalida.\n')
        break

    print('-----------------------------------------'
          f'\n{nome1} escolheu a classe {classe1}.\n'
          '-----------------------------------------')

    jogador1 = classes.heroi(nome1, classe1)

###Atributos do jogador 1### 
    print('Escolha uma opção:\n\n1 - Definir o valor de seus atributos.\n2 - Definir o valor de seus atributos aleatóriamente.\n')

    atributos1 = int(input('Digite sua escolha: \n'))

    if atributos1 == 1:
        Força = int(input('\nDigite o valor da sua força:'))
        if Força < 1 and Força > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador1.força = Força

        Destreza = int(input('\nDigite o valor da sua destreza:'))
        if Destreza  < 1 and Destreza > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador1.destreza = Destreza

        Constituicao = int(input('\nDigite o valor da sua constituição:'))
        if Constituicao < 1 and Constituicao > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador1.constituicao = Constituicao

        inteligencia = int(input('\nDigite o valor da sua inteligencia:'))
        if inteligencia < 1 and inteligencia > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador1.inteligencia = inteligencia

        Carisma = int(input('\nDigite o valor do seu carisma:'))
        if Carisma < 1 and Carisma > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador1.carisma = Carisma

    elif atributos1 == 2:
        jogador1.força = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador1.destreza = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador1.constituicao = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador1.inteligencia = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador1.carisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

    else:
        print('Opção Invalida.')
        break

    print(f"""Seus atributos são:
------------------------------
Força = {jogador1.força}
Destreza = {jogador1.destreza}
Constituição = {jogador1.constituicao}
Inteligencia = {jogador1.inteligencia}
Carisma = {jogador1.carisma}
------------------------------\n""")


### Jogador 2 ###

    nome2 = input('Digite o nome do jogador 2: ')

    print('\nEscolha uma classe:\n'
    '------------------------------\n'
    '1- Bárbaro\n'
    '2- Mago\n'
    '3- Ladino\n'
    '4- Bardo\n'
    '5- Guerreiro\n'
    '------------------------------')

    classe2 = int(input('\nInsira o valor desejado: '))
    if classe2 == 1:
        classe2 = 'Bárbaro'

    elif classe2 == 2:
        classe2 = 'Mago'

    elif classe2 == 3:
        classe2 = 'Ladino'

    elif classe2 == 4:
        classe2 = 'Bardo'

    elif classe2 == 5:
        classe2 = 'Guerreiro'

    else:
        print('\nOpção Invalida.\n')
        break

    print('-----------------------------------------'
          f'\n{nome2} escolheu a classe {classe2}.\n'
          '-----------------------------------------')
    
    jogador2 = classes.heroi(nome2, classe2)

###Atributos do Jogador 2###
    print('Escolha uma opção:\n\n1 - Definir o valor de seus atributos.\n2 - Definir o valor de seus atributos aleatóriamente.\n')

    atributos2 = int(input('Digite sua escolha: \n'))

    if atributos2 == 1:
        Força = int(input('\nDigite o valor da sua força:'))
        if Força < 1 and Força > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador2.força = Força

        Destreza = int(input('\nDigite o valor da sua destreza:'))
        if Destreza  < 1 and Destreza > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador2.destreza = Destreza

        Constituicao = int(input('\nDigite o valor da sua constituição:'))
        if Constituicao < 1 and Constituicao > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador2.constituicao = Constituicao

        inteligencia = int(input('\nDigite o valor da sua inteligencia:'))
        if inteligencia < 1 and inteligencia > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador2.inteligencia = inteligencia

        Carisma = int(input('\nDigite o valor do seu carisma:'))
        if Carisma < 1 and Carisma > 18:
            print('Erro nos valores dos atributos.')
        else:
            jogador2.carisma = Carisma

    elif atributos2 == 2:
        jogador2.força = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador2.destreza = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador2.constituicao = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador2.inteligencia = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        jogador2.carisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

    else:
        print('Opção Invalida.')
        break

    print(f"""Seus atributos são:
------------------------------
Força = {jogador2.força}
Destreza = {jogador2.destreza}
Constituição = {jogador2.constituicao}
Inteligencia = {jogador2.inteligencia}
Carisma = {jogador2.carisma}
------------------------------
\n""")


###BATALHA###

    primeiro = int(input(f'------------------------------------\n'
    f'Escolha o jogador inicial: \n1 - {jogador1.nome}\n2 - {jogador2.nome}\n3 - Escolher jogador aleatóriamente\n'
    '------------------------------------\n'))

    segundo = 0

    if primeiro == 1:
        primeiro = jogador1
        segundo = jogador2

    elif primeiro == 2:
        primeiro = jogador2
        segundo = jogador1

    elif primeiro == 3:
        dado = random.randint(1, 2)
        if dado == 1:
            primeiro = jogador1
            segundo = jogador2

        elif dado == 2:
            primeiro = jogador2
            segundo = jogador1

    else:
        print('Opção invalida.')
        break

    print(f'\nO jogador inicial é...{primeiro.nome}!!!')

    print('\nA batalha começa!!!\n')

    while True:
        print(f'1 - atacar {segundo.nome}\n2 - preparar defesa\n3 - passar turno\n4 - Ver status dos jogadores\n')
        açao1 = int(input(f'Oque {primeiro.nome} deseja fazer?\n'))
        
        if açao1 == 1:
            primeiro.atacar(segundo)

        elif açao1 == 2:
            print('-----------------------------------\n'
            f'{primeiro.nome} preparou uma defesa!\n'
            '-----------------------------------\n')
            primeiro.defender()

        elif açao1 == 3:
            print('-----------------------------------\n'
            f'{primeiro.nome} passou a vez!\n'
            '-----------------------------------')
        elif açao1 == 4:
            print(f'\n{primeiro}\n')
            print(f'{segundo}\n')

        print(f'1 - atacar {primeiro.nome}\n2 - preparar defesa\n3 - passar turno\n4 - Ver status dos jogadores\n')
        açao2 = int(input(f'Oque {segundo.nome} deseja fazer?\n'))
        
        if açao2 == 1:
            segundo.atacar(primeiro)

        elif açao2 == 2:
            print('-----------------------------------\n'
            f'{segundo.nome} preparou uma defesa!\n'
            '-----------------------------------\n')
            segundo.defender()

        elif açao2 == 3:
            print('-----------------------------------\n'
            f'{segundo.nome} passou a vez!\n'
            '-----------------------------------')

        elif açao2 == 4:
            print(f'\n{primeiro}\n')
            print(f'{segundo}\n')


        if primeiro.vida <= 0:
            print(f'{primeiro.nome} foi abatido!\n{segundo.nome} é o vencedor!!!')
            break
        if segundo.vida <= 0:
            print(f'{segundo.nome} foi abatido!\n{primeiro.nome} é o vencedor!!!')
            break


