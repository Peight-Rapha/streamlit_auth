import psycopg2
from dotenv import load_dotenv
import os
from contextlib import contextmanager


# chamar load_dotenv() para carregar as variáveis de ambiente do arquivo .env

DATABASE = os.getenv('DATABASE')
HOST = os.getenv('HOST')
USERSERVER = os.getenv('USERSERVER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')


# Criando decorador '@contextmanager' para gerenciar a conexão com o banco de dados

@contextmanager
def instance_cursor():
    # Realizando conexão com o banco de dados
    connection = psycopg2.connect(
        database=DATABASE,
        host=HOST,
        user=USERSERVER,
        password=PASSWORD,
        port=PORT
    )
    # criando um cursor para executar comandos SQL
    cursor = connection.cursor()
    try:
        # retornando sob demanda
        yield cursor
    finally:
        if (connection):
            # fechando o cursor
            cursor.close()
            print('Conexao com PostgreSQL fechada')



