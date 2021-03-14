from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    description: str

class RolePost(RoleBase):
    pass

class RolePut(RoleBase):
    pass

class Role(RoleBase):
    pid: int
    id: int
    visible: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]