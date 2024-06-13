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
import datetime
from fastapi import APIRouter, status

from config import OTPS
from models.user import User, VerifyUser
from templates.verification_email import BODY, SENDER_EMAIL, SENDER_KEY, SUBJECT
from ..utils.user import hash_password, generate_random_string, send_email
from ..utils.db import users


router = APIRouter()

@router.post("/create_user")
async def create_user(params: User):
    """ CREATE user

    Args:

    """
    try:
        hashed_p = hash_password(params.password)
        salt = generate_random_string()
        myuuid = str(uuid.uuid4())
        code = random.randint(100000, 999999)
        formatted_email = BODY.format(verification_code = str(code))

        if not users.check_email_duplication(params.email):
            if not users.check_username_duplication(params.username):

                users.insert_user_data(myuuid, params.username, params.email, 
                                params.firstname, params.lastname,
                                params.dob, params.gender.upper(),
                                hashed_p, salt)
                
                send_email(SUBJECT, formatted_email, SENDER_EMAIL, params.email, SENDER_KEY)

                OTPS[str(code)] = { "created": datetime.datetime.now() }

                return {"message": "User created successfully"}
            
            else:
                return {"message": "username already exists."}
            
        else:
            return {"message": "Email already exists."}
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.post("/verify_user")
async def verify_user(params: VerifyUser):
    """ Verify user by user_id

    Args:
        user_id, code
    """
    try:
        if params.verification_code in OTPS:
            # TODO: Check Time of OTP before verifying
            users.update_user_status(params.user_id)
            del OTPS[params.verification_code]
            return {"message": "Verification successful."}
        else:
            return {"message": "Verification unsuccessful."}
        
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.get("/{userid}")
async def read_user(userid: str):
    """ READ user by userid

    Args:
        userid (uuid): User ID
    """
    ...
