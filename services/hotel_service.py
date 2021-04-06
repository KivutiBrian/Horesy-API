from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
import string
import random
import uuid

# model
from models.hotel import Hotel
from models.role import Role
from models.user import User
from models.hotel_user_role import HotelUserRole

# schema
from schema import user, token, hotel, role

# utils
from utils.security import *

# configs
from configurations.base_config import settings

class HotelService:

    @classmethod
    def register_hotel(cls, hotel_payload: hotel.HotelPost, db: Session):
        """register a hotel"""