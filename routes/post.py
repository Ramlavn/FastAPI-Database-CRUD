from fastapi import APIRouter
from pydantic import BaseModel
from db_conn import conn_db

database, collection = conn_db()

router = APIRouter()

class Post(BaseModel):
    Name: str
    Age: int
    Sex: str
    Role: str

@router.post("/api/v1/data", 
    description="Add data to the collection",
    summary="Add data"
)

def add_data(request: Post):

    new_data = collection.insert_one(request.dict())

    if new_data is not None:
        return {
            "Name": request.Name,
            "Age": request.Age,
            "Sex": request.Sex,
            "Role" : request.Role
        }
        

    else:
        return "Error in Adding data"
