from sqlalchemy import update
from core import user_table, eng

con = eng.connect()

def atualizar_nome(nome_antigo, nome_novo):
    atualizar = update(user_table).where(user_table.c.nome == nome_antigo)
    atualizar = atualizar.values(nome=nome_novo)
    resultado = con.execute(atualizar)
    print(resultado.rowcount)