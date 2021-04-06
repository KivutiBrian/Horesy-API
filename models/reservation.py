from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, Text
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base


class Reservation(Model, Base):
    __tablename__ = 'reservations'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)