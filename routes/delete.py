from fastapi import APIRouter
from bson import ObjectId
from db_conn import conn_db

router = APIRouter()


database, collection = conn_db() 


@router.delete("/delete/{id}")
def delete(id: str):
    object_id = ObjectId(id)

    document = collection.find_one({'_id': object_id})

    if document is not None:
        collection.delete_one({'_id': object_id})
        return {"message": "Document deleted successfully"}
    else:
        return {"message": "Document not found"}