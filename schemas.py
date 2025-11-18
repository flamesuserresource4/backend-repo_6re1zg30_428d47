from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Contact form payload from the portfolio site
class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Sender full name")
    email: EmailStr = Field(..., description="Sender email address")
    message: str = Field(..., min_length=5, max_length=5000, description="Message body")
    company: Optional[str] = Field(None, max_length=150, description="Optional company name")


class ContactResponse(BaseModel):
    status: str
    id: Optional[str] = None
    message: str
