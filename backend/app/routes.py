from fastapi import APIRouter
from .hello import say_hello

router = APIRouter()

@router.get("/")
def get_hello():
    return {"message": say_hello()}