import asyncio
import sys
from websockets.asyncio.client import connect
from shared import WEBSOCKET_HOSTNAME, WEBSOCKET_PORT, WEBSOCKET_URL
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

class Client:
    uuid = None
    history = []

    @staticmethod
    async def start(websocket):
        # Wait until server assigns client UUID.
        Client.uuid = await websocket.recv()
        print(f"Joined server as Client {Client.uuid}")

        # Run async tasks.
        await asyncio.gather(
            Client.chat(websocket),
            Client.display(websocket)
        )

    @staticmethod
    async def chat(websocket):
        session = PromptSession(f"Client {Client.uuid}: ")
        with patch_stdout():  # Allows other prints while typing.
            while True:
                text = await session.prompt_async()
                await websocket.send(f"Client {Client.uuid}: {text}")

    @staticmethod
    async def display(websocket):
        while True:
            message = await websocket.recv()
            print(message)

async def main():
    async with connect(WEBSOCKET_URL) as websocket:
        await Client.start(websocket)

if __name__ == "__main__":
    asyncio.run(main())