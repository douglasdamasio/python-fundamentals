from sqlalchemy import delete
from core import user_table, eng

con = eng.connect()

def deletar_dado(dado):
    d = delete(user_table).where(user_table.c.nome == dado)
    resultado = con.execute(d)
    print(resultado.rowcount)
