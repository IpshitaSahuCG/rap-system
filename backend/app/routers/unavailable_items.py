from fastapi import APIRouter, HTTPException
from typing import List
from app.models import (
    BulkUnavailableItemsRequest,
    BulkUnavailableItemsResponse,
    LocationUnavailableItems,
    ErrorResponse
)
from app.services import idp_service
from app.data import mock_data

router = APIRouter(prefix="/api", tags=["unavailable-items"])

@router.get("/brands")
async def get_brands():
    """Get all available restaurant brands."""
    try:
        brands = mock_data.get_brands()
        return {
            "status": "success",
            "data": brands
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/cities/{brand}")
async def get_cities(brand: str):
    """Get cities for a specific brand."""
    try:
        cities = mock_data.get_cities_by_brand(brand)
        if not cities:
            raise HTTPException(
                status_code=404,
                detail=f"Brand '{brand}' not found"
            )
        return {
            "status": "success",
            "data": cities
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/locations/{brand}/{city}")
async def get_locations(brand: str, city: str):
    """Get locations for a specific brand and city."""
    try:
        locations = mock_data.get_locations_by_brand_and_city(brand, city)
        if not locations:
            raise HTTPException(
                status_code=404,
                detail=f"No locations found for brand '{brand}' in city '{city}'"
            )
        return {
            "status": "success",
            "data": locations
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/unavailable-items")
async def get_unavailable_items(request: BulkUnavailableItemsRequest) -> BulkUnavailableItemsResponse:
    """
    Get unavailable items for multiple locations.
    
    This endpoint supports bulk queries for unavailable items across multiple
    restaurant locations. It accepts a list of brand-location pairs and returns
    the unavailable items for each location.
    """
    try:
        if not request.queries:
            raise HTTPException(
                status_code=400,
                detail="At least one query must be provided"
            )
        
        # Limit to 100 queries per request for performance
        if len(request.queries) > 100:
            raise HTTPException(
                status_code=400,
                detail="Maximum 100 queries allowed per request"
            )
        
        # Fetch unavailable items for each query
        results = []
        for query in request.queries:
            unavailable_items = idp_service.get_unavailable_items(
                brand=query.brand,
                location=query.location
            )
            
            results.append(
                LocationUnavailableItems(
                    brand=query.brand,
                    location=query.location,
                    unavailable_items=unavailable_items
                )
            )
        
        return BulkUnavailableItemsResponse(
            status="success",
            data=results
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@router.get("/unavailable-items/{brand}/{location}")
async def get_unavailable_items_single(brand: str, location: str):
    """Get unavailable items for a single location."""
    try:
        unavailable_items = idp_service.get_unavailable_items(
            brand=brand,
            location=location
        )
        
        return {
            "status": "success",
            "data": {
                "brand": brand,
                "location": location,
                "unavailable_items": unavailable_items
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
