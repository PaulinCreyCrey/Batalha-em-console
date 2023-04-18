import random

class heroi(object):
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.força = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.carisma = 0
        self.vida = 100
        self.cont = 0
        self.defesa = 0

    def __str__(self):
        return f'Nome: {self.nome}, Classe: {self.classe}, Vida: {self.vida}.'


    def atacar(self, alvo):
        self.cont += 1
        
        print('----------------------------------\n'
        f'{self.nome} atacou {alvo.nome}.\n'
        '----------------------------------')

        if alvo.defesa >= 1:
            print(f"""\n----------------------------------
{alvo.nome} bloqueou o ataque!
----------------------------------\n""")
            self.dano(alvo,0)
            alvo.defesa = 0

        else:
            ataque =  random.randint(1, 6)

            if ataque <= 2:
                self.dano(alvo,0)
                print(f'{alvo.nome} sofreu 0 de dano!\n')

            elif ataque > 2 and ataque <= 5:
                self.dano(alvo,2)
                print(f'{alvo.nome} sofreu 2 de dano!\n')

            else:
                self.dano(alvo,4)
                print(f'{alvo.nome} sofreu 4 de dano!\n')


            if self.cont % 3 == 0:
                self.reconstituir(alvo)
                self.cont = 0


        

    def dano(self,alvo,valor):
        alvo.vida -= valor

        if alvo.vida <= 0:
            print(f'O inimigo {alvo.nome} foi abatido!')

    def reconstituir(self, alvo):
        reconstitui = random.randint(1, 6)

        if reconstitui <= 2:
            return

        elif reconstitui > 2 and reconstitui <= 5:
            alvo.vida += 2
            print(f'A vida de {alvo.nome} foi restaurada em 2!')

        else:
            alvo.vida += 4
            print(f'A vida de {alvo.nome} foi restaurada em 4!')

    def defender(self):
        self.defesa += 1