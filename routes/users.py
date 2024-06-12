"""
User Routes
-----------

- CREATE user
- Verify user
- READ user
- Complete user profile
"""

import uuid
import random
from fastapi import APIRouter, Request, status

from models.user import User, Verify_User
from utils.user import *
from utils.db.users import *


router = APIRouter()

@router.post("/create_user")
async def create_user(params: User):
    """ create user

    Args:

    """
    try:
        hashed_p = hash_password(params.password)
        salt = generate_random_string()
        myuuid = str(uuid.uuid4())
        code = random.randint(100000, 999999)
        formatted_email = BODY.format(verification_code = str(code))

        if not check_email_duplication(params.email):
            if not check_username_duplication(params.username):

                insert_user_data(myuuid, params.username, params.email, 
                                params.firstname, params.lastname,
                                params.dob, params.gender.upper(),
                                hashed_p, salt)
                
                send_email(SUBJECT, formatted_email, SENDER_EMAIL, params.email, SENDER_KEY)

                return {"message": "User created successfully"}
            
            else:
                return {"message": "username already exists."}
            
        else:
            return {"message": "Email already exists."}
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.post("/verify_user")
async def verify_user(params: Verify_User):
    """ Verify user by user_id

    Args:
        user_id, code
    """
    try:
        if update_user_status(params.user_id):
            return {"message": "Verification successful."}
        else:
            return {"message": "Verification unsuccessful."}
        
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.get("/{userid}")
async def read_user(userid: str):
    """ Read user by userid

    Args:
        userid (uuid): User ID
    """
    ...
