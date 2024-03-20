from telegram import bot
from data.db import DataBase
import asyncio
import logging
import sys

if __name__ == '__main__':
    try:
        DataBase.get_connection()
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(bot.TelegramBot.start_bot())
    except Exception as e:
        print(f'[Error] {e}')
    finally:
        DataBase.close_connection()
