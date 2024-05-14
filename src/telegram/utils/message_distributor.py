import json

from telegram import bot
from data.postgre_db import postgre_main
from data.redis_db import redis_main
from data.variable_storage.coinmarketcap_storage import CoinMarketCapStorage

async def send_to_all_users() -> None:
    tgbot = await bot.TelegramBot.get_bot()
    while True:
        data = await redis_main.RedisDB.delete_last_value()
        if data:
            users = postgre_main.DataBase.get_all_users()
            data = json.loads(data)
            for user in users:
                id = user[0]
                money_limit = user[2]
                list_of_coins = user[3]

                if money_limit * 1000 < int(data['Total']):
                    if data['Side'] == 'BUY':
                        await tgbot.send_message(id, f"🔴 #{data['Symbol']} Liquidated Long: ${data['Total']} at ${data['Average Price']}")
                    else:
                        await tgbot.send_message(id, f"🟢 #{data['Symbol']} Liquidated Short: ${data['Total']} at ${data['Average Price']}")
