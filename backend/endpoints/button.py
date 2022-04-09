"""
Обрабатывает код, который пользователь вводит в бразузерном редакторе кода
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from db import session
from endpoints.utils import add_time_to_event, manager

router = APIRouter()


@router.post("/")
async def save_button_event(
        new_button_click: schemas.ButtonEvent = Depends(add_time_to_event),
        db: Session = Depends(session.get_db),
):
    crud.button.create(db, obj_in=new_button_click)
    await manager.broadcast({
        "id": new_button_click.button_id,
        'status': 'clicked' if not new_button_click.is_long_click else 'double_click',
        'button_address': 'test',
    })

    return {"response": "ok"}
