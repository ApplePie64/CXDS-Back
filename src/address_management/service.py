from .dependencies import supabase

async def get_addresses_for_user(user_id: str):
    """
    Fetch addresses from the database for a given user ID.
    """
    response = supabase.table("address").select("*").eq("id", user_id).execute()
    if response.error:
        return None
    return response.data
