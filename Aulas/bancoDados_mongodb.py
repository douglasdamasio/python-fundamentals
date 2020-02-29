# Importar MongoDB client
from pymongo import MongoClient

# Passando o local do banco de dados para variavel
client = MongoClient('localhost')

# Declarando o banco de dados
db = client['dexterops']

# Função de Inserção
def inserir_dados():
    # Tente
    try:
        # comando de insert no MongoDB via JSON
        db.fila.insert({"_id":1, "empresa": "4linux",
                        "cursos": [{"nome":"python fundamentals",
                                    "carga horaria": 40},
                                    {"nome":"linux fundamentals",
                                    "carga horaria": 40}]})
    # Caso erro
    except Exception as e:
        # Mensagem para o usuário
        print(f'Erro! {e}')

# Call
# inserir_dados()

def buscar_dados():
        for r in db.fila.find():
                print(f'Empresa: {r["empresa"]}')
                for c in r["cursos"]:
                        print(20 * '=')
                        print(f'Nome: {c["nome"]}\nCarga Horaria {c["carga horaria"]}')

# buscar_dados()

def add_sub():
        db.fila.update({"_id":1}, {"$addToSet": {"instrutores": {"nome": "Mariana", "email": "mariana@4linux.com.br"}}})

# add_sub()

def update_instutor():
        db.fila.update({"_id":1, "instrutores.nome": "Mariana"}, {"$set": {"instrutores.$.nome": "Marcia"}})

# update_instutor()

def update_instutor_email():
        db.fila.update({"_id":1, "instrutores.nome": "Marcia"}, {"$set": {"instrutores.$.email": "marcia@4linux.com.br"}})

# update_instutor_email()
