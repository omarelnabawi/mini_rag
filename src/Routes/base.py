from fastapi import APIRouter, FastAPI,Depends
from helpers.config import get_settings,Settings
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
async def welcome(app_settings:Settings = Depends(get_settings)):
    #settings=get_settings()
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version
            }
