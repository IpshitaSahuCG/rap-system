from pydantic import BaseModel
from typing import List, Optional

class Brand(BaseModel):
    """Schema for restaurant brand."""
    id: str
    name: str

class City(BaseModel):
    """Schema for city."""
    id: str
    name: str

class Location(BaseModel):
    """Schema for restaurant location."""
    id: str
    name: str
    city: str
    brand: str

class UnavailableItemSchema(BaseModel):
    """Schema for unavailable item."""
    item_id: str
    item_name: str
    category: str
    reason_unavailable: Optional[str] = None
