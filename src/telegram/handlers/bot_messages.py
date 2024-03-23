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

@router.message(F.text.lower() == '💰money limit')
async def settings_moneylimit(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.moneylimit)
    await message.answer(f'Enter💰Money Limit in k $: ', reply_markup=reply.moneylimit_kb)

@router.message(F.text.lower() == '🪙list of coins')
async def settings_listofcoins(message: Message, state: FSMContext) -> None:
    await state.set_state(states.ChatStates.listofcoins)
    await message.answer(f'🪙List of Coins', reply_markup=reply.listofcoins_kb)

@router.message(F.text.lower() == "🔻cancel")
async def return_back(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    if current_state in ['ChatStates:moneylimit', 'ChatStates:listofcoins']: 
        await state.set_state(states.ChatStates.settings)
        await message.answer("🔻Cancel", reply_markup=reply.settings_kb)
    if current_state == 'ChatStates:settings':
        await state.clear()
        await message.answer("🔻Cancel", reply_markup=reply.main_kb)

# <-- implement adding values to a database -->
@router.message(states.ChatStates.moneylimit)
async def settings_moneylimit_handler(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.answer("❗️Enter only positive values k $: ")
        return
    else:
        await message.answer(f"✔️Money limit set to {message.text}k $", reply_markup=reply.settings_kb)
        await state.set_state(states.ChatStates.settings)

# <-- implement adding values to a database -->
@router.message(states.ChatStates.listofcoins)
async def settings_listofcoins_handler(message: Message, state: FSMContext) -> None:
    if message.text == "🎱All Coins":
        await message.answer(f"✔️All Coins will be shown", reply_markup=reply.settings_kb)
        await state.set_state(states.ChatStates.settings)
    elif message.text == "🎱Top 25 and Higher":
        await message.answer(f"✔️Top 25 and Higher will be shown", reply_markup=reply.settings_kb)
        await state.set_state(states.ChatStates.settings)
    elif message.text == "🎱Top 50 and Higher":
        await message.answer(f"✔️Top 50 and Higher will be shown", reply_markup=reply.settings_kb)
        await state.set_state(states.ChatStates.settings)
    else:
        await message.answer(f"❗️Choose one of the options", reply_markup=reply.listofcoins_kb)

