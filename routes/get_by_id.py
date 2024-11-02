from fastapi import APIRouter
from bson import ObjectId
from db_conn import conn_db

database, collection = conn_db()

router = APIRouter()


@router.get("/get/{id}")
def get(id: str):


    clean_id = id.strip('{}') # for post man 


    object_id = ObjectId(clean_id)  # Convert the string ID to ObjectId
    document = collection.find_one({'_id': object_id})  

# converting from BSON to JSONs
    if document is not None:
        document["_id"] = str(document["_id"])
        return document
    else:
        return {"message": "Document not found"}

