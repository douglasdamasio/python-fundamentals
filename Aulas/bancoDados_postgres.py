# Importantdo biblioteca do Postgres
import psycopg2

# Tente
try:

    # Abrir conexão com o banco de dados Postgres
    con = psycopg2.connect(
        'host=localhost dbname=projeto user=admin password=4linux'
        )

    # Iniciar o cursor
    cur = con.cursor()

    # Executar o comandos
    cur.execute(
        "insert into scripts(nome, conteudo) values ('teste_try.py', 'try exception')"
        )

    # Commitar a conexão
    con.commit()

# Caso encontre erro
except Exception as e:

    # Mostrar erro na tela
    print(f'ERRO! {e}')

    # Exibir mensagem para o usuário que está retrocedendo
    print('Aplicando Rollback')

    # Aplicando o rollback
    con.rollback()

# Finalmente
finally:

    # Mensagem para o usuário
    print('Fechando conexão com o Banco de dados')

    # Fechar conexão!
    con.close()