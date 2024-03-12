from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)
#from aiogram.fsm.context import FSMContext
#from aiogram.fsm.state import State, StatesGroup
#
#
#class MenuStates(StatesGroup):
#    menu = State()
#    settings = State()
#    settingsLanguage = State()
#    settingsMoneyLimit = State()
#    settingsListOfCoins = State()
#

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Settings")
        ]
    ],
    resize_keyboard=True
)

settings_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Language"),
            KeyboardButton(text="Money Limit"),
        ],
        [
            KeyboardButton(text="List of Coins"),
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)