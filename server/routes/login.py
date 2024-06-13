"""
Login Routes
-----------

"""

from fastapi import APIRouter, status

from ..utils.user import hash_password
from ..utils.db import login


router = APIRouter()

@router.get("/login_user")
async def login_user(email_or_username: str, password: str):
    try:
        hashed_p = hash_password(password)
        data, flag = login.get_user_data(email_or_username, hashed_p)

        if flag:
            return {"response": data, "status_code": status.HTTP_200_OK}
        else:
            return {"response": "Invalid Credentials", "status_code": status.HTTP_200_OK}
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}