from fastapi import APIRouter, Depends, HTTPException, Form, Body

# models
from models.user import User

# schema 

# service

# settings

# utils

router = APIRouter(
    prefix='/auth',
    tags=['AUTH'],
    responses={200:{'description':'Ok'},201:{'description':'created'},400: {"description": "Bad Request"},404: {"description": "Not found"}}
)

