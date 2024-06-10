from pydantic import BaseModel
from pydantic import EmailStr, PastDate, UUID1


class User(BaseModel):
    userid: UUID1
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    dob: PastDate
    gender: str
    