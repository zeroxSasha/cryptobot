from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔧Settings")
        ]
    ],
    resize_keyboard=True
)

settings_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰Money Limit"),
            KeyboardButton(text="🪙List of Coins"),
        ],
        [
            KeyboardButton(text="🔻Cancel")
        ]
    ],
    resize_keyboard=True
)

moneylimit_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔻Cancel")
        ]
    ],
    resize_keyboard=True
)

listofcoins_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎱All Coins"),
            KeyboardButton(text="🎱Top 25 and Higher"),
            KeyboardButton(text="🎱Top 50 and Higher"),
        ],
        [
            KeyboardButton(text="🔻Cancel")
        ]
    ],
    resize_keyboard=True
)
