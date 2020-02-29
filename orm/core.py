# Imports
from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, DateTime
from datetime import datetime

# Cria o banco local dentro do especificado no parametro
# Parametro echo serve para poder escrever dentro do banco 
eng = create_engine('sqlite:///teste.db', echo=True)

# Metadata apontando para a Engine
metadata = MetaData(bind=eng)

# Criação da tabela Usuários com o metadata e as colunas especificadas
user_table = Table('usuarios', 
                    metadata,
                        Column('id', Integer, primary_key=True),
                        Column('nome', String(40), index=True),
                        Column('idade', Integer, nullable=False),
                        Column('senha', String),
                        Column('criado_em', DateTime, default=datetime.now),
                        Column('atualizado_em', DateTime, 
                                default=datetime.now, onupdate=datetime.now))

# primary_key - Define a chave primária
# index - Indexação 
# nullable - Habilitando o Not Null
# default - Padrão
# onupdate - Sempre que houver uma atualização

# Executa tudo
metadata.create_all(eng)