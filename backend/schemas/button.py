import datetime

from pydantic import BaseModel


class RawTelemetry(BaseModel):
    firstButton: str


class RawButtonEvent(BaseModel):
    data: str


# Подаётся на сервер
class ButtonEventBase(BaseModel):
    button_id: str
    is_long_click: bool


class ButtonEvent(ButtonEventBase):
    pushed_time: datetime.datetime
