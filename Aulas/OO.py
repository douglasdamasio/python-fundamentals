# -*- coding: UTF-8 -*-


class Carro():

    def __init__(self):
        self.rodas = 4
        self.motor = True

    def ligar(self):
        print('Ligando...')

    def remover_motor(self):
        self.motor = False


palio = Carro()
# palio.ligar()

class Servidor():

    def __init__(self, servico, disco, processador, memoria):
        self.servico = servico
        self.disco = disco
        self.processador = processador
        self.memoria = memoria

    def add_memoria(self):
        self.memoria += 16
        print('Adicionado 16GB de memória')
    
    def add_disco(self):
        self.disco +=250
        print('Adicionado 250GB de espaço em disco')

    def muda_serv(self):
        self.servico = input('Digite o nome do novo serviço: ')

    

servidorweb = Servidor('Nginx', 250, 'i7 9º Geração', 16)
print(servidorweb.servico, servidorweb.disco, servidorweb.processador, servidorweb.memoria)
servidorweb.muda_serv()
servidorweb.add_disco()
servidorweb.add_memoria()
print(servidorweb.servico, servidorweb.disco, servidorweb.processador, servidorweb.memoria)


