import json

from telegram import bot
from data.postgre_db import postgre_main
from data.redis_db import redis_main
from data.variable_storage.coinmarketcap_storage import CoinMarketCapStorage

async def send_to_all_users() -> None:
    tgbot = await bot.TelegramBot.get_bot()
    while True:
        binance_liquidation = await redis_main.RedisDB.delete_last_value()
        if binance_liquidation:
            users = postgre_main.DataBase.get_all_users()
            binance_liquidation = json.loads(binance_liquidation)
            top25_coins = await CoinMarketCapStorage.get_top_25_coins()
            top50_coins = await CoinMarketCapStorage.get_top_50_coins()
            short_symbol_form = binance_liquidation['Symbol'][:-4]

            for user in users:
                id = user[0]
                money_limit = user[2]
                list_of_coins = user[3]

                if money_limit * 1000 < int(binance_liquidation['Total']):
                    if list_of_coins == 0: # all of the coins
                        print("all")
                        if binance_liquidation['Side'] == 'BUY':
                            await tgbot.send_message(id, f"🔴 #{binance_liquidation['Symbol']} Liquidated Long: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                        else:
                            await tgbot.send_message(id, f"🟢 #{binance_liquidation['Symbol']} Liquidated Short: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                    elif list_of_coins == 25 and short_symbol_form not in top25_coins: # not in first 25
                        print("25")
                        if binance_liquidation['Side'] == 'BUY':
                            await tgbot.send_message(id, f"🔴 #{binance_liquidation['Symbol']} Liquidated Long: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                        else:
                            await tgbot.send_message(id, f"🟢 #{binance_liquidation['Symbol']} Liquidated Short: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                    elif list_of_coins == 50 and short_symbol_form not in top25_coins and binance_liquidation['Symbol'] not in top50_coins: # not in first 50
                        print("50")
                        if binance_liquidation['Side'] == 'BUY':
                            await tgbot.send_message(id, f"🔴 #{binance_liquidation['Symbol']} Liquidated Long: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                        else:
                            await tgbot.send_message(id, f"🟢 #{binance_liquidation['Symbol']} Liquidated Short: ${binance_liquidation['Total']} at ${binance_liquidation['Average Price']}")
                        