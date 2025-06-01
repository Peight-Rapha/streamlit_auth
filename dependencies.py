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

