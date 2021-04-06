from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Optional, List
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime

# model import
from models.user import User
# configs
from configurations.base_config import settings
from configurations.sqlalchemy_config import SessionLocal, get_db
# schema
from schema import user

"""
*We need to install python-jose to generate and verify the JWT tokens in Python
*PassLib is a great Python package to handle password hashes
"""

# create an obj to manage hashes and related configurations
pwd_context = CryptContext(schemes=['bcrypt'])

# define the url the client will use to access the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# verify password
def verify_password(plain_password, hashed_password):
    """verify hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

# authenticate user with email
def authenticate_user(email:str, password:str, db:Session = Depends(get_db)):
    """authenticate a user using email"""
    user: user_schema.User = db.query(UserModel).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(plain_password=password, hashed_password=user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return user

# create access token
def create_access_token(data: dict,expires_delta:Optional[timedelta]=None ):
    """create an access token"""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    
    # ENCODE TOKEN
    new_data =data.copy()
    new_data.update({'exp':expire})
    token = jwt.encode(claims=new_data, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return token

# get user
def get_user(user_id:int):
    """Get a user that matches the userId provided"""
    db:Session = SessionLocal()
    user: user.User = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    return user

# create get user dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception  
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f'{e}')

    user = get_user(user_id=user_id)
    
    if user is None:
        raise credentials_exception
    return user

#  get active user 
async def get_current_active_user(current_user: user.User =  Depends(get_current_user)):
    if current_user.active_status == 0:
        raise HTTPException(status_code=400, detail='User account is has been retired! Contact support')
    if current_user.active_status ==  1:
        return current_user
    if current_user.active_status == 2:
        raise HTTPException(detail="User account has been suspended! Contact support", status_code=400)
    if current_user.active_status == 3:
        raise HTTPException(detail="User account has been blocked! This action is irreversible", status_code=400)
