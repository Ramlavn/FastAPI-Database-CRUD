from fastapi import APIRouter
from db_conn import conn_db
from bson import ObjectId


database, collection = conn_db()

router = APIRouter()

@router.get("/api/v1/data", 
    description="Retrieve all data.",
    status_code=200,
    summary="Get all data",
    responses={
        200: {"description": "Successfully retrieved the data."},
        400: {"description": "Invalid ID format."},
        404: {"description": "data not found."},
        500: {"description": "Server error while retrieving the data."}
    }
)
def get_all():
    all_data = list(collection.find())
    for doc in all_data:
        doc["_id"] = f"ObjectId('{str(doc["_id"])}')"
    total_data = len(all_data)
    return {"Dcuments": total_data, "Records": all_data}