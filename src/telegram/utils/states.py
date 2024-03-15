from aiogram.fsm.state import State, StatesGroup


class ChatStates(StatesGroup):   
    settings = State()
    language = State()
    moneylimit = State()
    listofcoins = State()

