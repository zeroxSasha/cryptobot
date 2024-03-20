from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    print(DataBase.get_connection())
    #db_connection.add_new_user(message.from_user.id, 0, 0, 0)
    await message.answer(f'Welcome to Crypto Bot 24/7', reply_markup=reply.main_kb)

