from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: int

class UserOut(BaseModel):
    id: int
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

