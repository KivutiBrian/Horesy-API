from configs.config_sqlalchemy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from base import Model

class Reservation(Model):
    __tablename__ = 'reservations'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)