from sqlalchemy import Column, Integer, Boolean, DateTime
from db.base_class import Base


class ButtonEvent(Base):
    id = Column(Integer, primary_key=True, index=True)
    is_long_click = Column(Boolean, default=False)
    pushed_time = Column(DateTime)
