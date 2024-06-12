"""
User Routes
-----------

- CREATE user
- Verify user
- READ user
- UPDATE user
- DELETE user
"""
import uuid
from fastapi import APIRouter, Request, status
from models.user import User, Verify_User
from utils.user import *
from db_utils.users import *


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

        insert_user_data(myuuid, params.username, params.email, 
                         params.firstname, params.lastname,
                         params.dob, params.gender.upper(),
                         hashed_p, salt)

        return {"message": "User created successfully"}
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.get("/verify_user")
async def verify_user(params: Verify_User):
    """ Verify user by user_id

    Args:
        user_id, code
    """
    try:
        ...
    except Exception as ex:
        return {"response": str(ex), "status_code": status.HTTP_400_BAD_REQUEST}


@router.get("/{username}")
async def read_user(username: str):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...


@router.put("/{username}")
async def update_user(username: str, request: Request):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...
    
    
@router.delete("/{username}")
async def delete_user(username: str):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...
