"""
User Routes
-----------

- CREATE user
- READ user
- UPDATE user
- DELETE user
- CREATE user_profile
- READ user_profile
- UPDATE user_profile
- DELETE user_profile
"""

from fastapi import APIRouter, Request
# from ..models import User

router = APIRouter()


@router.get("/users/")
async def read_users(request: Request):
    """ Read all users
    """
    ...


@router.get("/users/{username}")
async def read_user(username: str):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...


@router.put("/users/{username}")
async def update_user(username: str, request: Request):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...
    
    
@router.delete("/users/{username}")
async def delete_user(username: str):
    """ Read user by username

    Args:
        username (uuid): User ID
    """
    ...
