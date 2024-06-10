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


@router.get("/")
async def read_users(request: Request):
    return JSONResponse({"response": "Welcome to Tehelka App"})


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
