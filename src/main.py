from telegram import bot
from data.postgre_db import postgre_main
from data.redis_db import redis_main
from api import binance
import asyncio
import logging
import sys

async def main():
    await redis_main.RedisDB.get_connection()

    bot_task = asyncio.create_task(bot.run_telegram())
    binance_task = asyncio.create_task(binance.run_websocket())
    await asyncio.gather(bot_task, binance_task)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        postgre_main.DataBase.get_connection()

        asyncio.run(main())
    except Exception as e:
        print(f'[Error] {e}')
    finally:
        postgre_main.DataBase.close_connection()
