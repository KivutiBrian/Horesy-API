from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy config
from configurations.sqlalchemy_config import engine

# model
from models.hotel import *
from models.role import *
from models.user import *
from models.hotel_user_role import *
from models.roomtype import *
from models.room import *
from models.reservation import *

# create all tables
# Base.metadata.create_all(bind=engine)
# drop all tables
Base.metadata.create_all(bind=engine)

# routes
from routes import (auth,user, hotel, role)

app = FastAPI(
    title='Horesy API',
    version='0.0.1',
    description='services and endpoints for Horesy',
    redoc_url='/'
)

# setup the origins
origins = ["http://localhost","http://localhost:3000","http://127.0.0.1", ]

# add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include the routers
app.include_router(role.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(hotel.router)
