from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    joined_date: datetime = None

    class Config:
        # If necessary, you can add configuration options here
        arbitrary_types_allowed = True  # Allow arbitrary types like datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str
