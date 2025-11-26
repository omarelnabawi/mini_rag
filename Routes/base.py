from fastapi import APIRouter, FastAPI
import os
#app=FastAPI()
base_router = APIRouter(
    prefix="/api/v1",
    tags=["LLM Base Routes",""],
)

@base_router.get("/")
def welcome():
    return {
        "message": "The Mini RAG Default is running!"
            }

@base_router.get("/welcome")
async def welcome():
    app_name=os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version
            }
