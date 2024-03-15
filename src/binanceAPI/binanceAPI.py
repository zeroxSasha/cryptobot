import websocket
import json

socket = 'wss://fstream.binance.com/ws/!forceOrder@arr'

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


ws = websocket.WebSocketApp(socket, on_message=on_message, on_error=on_error)
ws.run_forever()
