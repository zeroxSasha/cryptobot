import asyncio
from dotenv import load_dotenv
from os import getenv
from json import loads

from api.coinmarketcap import get_top_coins


class CoinMarketCapStorage:
    __top25 = list()
    __top50 = list()

    @staticmethod
    async def run_coinmarketcap() -> None:
        try:
            while True:
                coins = await get_top_coins()
                for index, value in enumerate(coins, 1):
                    if index < 26:
                        CoinMarketCapStorage.__top25.append(value)
                    else:
                        CoinMarketCapStorage.__top50.append(value)
                
                await asyncio.sleep(43200)
        except Exception as e:
            print(f'[Error] {e}')
    
    async def get_top_25_coins() -> list[str]:
        return CoinMarketCapStorage.__top25

    async def get_top_50_coins() -> list[str]:
        return CoinMarketCapStorage.__top50
