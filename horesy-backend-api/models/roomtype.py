from configs.config_sqlalchemy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

class RoomType(Base):
    __tablename__ = 'roomtypes'