def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

assert somar(2, 2) == 4, f'Obtido: {somar(2,2)}, Esperado: 4'
assert somar(3, 3) == 6, f'Obtido: {somar(3,3)}, Esperado: 6'

assert subtrair(2, 2) == 0, f'Obtido: {subtrair(2,2)}, Esperado: 0'
assert subtrair(5, 3) == 2, f'Obtido: {subtrair(5,3)}, Esperado: 2'

assert multiplicar(10, 2) == 20, f'Obtido: {multiplicar(10,2)}, Esperado: 20'
assert multiplicar(1, 3) == 3, f'Obtido: {multiplicar(1,3)}, Esperado: 3'

assert dividir(4, 2) == 2, f'Obtido: {dividir(4,2)}, Esperado: 2'
assert dividir(9, 3) == 3, f'Obtido: {dividir(9,3)}, Esperado: 3'