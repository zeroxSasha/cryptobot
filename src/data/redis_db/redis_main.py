import redis
from dotenv import load_dotenv
from os import getenv


class RedisDB:
    __instance = None

    @staticmethod
    async def get_connection() -> redis.Redis:
        if not RedisDB.__instance:
            try:
                load_dotenv()
                RedisDB.__instance = redis.asyncio.from_url(getenv('REDIS_URL'))
                await RedisDB.__instance.flushall(asynchronous=True)
                print('Redis connection established')
            except Exception as e:
                print(f'[Error] {e}')
        
        return RedisDB.__instance
    
    @staticmethod
    async def close_connection() -> None:
        if RedisDB.__instance is not None:
            await RedisDB.__instance.aclose()
            RedisDB.__instance = None

    @staticmethod
    async def add_new_value(data: str) -> None:
        await RedisDB.__instance.rpush('signals', data)
    
    @staticmethod
    async def get_last_value() -> bytes:
        return await RedisDB.__instance.lindex('signals', 0)
    
    @staticmethod
    async def delete_last_value() -> bytes:
        return await RedisDB.__instance.lpop('signals')
