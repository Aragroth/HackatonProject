from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import schemas
import models


class CRUDButtonEvent:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, *, obj_in: schemas.ButtonEvent) -> models.ButtonEvent:
        button_clicked = db.query(models.Button).filter(models.Button.id == obj_in.button_id).first()
        if button_clicked is None:
            raise HTTPException(status_code=404, detail="Button id is not found")
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, button=button_clicked)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> schemas.ButtonEvent:
        return db.query(self.model).filter(self.model.id == id).first()


button = CRUDButtonEvent(models.ButtonEvent)
