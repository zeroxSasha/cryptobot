from aiogram.fsm.state import State, StatesGroup


class ChatStates(StatesGroup):   
    settings = State()
    language = State()
    money_limit = State()
    coins = State()

