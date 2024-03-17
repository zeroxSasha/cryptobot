import websocket
import json
import asyncio
from dotenv import load_dotenv
from os import getenv


def on_message(ws, message):
    data = json.loads(message)

    info = {
        'Symbol': data['o']['s'],
        'Side': data['o']['S'],
        'Total': round(float(data['o']['p']) * float(data['o']['q']), 2),
        'Average Price': data['o']['ap'],
    }

    print(info)


def on_error(ws, error):
        print(f'WebSocket error: {error}')


async def run_websocket():
    load_dotenv()
    ws = websocket.WebSocketApp(getenv('WEBSOCKET'), on_message=on_message, on_error=on_error)
    await ws.run_forever()

asyncio.run(run_websocket())
