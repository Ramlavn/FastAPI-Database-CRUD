from fastapi import APIRouter
from pydantic import BaseModel
from db_conn  import conn_db
from bson import ObjectId


database, collection = conn_db()

router = APIRouter()

class Put(BaseModel):
    Name: str
    Age: int
    Sex: str
    Occupation: str

@router.put("/api/v1/data", 
    description="Edit data in the collection",
    summary="Edit data"
)

def update(request:Put, id: str):
    object_id = ObjectId(id)

    retrieve = collection.find_one({"_id":object_id})

    if retrieve:

        corrected = collection.update_one(
            {"_id" : object_id},
            {"$set" : request.dict()}
        )
        
        return "Document updated successfully"
    else:
        return "Document not updated successfully"