from fastapi import FastAPI

from routes.post import router as post_router
from routes.get_by_id import router as get_by_id_router
from routes.delete import router as delete_router
from routes.get_all import router as get_all_router
from routes.put import router as put_router

app = FastAPI()


app.include_router(post_router)
app.include_router(get_by_id_router)
app.include_router(delete_router)
app.include_router(get_all_router)
app.include_router(put_router)