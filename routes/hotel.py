from fastapi import APIRouter, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
from typing import List

# schema 
from schema import hotel, user, token

# service
from services.hotel_service import HotelService

# settings
from configurations.sqlalchemy_config import get_db

# utils

router = APIRouter(
    prefix='/hotels',
    tags=['HOTEL SERVICE'],
    responses={200:{'description':'Ok'},201:{'description':'created'},400: {"description": "Bad Request"},404: {"description": "Not found"}}
)


# register a hotel
@router.post('',
summary='register a hotel',
response_model=token.Token,
response_description="list of all users",
status_code=201,
)
async def register_hotel(hotel: hotel.HotelPost, db:Session = Depends(get_db)):
    return HotelService.register_hotel(hotel_payload=hotel, db=db)
