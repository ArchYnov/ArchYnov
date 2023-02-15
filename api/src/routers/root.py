from fastapi import APIRouter, Depends, Response, status

router = APIRouter(prefix="", tags=["root"])

@router.get("/")
async def get_root():
    return {"message": "Hello World"}