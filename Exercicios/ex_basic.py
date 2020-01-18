frase = 'A soma dos resultados'

lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']

# print 3, 13, vasco
print(lista[1][2], lista[4][3], lista[-1])

# print 4, São Paulo, 14
print(lista[1][3], lista[3], lista[4][-1])

# print Corinthians, 2, 10, 14
print(lista[0], lista[1][1], lista[4][0], lista[4][-1])
