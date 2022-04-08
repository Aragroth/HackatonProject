from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import schemas
import models


class CRUDButtonEvent:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, *, obj_in: schemas.ButtonEvent) -> models.ButtonEvent:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> schemas.ButtonEvent:
        return db.query(self.model).filter(self.model.id == id).first()


button = CRUDButtonEvent(models.ButtonEvent)
