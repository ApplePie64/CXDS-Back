from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer
import jwt
import os

# Initialize the HTTPBearer authentication scheme
security = HTTPBearer()

# Load the JWT secret from the environment variables
JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

def get_current_user(token: str = Security(security)):
    """
    Validate the JWT token and return the user ID (sub field).
    This is used to authenticate the current user.
    """
    try:
        # Decode the JWT token
        payload = jwt.decode(token.credentials, JWT_SECRET, algorithms=["HS256"])
        return payload.get("sub")  # Return the user ID (Supabase UID)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
