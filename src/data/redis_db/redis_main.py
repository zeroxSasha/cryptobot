import redis
from dotenv import load_dotenv
from os import getenv


class RedisDB:
    __instance = None

    @staticmethod
    def get_connection():
        if not RedisDB.__instance:
            try:
                load_dotenv()
                RedisDB.__instance = redis.Redis.from_url(getenv('REDIS_URL'))

            except Exception as e:
                print(f'[Error] {e}')
        
        return RedisDB.__instance
    
    @staticmethod
    def close_connection() -> None:
        if RedisDB.get_connection() is not None:
            RedisDB.__instance.close()
            RedisDB.__instance = None

    @staticmethod
    def add_new_value(data: str) -> None:
        RedisDB.get_connection().rpush('signals', data)
    
    @staticmethod
    def get_last_value() -> None:
        return RedisDB.get_connection().lindex('signals', 0)
    
    @staticmethod
    def delete_last_value():
        return RedisDB.get_connection().lpop('signals')

