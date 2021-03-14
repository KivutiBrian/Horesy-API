from configs.config_sqlalchemy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from base import Model

class User(Model):
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
