import asyncio
import websockets
import websockets.exceptions

# lsof -i :8080
"""
kill -9 2543
"""

'''
python 代码注释
'''

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")

async def start_server():
    server = await websockets.serve(echo, "192.168.2.173", 8765)
    await server.wait_closed()

asyncio.run(start_server())
