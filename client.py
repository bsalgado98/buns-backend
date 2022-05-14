import asyncio 
import websockets
import json


def parse_event(event: str) -> (str, str):
    event = event.split(":")
    api = event[0]
    fn = event[1]
    return api, fn


# create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    data = json.loads(data)
    event = data['event']
    payload = data['payload']

    api, fn = parse_event(event)

    if api == 'lobby':
        if fn == 'add_player':
            player = payload['player']
            lobby.add_player(player)
            await websocket.send(lobby.players)


class Lobby:
    players = []

    def add_player(self, player: str):
        print('player added:', player)
        self.players.append(player)
        

if __name__ == "__main__":
    start_server = websockets.serve(handler, "localhost", 8000)

    lobby = Lobby()

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
