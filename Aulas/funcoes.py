# Desafio 1
def soma(x, y):
    return x + y


def sub(x, y):
    return x - y

n1 = int(input('num: '))
n2 = int(input('num: '))

print(f'O resultado da soma é {soma(n1, n2)}')
print(f'O resultado da subtração é {sub(n1, n2)}')

# Desafio 2
def maior(x, y):
    if x > y:
        return print(f'O Numero {x} é o maior')
    elif x < y:
        return print(f'O Numero {y} é o maior')
    else:
        return print(f'O Numero {x} é igual ao {y}')

n1 = int(input('num: '))
n2 = int(input('num: '))

maior(n1, n2)

# Função maior do built-in do python
max(n1, n2)

# Função map()
# Serve para aplicar uma função dentro de um item iteravel
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobro = list(map(lambda x: x * 2, lista))
print(dobro)

# Exemplo 2
contas = [dict(nome='João', saldo=100), dict(nome='Felipe', saldo=50000), dict(nome='Camila', saldo=2500)]
print(list(map(lambda x: x['saldo'] > 1000, contas)))


# Função reduce()
# Funciona como map() mas o retorno é um unico item
# A linha abaixo deve ficar no topo do arquivo segundo a pep8
from functools import reduce

soma = reduce((lambda x, y: x + y), lista)

print(soma)

# Função filter()
# Como próprio nome ja diz, filtra os valores
n_par = list(filter(lambda x: x % 2 == 0, lista))

print(n_par)
