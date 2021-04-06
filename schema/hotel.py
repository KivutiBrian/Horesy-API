from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

    # pid = Column(String, nullable=False, unique=True)
    # id = Column(BIGINT, nullable=False, primary_key=True)
    # picture = Column(String, nullable=True)
    # hotel_name = Column(String, nullable=False, unique=True)
    # facilities = Column(Text, nullable=True)
    # physical_location = Column(String, nullable=True)
    # coordinates = Column(JSON, nullable=True)
    # owner_first_name = Column(String, nullable=False)
    # owner_last_name = Column(String, nullable=False)
    # verified = Column(Boolean, default=False)
    # created_at = Column(DateTime, default=func.now(), nullable=False)
    # update_at = Column(DateTime, nullable=True)


class HotelBase(BaseModel):
    hotel_name: str
    owner_first_name: str
    owner_first_name: str

class HotelPost(HotelBase):
    pass

class HotelPut(BaseModel):
    pass

class Hotel(HotelBase):
    pid: str
    id: str
    verified: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
       orm_mode = True
 
