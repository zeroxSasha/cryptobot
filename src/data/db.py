from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv

from data import add_data, update_data


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

    # add_data.py
    @staticmethod
    def add_new_user(user_id: int, days_left: int, money_limit: int, list_of_coins: int) -> None:
        add_data.add_new_user(DataBase.__instance, user_id, days_left, money_limit, list_of_coins)
        