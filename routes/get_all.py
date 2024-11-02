from fastapi import APIRouter, Query
from db_conn import conn_db
from bson import ObjectId
from typing import Optional

# Establish database connection
database, collection = conn_db()
router = APIRouter()

@router.get(
    "/api/v1/data", 
    description="Retrieve all data.",
    status_code=200,
    summary="Get all data",
    responses={
        200: {"description": "Successfully retrieved the data."},
        400: {"description": "Invalid ID format."},
        404: {"description": "Data not found."},
        500: {"description": "Server error while retrieving the data."}
    }
)
def get_all(role: Optional[str] = Query(None, description="Filter by role")):
    # Filter query based on role, if provided
    filter_query = {}
    if role:
        filter_query["Role"] = role

    # Fetch data with optional filtering
    all_data = list(collection.find(filter_query))
    for doc in all_data:
        doc["_id"] = f"ObjectId('{str(doc["_id"])}')"  # Convert ObjectId to string
    total_data = len(all_data)
    return {"Documents": total_data, "Records": all_data}
