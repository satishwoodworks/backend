"""
Login Routes
-----------

"""

from fastapi import APIRouter, Request, status

from utils.user import *
from utils.db.login import *


router = APIRouter()

@router.get("/login_user")
async def login_user(email_or_username: str, password: str):
    try:
        hashed_p = hash_password(password)
        data, flag = get_user_data(email_or_username, hashed_p)

        if flag:
            return {"response": data, "status_code": status.HTTP_200_OK}
        else:
            return {"response": "invalid credentials", "status_code": status.HTTP_200_OK}
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}