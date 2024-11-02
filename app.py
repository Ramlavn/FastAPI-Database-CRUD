from fastapi import FastAPI
from routes.post import router as post_router
from routes.get import router as get_router
app = FastAPI()

app.include_router(post_router)
app.include_router(get_router)
