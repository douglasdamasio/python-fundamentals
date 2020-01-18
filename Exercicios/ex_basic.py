# Faça um programa que receba 4 notas de alunos
# some e divida por 4

# n1 = float(input('Digite a 1ª nota: '))
# n2 = float(input('Digite a 2ª nota: '))
# n3 = float(input('Digite a 3ª nota: '))
# n4 = float(input('Digite a 4ª nota: '))

# resultado = (n1 + n2 + n3 + n4) / 4
# print(f'''
# As notas são \033[1m{n1}\033[m, \033[1m{n2}\033[m,
# \033[1m{n3}\033[m, \033[1m{n4}\033[m
# A soma dos resultados, divido por 4 é igual a
# \033[1m{resultado}\033[m''', end='\n\n')

frase = 'A soma dos resultados'

lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']

# print 3, 13, vasco
print(lista[1][2], lista[4][3], lista[-1])

# print 4, São Paulo, 14
print(lista[1][3], lista[3], lista[4][-1])

# print Corinthians, 2, 10, 14
print(lista[0], lista[1][1], lista[4][0], lista[4][-1])
