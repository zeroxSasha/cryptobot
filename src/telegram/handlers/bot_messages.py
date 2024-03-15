import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import reply
from utils import states

router = Router()


@router.message(F.text.lower() == 'settings')
async def settings(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.settings)
    await message.answer(f'I analyze the market', reply_markup=reply.settings_kb)

@router.message(F.text.lower() == "cancel")
async def return_back(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return 
        
    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer("Cancelled", reply_markup=reply.main_kb)
