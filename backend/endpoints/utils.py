import datetime
from typing import List
from fastapi import FastAPI, WebSocket

import schemas


async def add_time_to_event(button_event: schemas.ButtonEventBase) -> schemas.ButtonEvent:
    return schemas.ButtonEvent(pushed_time=datetime.datetime.now(), **button_event.dict())


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                pass


manager = ConnectionManager()