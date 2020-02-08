# Laço de repetição FOR
frutas = ['Abacaxi', 'Banana', 'Caju']

for fruta in frutas:
    print(fruta)

# Exemplo com tupla
carros = ('Golf', 'Fox', 'Camaro')

for carro in carros:
    print(carro)

# Laço FOR in range 
# No range o 1o arg. é INCLUSIVO, o 2o é EXCLUSIVO e o 3o é o STEP
for n in range(1, 100):
    print(n)

# Condições aninhadas
carros = ['Ferrari', 'Lamborghini', 'Porsche']
cores = ['Vermelha', 'Azul', 'Preto']

for carro in carros:
    for cor in cores:
        print(carro, cor)

# Comando break 
# Serve para parar a execução de um laço de repetição
for i in range(1, 500):
    if i == 50:
        print(i)
        break

# Comando continue 
# Serve para retornar ao começo do bloco de comandos do laço de repetição
for i in range(1, 500):
    if i == 50:
        print(i)
        continue

########### try/exception ###########

# Tratamento de erro genérico
try:
    if nome == 'douglas':
        print(nome)
except Exception as e:
    print('errouuuu!')

