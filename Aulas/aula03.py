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

# ########## try/exception ###########

# Tratamento de erro genérico
try:
    if nome == 'douglas':
        print(nome)
except Exception as e:
    print('errouuuu!')

# Criando erro com Raise
blacklist = ['daniel', 'camila']
try:
    nome = input('Digite seu nome: ')
    if nome.lower() in blacklist:
        raise NameError('Usuário bloqueado!')
except NameError as n:
    print(n)

# ########## Manipulação de Arquivos ###########

# Comando w (write)
# Serve para escrever dentro do arquivo
with open('arquivo.txt', 'w') as file:
        file.write('Novo Arquivo txt')

# Comando r (read)
# Serve para ler o arquivo
with open('arquivo.txt', 'r') as file:
        file.read()

# Comando a (append)
# Serve para adicionar texto ao arquivo
with open('arquivo.txt', 'a') as file:
        file.write('\nNovo Arquivo txt + 1 linha')

# Comando x (create)
# Serve para criar o arquivo, caso ele não exista
with open('arquivo.txt', 'x') as file:
        file.write('ARQUIVO')

