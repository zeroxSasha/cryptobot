from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from telegram.handlers import bot_messages, user_commands 


class TelegramBot:
    __instance = None

    @staticmethod
    async def start_bot() -> None:
        load_dotenv()
        TelegramBot.__instance = Bot(token=getenv('TELEGRAM_API_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dp = Dispatcher()

        dp.include_routers(
            user_commands.router,
            bot_messages.router
        )

        await TelegramBot.__instance.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(TelegramBot.__instance)

    @staticmethod
    async def get_bot() -> Bot:
        return TelegramBot.__instance

