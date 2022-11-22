import asyncio
import websockets
import json
import time

from celery.contrib.abortable import AbortableTask
from quiz.celery import app


class WebsocketSenders:
    HOST = 'localhost:8000'
    LOOP = asyncio.get_event_loop()

    @classmethod
    def send_code(cls, code: str) -> None:

        async def code_sender():
            async with websockets.connect(f'ws://{cls.HOST}/timer/') as websocket:
                await websocket.send(code)
                await websocket.recv()

        cls.LOOP.run_until_complete(code_sender())

    @classmethod
    def send_state(cls, state, game_pk):
        connection_url = f'ws://{cls.HOST}/game-change-state/'
        print('send_state')

        async def state_sender():
            async with websockets.connect(connection_url) as websocket:
                await websocket.send(json.dumps({
                    'pk': game_pk,
                    'event_data': state
                }))
                await websocket.recv()

        cls.LOOP.run_until_complete(state_sender())


@app.task(bind=True, base=AbortableTask)
def set_timer(self, time_for: float, code):
    try:
        time.sleep(time_for - 2)
    except ValueError:
        pass
    if self.is_aborted():
        return

    WebsocketSenders.send_code(code)


@app.task
def send_state_to_consumer(state: str, game_pk: int):
    print('send_state_to_consumer...')
    WebsocketSenders.send_state(state=state, game_pk=game_pk)
