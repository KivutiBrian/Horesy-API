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
    phone_number = Column(String, nullable=True)
    password = Column(String, nullable=False)
    active_status = Column(Integer, nullable=False, default=1) # 0-retired 1-active 2-suspended 3-blocked
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True)

    hotels = relationship('HotelUserRole', back_populates='user', cascade="all, delete, delete-orphan")
