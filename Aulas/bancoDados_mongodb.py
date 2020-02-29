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

# Função de busca (Select)
def buscar_dados():

        # Laço for para trazer os registros
        for r in db.fila.find():

                # Imprime na tela o nome da empresa
                print(f'Empresa: {r["empresa"]}')

                # Laço for para trazer cada curso de cada empresa
                for c in r["cursos"]:

                        # Imprime um separador
                        print(20 * '=')

                        # Imprime os dados nome e carga horaria de cada curso
                        print(f'Nome: {c["nome"]}\nCarga Horaria {c["carga horaria"]}')

# Call
# buscar_dados()

# Função de adição
def add_sub():

        # Update de um novo tipo de registro, comando Update com parametro $addToSet
        db.fila.update({"_id":1}, {"$addToSet": {"instrutores": {"nome": "Mariana", "email": "mariana@4linux.com.br"}}})

# Call
# add_sub()

# Função de atualização do "campo" de nome do instrutor
def update_instutor():

        # Comando Update com parametro $set
        db.fila.update({"_id":1, "instrutores.nome": "Mariana"}, {"$set": {"instrutores.$.nome": "Marcia"}})

# Call
# update_instutor()

# Função de atualização do "campo" do e-mail do instrutor
def update_instutor_email():

        # Comando Update com parametro $set
        db.fila.update({"_id":1, "instrutores.nome": "Marcia"}, {"$set": {"instrutores.$.email": "marcia@4linux.com.br"}})

# Call
# update_instutor_email()
