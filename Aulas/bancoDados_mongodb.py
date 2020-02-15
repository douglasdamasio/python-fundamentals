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
inserir_dados()