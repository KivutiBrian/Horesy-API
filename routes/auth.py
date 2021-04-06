from fastapi import APIRouter, Depends, HTTPException, Form, Body
from fastapi.security import OAuth2PasswordBearer

# google auth configurations
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth
from google.oauth2 import id_token
from google.auth.transport import requests as google_auth_request
import requests

# models
from models.user import User

# schema 
from schema import token, user, hotel

# service

# settings
from configurations.base_config import settings

# utils
from utils.security import *

# define the url the client will use to access the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

router = APIRouter(
    prefix='/auth',
    tags=['AUTH'],
    responses={200:{'description':'Ok'},201:{'description':'created'},400: {"description": "Bad Request"},404: {"description": "Not found"}}
)

# login
@router.post('/login',
summary='login to get access token',
response_model=token.Token,
status_code=200
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user":user}

# google signin
@router.post('/login/google',
summary='use this endpoint to send google token to server',
response_model=token.Token,
status_code=200,
)
async def auth(token, db:Session=Depends(get_db)):
    try:

        
        req = google_auth_request.Request()
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, req,settings.CLIENT_ID )
        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        # userid = idinfo['sub']

        # check if useer exists
        user = db.query(UserModel).filter(UserModel.email==idinfo['email']).first()
        if user:
            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": str(user.id)}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer","user":user}
        else:
            # create user...
            record = User(public_id=str(uuid4()),profile_url=idinfo['picture'],email=idinfo['email'], first_name=idinfo['family_name'], last_name=idinfo['given_name'],
                            password='1234')

            db.add(record)
            db.commit()
            db.refresh(record)

            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": str(record.id)}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer", "user":user}
    except ValueError:
    # Invalid token
        pass

# get current logged in user
@router.get("/users/me/", 
summary="return authorized user",
# response_model=user.SingleUserOut,
)
async def read_users_me(current_user: user.User = Depends(get_current_active_user)):
    return current_user
 

