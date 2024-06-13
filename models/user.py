from pydantic import BaseModel
from pydantic import EmailStr, PastDate, Field


class User(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    password: str = Field(..., min_length=8)
    dob: PastDate
    gender: str


class Verify_User(BaseModel):
    user_id: str
    verification_code: str