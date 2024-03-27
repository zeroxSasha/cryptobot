import websockets
import json
import asyncio

from data.redis_db import redis_main


def on_message(message) -> dict:
    data = json.loads(message)

    info = {
        'Symbol': data['o']['s'],
        'Side': data['o']['S'],
        'Total': round(float(data['o']['p']) * float(data['o']['q']), 2),
        'Average Price': data['o']['ap'],
    }
    
    if info['Total'] > 5000:
        redis_main.RedisDB.add_new_value(json.dumps(info))

async def run_websocket() -> None:
    while True:
        try:
            print('Connecting to Binance WebSocket...')
            async with websockets.connect(f'wss://fstream.binance.com/ws/!forceOrder@arr') as ws:
                async for message in ws:
                    on_message(message)

        except Exception as e:
            print(f'WebSocket connection error: {e}')
            await asyncio.sleep(5)
