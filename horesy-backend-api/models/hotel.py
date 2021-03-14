from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

from .base import Model
from configurations.sqlalchemy_config import Base


class Hotel(Model, Base):
    __tablename__ = 'hotels'
    pid = Column(String, nullable=False, unique=True)
    id = Column(BIGINT, nullable=False, primary_key=True)
    picture = Column(String, nullable=True)
    hotel_name = Column(String, nullable=False, unique=True)
    facilities = Column(Text, nullable=True)
    physical_location = Column(String, nullable=True)
    coordinates = Column(JSON, nullable=True)
    owner_first_name = Column(String, nullable=False)
    owner_last_name = Column(String, nullable=False)
    verified = Column(Boolean, default=False)

    users = relationship('HotelUserRole', back_populates='hotel', cascade="all, delete, delete-orphan")