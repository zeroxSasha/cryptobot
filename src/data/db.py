from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv


class DataBase:
    __instance = None

    @staticmethod
    def get_connection():
        if not DataBase.__instance:
            try:
                load_dotenv()
                DataBase.__instance = connect(getenv('DATABASE_URL'))
                DataBase.__instance.autocommit = True

            except Exception as e:
                print(f'[Error] {e}')
        
        return DataBase.__instance
    
    @staticmethod
    def close_connection() -> None:
        if DataBase.__instance is not None:
            DataBase.__instance.close()
            DataBase.__instance = None
