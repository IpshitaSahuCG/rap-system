"""
Mock data for testing and development.
Replace this with real IDP integration in production.
"""

from typing import List, Dict, Any

# Mock brands data
BRANDS = [
    {"id": "mcdonalds", "name": "McDonald's"},
    {"id": "burger_king", "name": "Burger King"},
    {"id": "subway", "name": "Subway"},
    {"id": "kfc", "name": "KFC"},
    {"id": "taco_bell", "name": "Taco Bell"}
]

# Mock cities data
CITIES = {
    "mcdonalds": [
        {"id": "chicago", "name": "Chicago"},
        {"id": "los_angeles", "name": "Los Angeles"},
        {"id": "new_york", "name": "New York"}
    ],
    "burger_king": [
        {"id": "chicago", "name": "Chicago"},
        {"id": "miami", "name": "Miami"},
        {"id": "new_york", "name": "New York"}
    ],
    "subway": [
        {"id": "chicago", "name": "Chicago"},
        {"id": "denver", "name": "Denver"},
        {"id": "austin", "name": "Austin"}
    ],
    "kfc": [
        {"id": "dallas", "name": "Dallas"},
        {"id": "houston", "name": "Houston"},
        {"id": "chicago", "name": "Chicago"}
    ],
    "taco_bell": [
        {"id": "los_angeles", "name": "Los Angeles"},
        {"id": "phoenix", "name": "Phoenix"},
        {"id": "denver", "name": "Denver"}
    ]
}

# Mock locations data
LOCATIONS = {
    "mcdonalds": {
        "chicago": [
            {"id": "mcd_chicago_downtown", "name": "Downtown Chicago"},
            {"id": "mcd_chicago_northside", "name": "North Side Chicago"},
            {"id": "mcd_chicago_southside", "name": "South Side Chicago"}
        ],
        "los_angeles": [
            {"id": "mcd_la_downtown", "name": "Downtown LA"},
            {"id": "mcd_la_hollywood", "name": "Hollywood"}
        ],
        "new_york": [
            {"id": "mcd_ny_manhattan", "name": "Manhattan"},
            {"id": "mcd_ny_brooklyn", "name": "Brooklyn"}
        ]
    },
    "burger_king": {
        "chicago": [
            {"id": "bk_chicago_downtown", "name": "Downtown Chicago"},
            {"id": "bk_chicago_oconnor", "name": "O'Connor Plaza"}
        ],
        "miami": [
            {"id": "bk_miami_downtown", "name": "Downtown Miami"},
            {"id": "bk_miami_beach", "name": "Miami Beach"}
        ],
        "new_york": [
            {"id": "bk_ny_manhattan", "name": "Manhattan"}
        ]
    },
    "subway": {
        "chicago": [
            {"id": "sw_chicago_downtown", "name": "Downtown Chicago"},
            {"id": "sw_chicago_loop", "name": "The Loop"}
        ],
        "denver": [
            {"id": "sw_denver_downtown", "name": "Downtown Denver"},
            {"id": "sw_denver_cherry", "name": "Cherry Creek"}
        ],
        "austin": [
            {"id": "sw_austin_downtown", "name": "Downtown Austin"}
        ]
    },
    "kfc": {
        "dallas": [
            {"id": "kfc_dallas_downtown", "name": "Downtown Dallas"},
            {"id": "kfc_dallas_uptown", "name": "Uptown Dallas"}
        ],
        "houston": [
            {"id": "kfc_houston_downtown", "name": "Downtown Houston"}
        ],
        "chicago": [
            {"id": "kfc_chicago_downtown", "name": "Downtown Chicago"}
        ]
    },
    "taco_bell": {
        "los_angeles": [
            {"id": "tb_la_downtown", "name": "Downtown LA"},
            {"id": "tb_la_hollywood", "name": "Hollywood"}
        ],
        "phoenix": [
            {"id": "tb_phoenix_downtown", "name": "Downtown Phoenix"}
        ],
        "denver": [
            {"id": "tb_denver_downtown", "name": "Downtown Denver"}
        ]
    }
}

# Mock unavailable items data
UNAVAILABLE_ITEMS = {
    "mcd_chicago_downtown": [
        {"item_id": "001", "item_name": "Big Mac", "category": "Burgers", "reason_unavailable": "Out of stock"},
        {"item_id": "002", "item_name": "Quarter Pounder", "category": "Burgers", "reason_unavailable": "Equipment malfunction"},
        {"item_id": "003", "item_name": "Chicken McNuggets 20pc", "category": "Chicken", "reason_unavailable": "Delivery delayed"}
    ],
    "mcd_chicago_northside": [
        {"item_id": "002", "item_name": "Quarter Pounder", "category": "Burgers", "reason_unavailable": "Out of stock"},
        {"item_id": "008", "item_name": "Filet-O-Fish", "category": "Fish", "reason_unavailable": "Supplier issue"}
    ],
    "bk_chicago_downtown": [
        {"item_id": "101", "item_name": "Whopper", "category": "Burgers", "reason_unavailable": "Equipment maintenance"},
        {"item_id": "102", "item_name": "Crispy Chicken Sandwich", "category": "Chicken", "reason_unavailable": "Out of stock"}
    ],
    "sw_denver_downtown": [
        {"item_id": "201", "item_name": "Italian BMT", "category": "Sandwiches", "reason_unavailable": "Ingredient shortage"},
        {"item_id": "202", "item_name": "Meatball Marinara", "category": "Sandwiches", "reason_unavailable": "Supplier delay"}
    ],
    "kfc_dallas_downtown": [
        {"item_id": "301", "item_name": "12pc Bucket", "category": "Chicken", "reason_unavailable": "Out of stock"},
        {"item_id": "302", "item_name": "Popcorn Chicken", "category": "Chicken", "reason_unavailable": "Equipment issue"}
    ],
    "tb_la_downtown": [
        {"item_id": "401", "item_name": "Crunchwrap Supreme", "category": "Wraps", "reason_unavailable": "Out of stock"},
        {"item_id": "402", "item_name": "Cheesy Bean and Rice Burrito", "category": "Burritos", "reason_unavailable": "Ingredient shortage"}
    ]
}

def get_brands() -> List[Dict[str, Any]]:
    """Get all available brands."""
    return BRANDS

def get_cities_by_brand(brand: str) -> List[Dict[str, Any]]:
    """Get cities for a specific brand."""
    return CITIES.get(brand, [])

def get_locations_by_brand_and_city(brand: str, city: str) -> List[Dict[str, Any]]:
    """Get locations for a specific brand and city."""
    brand_locations = LOCATIONS.get(brand, {})
    if city:
        return brand_locations.get(city, [])
    # Return all locations for the brand if city is not specified
    all_locations = []
    for locations in brand_locations.values():
        all_locations.extend(locations)
    return all_locations

def get_unavailable_items(brand: str, location: str) -> List[Dict[str, Any]]:
    """Get unavailable items for a specific location."""
    return UNAVAILABLE_ITEMS.get(location, [])
