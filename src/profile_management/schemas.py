# Pydantic schemas for profile_management
from pydantic import BaseModel
from typing import Optional
from enum import Enum

# Enums
class DressingStyle(str, Enum):
    masculine = "Masculine"
    feminine = "Feminine"

class BodyType(str, Enum):
    rectangle = "Rectangle"
    triangle = "Triangle"
    oval = "Oval"
    trapezoid = "Trapezoid"
    hourglass = "Hourglass"
    pear = "Pear"
    inverted_triangle = "Inverted Triangle"
    plus = "Plus"

class SkinTone(str, Enum):
    fair = "Fair"
    medium = "Medium"
    tanned = "Tanned"
    dark = "Dark"

class Vibe(str, Enum):
    cheerful = "Cheerful"
    casual = "Casual"
    western = "Western"
    indian = "Indian"
    fusion = "Fusion"

# Update Schema
class PersonalizationUpdate(BaseModel):
    dressing_style: Optional[DressingStyle] = None
    body_type: Optional[BodyType] = None
    skin_tone: Optional[SkinTone] = None
    vibe: Optional[Vibe] = None
