# -*- coding: utf-8 -*-

dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87
        }
    }
}

# NOMES DOS ESTADOS
print('-- Nomes dos estados --')
print(f"Nome: {dados['estados']['sp']['nome']}")
print(f"Nome: {dados['estados']['rj']['nome']}")
print(f"Nome: {dados['estados']['mg']['nome']}")
print('-' * 30)

# NOMES DOS ESTADOS E SUA POPULAÇÃO EM MILHÕES
print('-- Nomes dos estados e suas populações --')
print(f"Nome: {dados['estados']['sp']['nome']}, Popolução: {dados['estados']['sp']['população']} mi")
print(f"Nome: {dados['estados']['rj']['nome']}, Popolução: {dados['estados']['rj']['população']} mi")
print(f"Nome: {dados['estados']['mg']['nome']}, Popolução: {dados['estados']['mg']['população']} mi")
print('-' * 30)

# NOMES DOS ESTADOS E QUANTIDADE DE MUNICIPIOS
print('-- Nomes dos estados e quantidade de municipios --')
print(f"Nome: {dados['estados']['sp']['nome']}, Municipios: {dados['estados']['sp']['municipios']}")
print(f"Nome: {dados['estados']['rj']['nome']}, Municipios: {dados['estados']['rj']['municipios']}")
print(f"Nome: {dados['estados']['mg']['nome']}, Municipios: {dados['estados']['mg']['municipios']}")
print('-' * 30)

# Solução alternativa
print('Solução alternativa para Nomes')
for sigla in dados['estados']: # Pode-se usar -> for sigla in dados['estados'].keys():
    print(f"Nome: {dados['estados'][sigla]['nome']}")
print('-' * 30)

print('Solução alternativa para Nomes e População')
for sigla in dados['estados']:
        print(f"Nome: {dados['estados'][sigla]['nome']}, Popolução: {dados['estados'][sigla]['população']} mi")
print('-' * 30)

print('Solução alternativa para Nomes e Municipios')
for sigla in dados['estados']:
        print(f"Nome: {dados['estados'][sigla]['nome']}, Municipios: {dados['estados'][sigla]['municipios']}")
print('-' * 30)

### Exercicio IF
usuario = input('Digite o nome do usuário: ').lower()
user = ['rafael', 'camila', 'paulo', 'pamela']

if usuario in user:
    print('Acesso permitido')
else:
        print('Acesso negado') 