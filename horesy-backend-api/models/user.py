from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base


class User(Model, Base):
    __tablename__ = 'users'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)
    picture = Column(String, nullable=True)
    first_name = Column(String, nullable=False) 
    last_name = Column(String, nullable=False) 
    email = Column(String, nullable=False, unique=True) 
    password = Column(String, nullable=False)
    verified = Column(Boolean, default=False)

    hotels = relationship('HotelUserRole', back_populates='user', cascade="all, delete, delete-orphan")
