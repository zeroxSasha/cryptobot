from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv


def get_connection():
    try:
        load_dotenv()
        
        connection = connect(getenv('DATABASE_URL'))
        connection.autocommit = True

        return connection

    except Exception as e:
        print(f'[Error] {e}')

def close_connection(conn):
    if conn is not None:
        conn.close()
