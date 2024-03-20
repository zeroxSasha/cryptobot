import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from telegram.keyboards import reply
from telegram.utils import states

router = Router()


@router.message(F.text.lower() == '🔧settings')
async def settings(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.settings)
    await message.answer(f'I analyze the market', reply_markup=reply.settings_kb)

@router.message(F.text.lower() == '🇺🇸🇺🇦language')
async def settings(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.language)
    await message.answer(f'🇺🇸🇺🇦Language', reply_markup=reply.language_kb)

@router.message(F.text.lower() == '💰money limit')
async def settings(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.moneylimit)
    await message.answer(f'💰Money Limit', reply_markup=reply.moneylimit_kb)

@router.message(F.text.lower() == '🪙list of coins')
async def settings(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.listofcoins)
    await message.answer(f'🪙List of Coins', reply_markup=reply.listofcoins_kb)

@router.message(F.text.lower() == "🔻cancel")
async def return_back(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    if current_state in ['ChatStates:language', 'ChatStates:moneylimit', 'ChatStates:listofcoins']: 
        await state.set_state(states.ChatStates.settings)
        await message.answer("🔻Cancel", reply_markup=reply.settings_kb)
    if current_state == 'ChatStates:settings':
        await state.clear()
        await message.answer("🔻Cancel", reply_markup=reply.main_kb)
