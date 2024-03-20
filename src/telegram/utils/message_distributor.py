import asyncio

from telegram import bot
from api import api
from data import db


async def send_to_all_users(id: int, text: str) -> None:
    tgbot = await bot.TelegramBot.get_bot()
    while True:
        await tgbot.send_message(id, text)
        await asyncio.sleep(3)
