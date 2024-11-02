from fastapi import APIRouter
from pydantic import BaseModel
from db_conn import conn_db

router = APIRouter()


database, collection = conn_db()

class Post(BaseModel):
    Age: int

@router.post("/post")

def create_post(request:Post):
    inserted = collection.insert_one(request.dict())
    return{"id": str(inserted.inserted_id),
           "Age": request.Age
}