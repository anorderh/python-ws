import asyncio
from websockets.asyncio.server import serve
import websockets
from shared import WEBSOCKET_HOSTNAME, WEBSOCKET_PORT
import uuid

sockets = {}

async def assign(websocket):
    # Generate UUID and store in dict.
    client_uuid = str(uuid.uuid1())
    sockets[client_uuid] = websocket
    return client_uuid

async def broadcast(websocket):
    # Return UUID to client.
    client_uuid = await assign(websocket)
    print(f"Connection made with Client {client_uuid}")
    await websocket.send(client_uuid)

    try:
        # Stream messages to all clients.
        async for message in websocket:
            print(message)

            # Distribute to other clients.
            for client_uuid, socket in sockets.items():
                if (websocket != socket):
                    await socket.send(message)
                    # print(f"Sent message to {client_uuid}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        del sockets[client_uuid]

async def main():
    print("Server started!")
    async with serve(broadcast, WEBSOCKET_HOSTNAME, WEBSOCKET_PORT) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())