from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from telegram.keyboards import reply
from data.db import DataBase
from telegram.utils import message_distributor

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    DataBase.add_new_user(message.from_user.id, 0, 0, 0)
    await message_distributor.send_to_all_users(message.from_user.id, "hello, dude")
    await message.answer(f'Welcome to Crypto Bot 24/7', reply_markup=reply.main_kb)

