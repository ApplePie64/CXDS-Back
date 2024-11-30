from fastapi import APIRouter, HTTPException, Query
from .schemas import AddressCreate
from .dependencies import supabase  # Import the supabase client from dependencies

router = APIRouter()

@router.get("/")
async def get_addresses(user_id: str = Query(..., description="User ID to fetch addresses for")):
    """
    Fetch all addresses for a specific user by user_id.
    """
    try:
        # Query the address table using the user_id (foreign key reference)
        response = supabase.table("address").select("*").eq("id", user_id).execute()

        # Check if the response data is not empty
        if response.data is None or len(response.data) == 0:
            raise HTTPException(status_code=404, detail="No addresses found for this user.")
        
        # Return the list of addresses
        return response.data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/", response_model=dict)
async def create_address(
    address: AddressCreate,  # Address schema
    user_id: str  # Accepting user_id manually for testing
):
    # Insert the new address into the address table in Supabase
    response = supabase.table("address").insert({
        "id": user_id,  # Manually passed user_id
        "address1": address.address1,
        "address2": address.address2,
        "address3": address.address3,
        "city": address.city,
        "state": address.state,
        "country": address.country,
        "pin": address.pin
    }).execute()

    # Check if the insertion was successful
    if response.data is None or len(response.data) == 0:
            raise HTTPException(status_code=404, detail="error.")

    return {"address_id": response.data[0]["address_id"], "message": "Address successfully created"}

@router.get("/{address_id}")
async def get_address(address_id: str):
    # Retrieve the address details from Supabase
    address_data = supabase.table("address").select("*").eq("address_id", address_id).execute()

    # Check if the address was found
    if not address_data.data:
        raise HTTPException(status_code=404, detail="Address not found")

    # Return the address details
    return {"data": address_data.data[0]}

@router.put("/")
async def update_address(address_id: str, address: AddressCreate):
    # Step 1: Retrieve the existing address data from Supabase by address_id
    existing_address = supabase.table("address").select("*").eq("address_id", address_id).execute()

    if not existing_address.data:
        raise HTTPException(status_code=404, detail="Address not found")

    # Step 2: Update the address with the new data from the request body
    updated_address = supabase.table("address").update({
        "address1": address.address1,
        "address2": address.address2,
        "address3": address.address3,
        "city": address.city,
        "state": address.state,
        "country": address.country,
        "pin": address.pin
    }).eq("address_id", address_id).execute()

    # Check if the update was successful
    if not updated_address.data:
        raise HTTPException(status_code=400, detail="Failed to update the address")

    # Return the updated address details
    return {"message": "Address updated successfully", "data": updated_address.data[0]}

@router.delete("/")
async def delete_address(address_id: str):
    # Check if the address exists
    response = supabase.table("address").select("*").eq("address_id", address_id).execute()
    
    # If no address is found, raise an exception
    if len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Address not found")

    # Delete the address
    delete_response = supabase.table("address").delete().eq("address_id", address_id).execute()

    # If the delete response is successful, return a success message
    if not delete_response.data:
        raise HTTPException(status_code=500, detail="Failed to delete address")
    else:
        return {"message": "Address deleted successfully"}
       