from pydantic import BaseModel, EmailStr

class LinkID(BaseModel):
    email: EmailStr
    linked_id: str
