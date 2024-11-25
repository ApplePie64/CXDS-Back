from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum
from uuid import UUID


class IdentityEnum(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseModel):
    """
    Base user schema for shared fields.
    """
    username: str
    name: str
    identity: IdentityEnum
    vibe: Optional[str] = None


class UserCreate(BaseModel):
    """
    Schema for user registration. This includes authentication fields
    and additional user details to be saved in the database.
    """
    email: EmailStr
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long.")
    username: str
    name: str
    identity: IdentityEnum
    vibe: Optional[str] = None


class UserUpdate(BaseModel):
    """
    Schema for updating user details. All fields are optional.
    """
    name: Optional[str] = None
    username: Optional[str] = None
    identity: Optional[IdentityEnum] = None
    vibe: Optional[str] = None


class UserInDB(UserBase):
    """
    Schema for returning user data from the database.
    Includes the user's UUID as the primary identifier.
    """
    id: UUID

    class Config:
        orm_mode = True
