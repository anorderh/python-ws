import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        # Listen for messages from the client
        async for message in websocket:
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, 'localhost', 12345)
    print("Listening!");
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())