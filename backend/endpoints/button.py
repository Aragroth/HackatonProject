"""
Обрабатывает код, который пользователь вводит в бразузерном редакторе кода
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from db import session
from endpoints.utils import add_time_to_event

router = APIRouter()


@router.get("/{button_id}")
async def get_snippet(button_id: str, db: Session = Depends(session.get_db)) -> schemas.ButtonEvent:
    return crud.button.get(db, button_id)


@router.post("/")
async def save_button_event(
        new_button_click: schemas.ButtonEvent = Depends(add_time_to_event),
        db: Session = Depends(session.get_db),
):
    crud.button.create(db, obj_in=new_button_click)
    return {"response": "ok"}
