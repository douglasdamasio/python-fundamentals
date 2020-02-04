
__author__ = 'Douglas Damasio'

def ler_arquivo():
    '''
    Lê arquivo e imprimir no terminal como lista
    '''
    with open('EAD/text.txt', 'r') as arq:
        lista = arq.readlines()
        return print(lista)

def escrever_arquivo(lista_de_conteudo):
    '''
    Recebe o conteudo e imprime inseri ele no documento
    '''
    with open('EAD/text.txt', 'a') as arq:
        arq.seek(1)
        arq.writelines(lista_de_conteudo)
        arq.write('\n')
        return print('Escrito com sucesso')

def contar_linhas():
    '''
    Conta o numero de linha no arquivo
    '''
    with open('EAD/text.txt', 'r') as arq:
        return print(f'\nA quantidade de linhas é: {len(arq.readlines())}\n')

print('-' * 30)
print('Menu')
print('-' * 30)
print('Escolha a opção desejada: \n')
print('1: Ler arquivo')
print('2: Escrever arquivo')
print('3: Contar Linhas\n')

while True:
    opcao = input('Digite o numero da sua opção: \n> ').split()
    if opcao[0].isnumeric() and (int(opcao[0]) < 4 and int(opcao[0]) > 0):
        break
    else:
        print('Opção inválida')
        continue 

if int(opcao[0]) == 1:
    ler_arquivo() 

elif int(opcao[0]) == 2:
    conteudo = input('Digite o conteudo do arquivo: \n> ')
    cont_in_list = []
    cont_in_list.append(conteudo)
    escrever_arquivo(cont_in_list)

else:
    contar_linhas()

print('-' * 30)
print('Fim do programa!')
print('-' * 30)
