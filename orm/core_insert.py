from core import user_table, eng

con = eng.connect()
ins = user_table.insert()

def inserir_dados(i, n, s):
    '''Função insere dados:
                            i = idadae
                            n = nome
                            s = senha
    '''
    new = ins.values(idade=i, nome=n, senha=s)
    con.execute(new)

# inserir_dados(27, 'douglas', 'abacaxi12')