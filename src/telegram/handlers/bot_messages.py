from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply

router = Router()


@router.message(F.text.lower() == 'settings')
async def settings(message: Message) -> None:
    await message.answer(f'I analyze a market',
        reply_markup=reply.settings_kb)
