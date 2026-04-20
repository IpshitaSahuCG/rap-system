from pydantic import BaseModel

class UnavailableItem(BaseModel):
    item_id: int
    unavailable_since: str
    reason: str

class LocationQuery(BaseModel):
    location_id: int

class BulkUnavailableItemsRequest(BaseModel):
    items: list[UnavailableItem]

class LocationUnavailableItems(BaseModel):
    location_id: int
    unavailable_items: list[UnavailableItem]

class BulkUnavailableItemsResponse(BaseModel):
    locations: list[LocationUnavailableItems]

class ErrorResponse(BaseModel):
    error_code: int
    error_message: str
