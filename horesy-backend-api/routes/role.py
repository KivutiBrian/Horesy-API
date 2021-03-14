from fastapi import APIRouter, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
from typing import Optional, List

# models
from models.role import Role

# schema 
from schema import role, user

# service
from services.role_service import RoleService

# settings
from configurations.sqlalchemy_config import get_db

# utils
from utils.security import *

router = APIRouter(
    prefix='/roles',
    tags=['ROLES SERVICES'],
    responses={200:{'description':'Ok'},201:{'description':'created'},400: {"description": "Bad Request"},404: {"description": "Not found"}}
)

"""GET A LIST OF ALL ROLES"""
@router.get('',
summary='get a list of all roles',
response_model=List[role.Role],
response_description="list of all users",
status_code=200, 
)
async def get_roles(db:Session = Depends(get_db)):#, current_user: user_schema.User = Depends(get_current_active_user)
    return RoleService.get_roles(db=db)

"""GET A ROLE BY PUBLIC ID"""
@router.get('/{public_id}',
summary='get role details that matches the roleId provided',
# response_model=role.RoleWithUsers,
response_description="list of all users",
status_code=200,
)
async def get_role(public_id:str, db:Session=Depends(get_db), current_user: user.User = Depends(get_current_active_user)):
    return RoleService.get_role(role_public_id=public_id, db=db)

""""CREATE A ROLE"""
@router.post('',
summary='create a new role',
response_model=role.Role,
response_description="list of all users",
status_code=200,
)
async def create_role(rolePayload: role.RolePost, db:Session=Depends(get_db)): #, current_user: user_schema.User = Depends(get_current_active_user)
    return RoleService.create_new_role(roleData=rolePayload, db=db)


"""EDIT A ROLE"""
@router.put('/{public_id}',
summary='edit role details',
response_model=role.Role,
response_description="list of all users",
status_code=200,
)
async def edit_role(public_id:str,rolePayload: role.RolePut, db: Session= Depends(get_db), current_user: user.User = Depends(get_current_active_user)):
    return RoleService.update_role_details(role_public_id=public_id, roleData=rolePayload, db=db)
