from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base


class Role(Model, Base):
    __tablename__ = 'roles'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    update_at = Column(DateTime, nullable=True)
    
    users = relationship('HotelUserRole', backref='role', cascade="all, delete, delete-orphan")