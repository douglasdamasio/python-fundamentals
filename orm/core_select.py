from sqlalchemy import select
from core import user_table

def selecionar_dados(dado):
    selecionar = select([user_table]).where(user_table.c.nome == dado)
    print([x for x in selecionar.execute()])

# selecionar_dados('douglas')
