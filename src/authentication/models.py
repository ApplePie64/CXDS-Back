from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base
import enum


class IdentityEnum(enum.Enum):
    male = "male"
    female = "female"


class User(Base):
    """
    SQLAlchemy model for the `users` table.
    This table extends the Supabase `auth.users` table with additional fields.
    """
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)  # References auth.users.id
    name = Column(String, nullable=False)
    identity = Column(Enum(IdentityEnum), nullable=False)
    vibe = Column(String, nullable=True)
    wishlist = Column(String, nullable=True)  # Stores comma-separated product IDs

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, identity={self.identity})>"
