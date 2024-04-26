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
            if isinstance(message, str):
                print("Received string message from client:", message)
                await websocket.send("---> "+message)  # 向客户端发送消息
            elif isinstance(message, bytes):
                print("Received byte message from client byte []->:", len(message))
                # 如果需要将字节数组解码为字符串，可以使用 message.decode('utf-8') 等方法
            else:
                print("Received unknown type of message from client")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")

async def start_server():
    server = await websockets.serve(echo, "192.168.2.173", 8765)  # 设置连接超时时间为 30 秒
    await server.wait_closed()

asyncio.run(start_server())
