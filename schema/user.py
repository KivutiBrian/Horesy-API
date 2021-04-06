from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

    # picture = Column(String, nullable=True)
    # first_name = Column(String, nullable=False) 
    # last_name = Column(String, nullable=False) 
    # email = Column(String, nullable=False, unique=True) 
    # password = Column(String, nullable=False)

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserPost(UserBase):
    password: str

class UserPut(BaseModel):
    profile_url:Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    password: Optional[str]

class User(UserBase):
    pid: str
    id: int
    verified: bool
    active_status: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
       orm_mode = True
 
    
