#! /usr/bin/python3
# O comando acima trata-se de uma sheebang para a execução do arquivo no linux (necessario permissao de execução do arquivo)

palavras = 'Palavras ao vento, são só palavras'
lista = ['jovem', 'valor', 'aula', 'comida', 'horario']

# Divide de acordo com o argumento passado
palavras.split('p')

# Retorna a posição do valor argumentado em index
lista.index('comida')

# Adicionar elementos ao final da lista
lista.append('item')

# Adicionar elementos em qualquer ponto da lista (Pirmeiro argumento é a posição)
lista.insert(0, 'Posição')

# Remover itens pelo nome
lista.remove('item')

# Remove itens pela posição
lista.pop(0)

# Imprime a lista organizada
lista.sort()
print(lista)

# Imprime a lista reversa
lista.sort(reverse=1)
print(lista)
