from fastapi import APIRouter
from db_conn import conn_db
from bson import ObjectId

database, collection = conn_db()


router = APIRouter()



@router.delete("/api/v1/data/{id}", 
    description="Delete data from collection",
    summary="Delete data"
)

def delete(id: str):

    object_id = ObjectId(id)
    retrieved = collection.find_one({"_id":object_id})

    if retrieved is not None:

        delete = collection.delete_one({"_id":object_id})
        return {"Message":"Deleted successfully", "Deleted_Id":str(retrieved["_id"])}

    else:
        return {"Message":"Delete not successfull"}
