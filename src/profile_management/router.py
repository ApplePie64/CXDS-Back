from fastapi import APIRouter, HTTPException, Query
from src.authentication.dependencies import supabase  # Import the supabase client from dependencies
from .schemas import PersonalizationUpdate
from .service import PersonalizationService


router = APIRouter()

@router.get("/")
async def get_user_details(user_id: str = Query(..., description="User ID to fetch details for")):
    """
    Fetch the username and join date for a user from the database.
    """
    try:
        # Select only 'username' and 'join_date' fields, could change to retrieve more( depends on frontend )
        response = supabase.table("users").select("name, join_date").eq("id", user_id).execute()

        # Check if the response data is not empty
        if response.data is None or len(response.data) == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Return the user data
        return response.data[0]  # Return the details
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    
@router.post("/change-password")
async def change_password(email: str, new_password: str):
    """
    Handle password updates for a Supabase user.
    """
    try:
        # Step 1: we should change this to ensure the actual use is changing the password

        # Step 2: Update the password
        auth_response = supabase.auth.update_user(
            {
                "email": email,
                "password": new_password,
            }
        )

        if not auth_response.user:
            raise HTTPException(status_code=500, detail="Failed to update the password.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error changing password: {str(e)}")

    return {"message": "Password updated successfully."}

@router.put("/personalization")
async def update_personalization(
    user_id: str, #temporary till frontend exists 
    personalization_data: PersonalizationUpdate
):
    """
    Endpoint to update personalization details.
    """
    return await PersonalizationService.update_personalization(
        user_id, personalization_data
    )