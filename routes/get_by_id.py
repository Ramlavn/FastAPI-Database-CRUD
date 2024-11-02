from fastapi import APIRouter
from db_conn import conn_db
from bson import ObjectId

database, collection = conn_db()

router = APIRouter()


@router.get("/api/v1/data/{id}", 
    description="Retrieve a specific document by its unique identifier (ID).",
    status_code=200,
    summary="Get data by ID",
    responses={
        200: {"description": "Successfully retrieved the data."},
        400: {"description": "Invalid ID format."},
        404: {"description": "data not found."},
        500: {"description": "Server error while retrieving the data."}
    }
)

def get(id):

    object_id = ObjectId(id)
    created_doc = collection.find_one({'_id':object_id})

    if created_doc is not None:
        created_doc["_id"] = f"ObjectId('{str(created_doc["_id"])}')"
        return created_doc

    else:
        return "error"
