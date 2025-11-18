from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Contact(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    message: str = Field(..., min_length=1, max_length=5000)

class ContactResponse(BaseModel):
    id: str
    status: str
    message: str

