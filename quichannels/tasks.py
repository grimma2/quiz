import logging
import time

import websockets
import asyncio

from celery.contrib.abortable import AbortableTask
from celery.signals import task_revoked, task_postrun

from quiz.celery import app
from quiz.settings import SECRET_KEY


async def send_code(host: str, code: str) -> None:
    async with websockets.connect(f'ws://{host}/timer/{SECRET_KEY}/') as websocket:
        await websocket.send(code)
        await websocket.recv()


@app.task(bind=True, base=AbortableTask)
def set_timer(self, time_for: float, code):
    time.sleep(time_for)

    if self.is_aborted():
        return

    host = 'localhost:8000'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_code(host, code))


@task_revoked.connect(sender=set_timer)
def timer_revoked(sender=None, **kwargs):
    logging.getLogger('DL').info('timer_revoked')


@task_postrun.connect(sender=set_timer)
def timer_postrun(sender=None, **kwargs):
    logging.getLogger('DL').info('timer_postrun')