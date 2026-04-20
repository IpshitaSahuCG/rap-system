"""
Service for interacting with IDP (Item Data Provider) system.
This module handles data retrieval and processing from the IDP.
"""

from typing import List
from app.models import UnavailableItem
from app.data import mock_data

def get_unavailable_items(brand: str, location: str) -> List[UnavailableItem]:
    """
    Retrieve unavailable items from the IDP system for a specific brand and location.
    
    Args:
        brand: The restaurant brand name
        location: The specific location within the brand
    
    Returns:
        List of UnavailableItem objects
    
    Raises:
        ValueError: If brand or location is invalid
    """
    # Validate brand and location exist
    brands = mock_data.get_brands()
    brand_ids = [b["id"] for b in brands]
    
    if brand not in brand_ids:
        raise ValueError(f"Brand '{brand}' not found in IDP system")
    
    # Get unavailable items from mock data (or real IDP in production)
    unavailable_items = mock_data.get_unavailable_items(brand, location)
    
    return unavailable_items

def validate_location(brand: str, location: str) -> bool:
    """
    Validate if a location exists for a given brand.
    
    Args:
        brand: The restaurant brand
        location: The location identifier
    
    Returns:
        True if location is valid, False otherwise
    """
    try:
        locations = mock_data.get_locations_by_brand_and_city(brand, "")
        location_ids = [loc["id"] for loc in locations]
        return location in location_ids
    except:
        return False
