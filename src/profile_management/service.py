from src.authentication.dependencies import supabase  # Import the centralized Supabase client
from fastapi import HTTPException
from .schemas import PersonalizationUpdate  # Import the Pydantic schema


class PersonalizationService:
    """
    Service class to handle personalization table operations.
    """

    @staticmethod
    async def update_personalization(user_id: str, data: PersonalizationUpdate):
        """
        Update the personalization details for a user.
        
        :param user_id: The ID of the user.
        :param data: PersonalizationUpdate schema with optional fields.
        """
        try:
            # Prepare only the fields that are provided (non-None)
            update_data = data.dict(exclude_unset=True)

            if not update_data:
                raise HTTPException(status_code=400, detail="No fields provided for update.")

            # Perform the update query
            response = (
                supabase.table("personalization")
                .update(update_data)
                .eq("id", user_id)  # Match user by ID
                .execute()
            )

            # Check if the update succeeded
            if response.data is None or len(response.data) == 0:
                raise HTTPException(status_code=404, detail="User not found or update failed.")

            return {"message": "Personalization updated successfully", "data": response.data}

        except Exception as e:
            # Handle unexpected errors
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    @staticmethod
    async def get_personalization(user_id: str):
        """
        Retrieve personalization details for a specific user.
        
        :param user_id: The ID of the user.
        """
        try:
            # Query the personalization table for the given user ID
            response = (
                supabase.table("personalization")
                .select("dressing_style, body_type, skin_tone, vibe")
                .eq("id", user_id)
                .execute()
            )

            # Check if the data is found
            if response.data is None or len(response.data) == 0:
                raise HTTPException(status_code=404, detail="User personalization not found.")

            return response.data[0]

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
