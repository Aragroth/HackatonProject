from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Button(Base):
    id = Column(String, primary_key=True, index=True)
    place = Column(String, nullable=False)

    events = relationship("ButtonEvent", cascade="all,delete", backref="button")


class ButtonEvent(Base):
    id = Column(Integer, primary_key=True, index=True)
    button_id = Column(String, ForeignKey(Button.id, ondelete='CASCADE'))
    is_long_click = Column(Boolean, default=False)
    pushed_time = Column(DateTime)

