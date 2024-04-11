import asyncio
import websockets

connected_clients = set()
current_player = 1

async def handle_client(websocket, path):
    global current_player
    connected_clients.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            # Handle messages from clients if necessary
            # For player switching logic, simply broadcast the current player to all clients
            await broadcast(str(current_player))
    finally:
        connected_clients.remove(websocket)

async def broadcast(message):
    if connected_clients:
        await asyncio.wait([client.send(message) for client in connected_clients])

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
