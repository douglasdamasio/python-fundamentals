# -*- coding: UTF-8 -*-

import requests

class Carro():

    def __init__(self):
        self.rodas = 4
        self.motor = True

    def ligar(self):
        print('Ligando...')

    def remover_motor(self):
        self.motor = False


class Servidor():

    def __init__(self, servico, disco, processador, memoria):
        self.servico = servico
        self.disco = disco
        self.processador = processador
        self.memoria = memoria

    def add_memoria(self, addM):
        self.memoria += addM
        print(f'Adicionado {addM} GB de memória')
    
    def add_disco(self, addD):
        self.disco += addD
        print(f'Adicionado {addD} GB de espaço em disco')

    def muda_serv(self, new_serv):
        self.servico = new_serv
        print(f'Adicionado novo serviço {new_serv}')


class Tests():
    
    def __init__(self):
        self.SITE = 'https://renatobarbosa.tech'

    def verificar_site(self):
        self.requisicao = requests.get(self.SITE)
        return self.requisicao


class servidor_web(Servidor):
    def __init__(self, servico, disco, processador, memoria):
        super().__init__(servico, disco, processador, memoria)
        self.servico = 'nginx'

vader = servidor_web('mariadb', 250, 'i9', 32)
print(vader.servico, vader.disco)