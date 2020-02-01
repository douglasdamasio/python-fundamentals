# Software de Folha de Pagamento

__author__ = 'DOUGLAS DAMASIO'

# Entrada de dados do usuário. VALOR DE HORA e QTD. DE HORA
valor_hora = float(input('Digite o Valor cobrado por hora: '))
qtd_horas = float(input('Digite a quantidade de horas: '))

# Calculo do salario Bruto
salario_bruto = valor_hora * qtd_horas

# Condição de isenção
if salario_bruto <= 1900:
    calc = 0.00
    ir = str('(-) IR (isento): R$ 0.00')

# Condição de 7%
elif salario_bruto >= 1901 and salario_bruto <= 2800:
    calc = salario_bruto * 0.07
    ir = str('(-) IR (7%): R$ {:.2f}'.format(calc))

# Condição de 15%
elif salario_bruto >= 2801 and salario_bruto <= 3700:
    calc = salario_bruto * 0.15
    ir = str('(-) IR (15%): R$ {:.2f}'.format(calc))

# Condição de 22%
elif salario_bruto >= 3701 and salario_bruto <= 4600:
    calc = salario_bruto * 0.22
    ir = str('(-) IR (22%): R$ {:.2f}'.format(calc))

# Condição de 27%
elif salario_bruto >= 4601:
    calc = salario_bruto * 0.27
    ir = str('(-) IR (27%): R$ {:.2f}'.format(calc))

# Desconto em comum do sindicato
sindicato = salario_bruto * 0.03

# FGTS (Não deve entrar no calculo do desconto)
fgts = salario_bruto * 0.11

# Calculo total do desconto
total_desc = calc + sindicato 

# Calculo do salario liquido
salario_liquido = salario_bruto - total_desc

# Extrato em fstr
print(f'''
Valor da hora: {valor_hora}
Quantidade de horas trabalhadas: {qtd_horas}
Salario Bruto: ({valor_hora} * {qtd_horas}): R$ {salario_bruto:.2f}
{ir}
(-) Sindicato (3%): R$ {sindicato:.2f}
FGTS (11%): R$ {fgts:.2f}
Total de descontos: R$ {total_desc:.2f}
Salario Liquido: R$ R$ {salario_liquido:.2f}
''')

# Fim