from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr  # Use EmailStr for email validation
    city: str
    interests: List[str]

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[EmailStr] = None  # Use EmailStr for email validation
    city: Optional[str] = None
    interests: Optional[List[str]] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
