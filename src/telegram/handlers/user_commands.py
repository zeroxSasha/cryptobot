from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from telegram.keyboards import reply
from data.postgre_db import postgre_main

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    postgre_main.DataBase.add_new_user(message.from_user.id, 0, 0, 0)
    await message.answer(f'Welcome to Crypto Bot 24/7', reply_markup=reply.main_kb)

