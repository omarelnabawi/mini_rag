from fastapi import APIRouter, FastAPI
#app=FastAPI()
base_router = APIRouter()

@base_router.get("/")
def welcome():
    return {
        "message": "The Mini RAG Default is running!"
            }

@base_router.get("/welcome")
def welcome():
    return {
        "message": "Welcome to the Mini RAG !"
            }

@base_router.get("/hello")
def welcome():
    return {
        "message": "hello from base router!"
            }