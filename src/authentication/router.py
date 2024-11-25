from fastapi import APIRouter, HTTPException, Depends
from .schemas import UserCreate, UserInDB, UserUpdate
from .dependencies import supabase
from .service import create_user, get_user_by_id, update_user, delete_user
import httpx
import os

router = APIRouter()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

@router.post("/register")
async def register_user(user_data: UserCreate):
    """
    Handle user registration by creating a Supabase user
    and inserting additional details into the users table.
    """
    # Validate `identity`
    if user_data.identity not in ["male", "female"]:
        raise HTTPException(status_code=400, detail="Invalid identity value. Must be 'male' or 'female'.")

    # Step 1: Create the user in Supabase Authentication
    try:
        auth_response = supabase.auth.sign_up(
            {
                "email": user_data.email,
                "password": user_data.password,
            }
        )
        supabase_user = auth_response.user  # Extract the User object

        # Ensure the user object exists
        if not supabase_user:
            raise HTTPException(status_code=500, detail="Failed to create Supabase user.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating Supabase user: {str(e)}")

    # Extract user ID from the created Supabase user
    user_id = supabase_user.id

    # Step 2: Insert additional user details into the users table
    try:
        create_user(user_data, user_id)
    except Exception as e:
        # Rollback the Supabase Auth user creation if insertion fails
        await delete_supabase_user(user_id)
        raise HTTPException(status_code=500, detail=f"Error saving user details: {str(e)}")

    return {
        "message": "User registered successfully.",
        "user": {
            "id": user_id,
            "email": user_data.email,
            "username": user_data.username,
            "name": user_data.name,
            "identity": user_data.identity,
            "vibe": user_data.vibe,
        },
    }

async def delete_supabase_user(user_id: str):
    """
    Delete a user from Supabase using the Admin API.
    """
    headers = {
        "Authorization": f"Bearer {SERVICE_ROLE_KEY}",
        "apikey": SERVICE_ROLE_KEY,
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{SUPABASE_URL}/auth/v1/admin/users/{user_id}", headers=headers)
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to delete Supabase user: {response.text}",
            )
            
@router.get("/{user_id}", response_model=UserInDB)
def get_user(user_id: str):
    """
    Get user by Supabase ID.
    """
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserInDB)
def update_user_details(user_id: str, user: UserUpdate):
    """
    Update user details.
    """
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return updated_user[0]


@router.delete("/{user_id}")
def delete_user_account(user_id: str):
    """
    Delete user by Supabase ID.
    """
    result = delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found or deletion failed")
    return {"message": "User deleted successfully"}
