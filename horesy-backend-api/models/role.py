from configs.config_sqlalchemy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from base import Model

class Role(Model):
    __tablename__ = 'users'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    update_at = Column(DateTime, nullable=True)
    
    users = relationship('HotelUserRole', backref='role', cascade="all, delete, delete-orphan")