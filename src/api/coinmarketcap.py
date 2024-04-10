import json
import asyncio
import aiohttp
from dotenv import load_dotenv
from os import getenv

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': getenv('COINMARKETCAP_API_KEY'),
}


async def run_coinmarketcap() -> list[str]:
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=parameters) as response:
            response.raise_for_status()
            
            data = await response.json()
            coins = list()
            for i in data['data']:
                coins.append(i['symbol'].lower() + 'usdt')
            
            return coins

if __name__ == '__main__':
    asyncio.run(run_coinmarketcap())
