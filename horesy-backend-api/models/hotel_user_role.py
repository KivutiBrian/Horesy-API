from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base

class HotelUserRole(Model, Base):
    __tablename__ = 'hotel_users_roles'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())

    hotel = relationship('Hotel', back_populates='users')
    user = relationship('User', back_populates='hotels')