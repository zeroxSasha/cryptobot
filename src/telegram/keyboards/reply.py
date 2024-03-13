from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

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