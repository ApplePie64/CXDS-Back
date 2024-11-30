from pydantic import BaseModel
from typing import Optional

class AddressOut(BaseModel):
    address_id: str
    address1: str
    address2: Optional[str]
    address3: Optional[str]
    city: str
    state: str
    country: str
    pin: str

    class Config:
        orm_mode = True

class AddressCreate(BaseModel):
    address1: str
    address2: str = None  # Optional field
    address3: str = None  # Optional field
    city: str
    state: str
    country: str
    pin: str
