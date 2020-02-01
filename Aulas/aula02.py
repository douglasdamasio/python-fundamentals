
# Aula sobre tuplas, dicionarios e condições if

########### TUPLAS ###########

# Tuplas são imutaveis e chatas

# Iniciando variavel tupla
valores = (1, 2, 3)

# Tuplas guardam vários itens
valores = (1, 2, [1, 2, 3], {'chave': 'valor'})

# Metodo index mostra a posição do intem que é passado
print(valores.index(2))

# Metodo count conta valores dentro de tuplas, dicionarios ou listas
print(valores.count(1))

########### DICIONARIOS ###########

# Dicionários são chaves {}
ling = {'joao': 'java', 'daniel': 'python', 'hector': 'PHP'}

# Imprime valor na tela da chave
print(ling['daniel'])

# Novo dicionario
time_favorito = {'joao': 'corinthians', 'rafael': 'flamengo', 'ana': 'palmeiras'}

# Adicionar chave e valor no dicionario
time_favorito['marcelo'] = 'vasco'

# Alterar valores dentro do dicionario alterando a posição da pilha
time_favorito.update({'marcelo': 'botafogo'})

# Imprime valores das chaves
print(time_favorito.values())

# Imprimindo chaves
print(time_favorito.keys())

# Primeira chave receber o valor da chave passada
time_favorito['joao'] = time_favorito['rafael']

# Novo dicionario (complexo) _mongodb
dados_cliente = {'clientes':{'cl001': {'nome': 'Rafael Silva',
                                     'idade': 25,
                                     'telefone': '1164824198'
                                     },
                            'cl002': {'nome': 'Carla Pereira',
                                     'idade': 28,
                                     'telefone': ''
                                     }
                            }
                }

# Imprimindo todos os dados dentro da chave especificada
print(dados_cliente['clientes'])

# Imprimindo dados de um segundo dicionario dentro de outro dicionario
print(dados_cliente['clientes']['cl002'])

# Imprimindo dados de um terceiro dicionario, ou seja, uma terceira chave
print(dados_cliente['clientes']['cl002']['nome'])

# Adicionando um valor a chave sem mudar o local na pilha
dados_cliente['clientes']['cl002']['telefone'] = '1164822247'
print(dados_cliente['clientes']['cl002']['telefone'])

# Iniciar uma váriavel para buscar no dicionario
var = input('Entre com o código do cliente: ')

# ifzinho de brinqk
if int(var) > 2:
    print('Cliente não cadastrado!')
else:
# Impressão com variavel
    print(dados_cliente['clientes']['cl00' + var])

########### IF ###########

idade = int(input('Digite sua idade: '))
habilitacao = int(input('Possui habilitação:\nSIM digite 1 \nNÃO digite 2 \n> '))
if idade >= 18 and habilitacao == 1:
    print('Você pode dirigir!')
else:
    print('Você não pode dirigir!')
