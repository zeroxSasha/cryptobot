from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from os import getenv

from data.postgre_db import update_data
from data.postgre_db import add_data, get_data


class DataBase:
    __instance = None

    @staticmethod
    def get_connection():
        if not DataBase.__instance:
            try:
                load_dotenv()
                DataBase.__instance = connect(getenv('POSTGRESQL_URL'))
                DataBase.__instance.autocommit = True

                DataBase.ensure_users_table()

            except Exception as e:
                print(f'[Error] {e}')
        
        return DataBase.__instance
    
    @staticmethod
    def ensure_users_table():
        try:
            with DataBase.__instance.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT 1 
                        FROM information_schema.tables 
                        WHERE table_name = 'users'
                    );
                """)
                table_exists = cursor.fetchone()['exists']
                
                if not table_exists:
                    cursor.execute("""
                        CREATE TABLE users (
                            user_id BIGSERIAL PRIMARY KEY,
                            days_left INTEGER DEFAULT 0,
                            money_limit INTEGER DEFAULT 10,
                            list_of_coins INTEGER DEFAULT 0
                        );
                    """)
                    print("[Info] Table 'users' is created.")
                else:
                    print("[Info] Table 'users' already exists.")
        
        except Exception as e:
            print(f"[Error] Unable to check or create a table: {e}")

    @staticmethod
    def close_connection() -> None:
        if DataBase.__instance is not None:
            DataBase.__instance.close()
            DataBase.__instance = None

    
    # add_data.py
    @staticmethod
    def add_new_user(user_id: int, days_left: int, money_limit: int, list_of_coins: int) -> None:
        add_data.add_new_user(DataBase.__instance, user_id, days_left, money_limit, list_of_coins)
    
    # change_data.py
    @staticmethod
    def change_moneylimit(user_id: int, money_limit: int) -> None:
        update_data.change_moneylimit(DataBase.__instance, user_id, money_limit)

    def change_listofcoins(user_id: int, list_of_coins: int) -> None:
        update_data.change_listofcoins(DataBase.__instance, user_id, list_of_coins)

    # get_data.py
    @staticmethod
    def get_all_users() -> list:
        return get_data.get_all_users(DataBase.__instance)
