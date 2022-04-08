import datetime

from pydantic import BaseModel


# Подаётся на сервер
class ButtonEventBase(BaseModel):
    id: int
    is_long_click: bool


class ButtonEvent(ButtonEventBase):
    pushed_time: datetime.datetime