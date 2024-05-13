from fastapi import APIRouter
from app.services import ai_service

router = APIRouter()

@router.get("/test/")
async def test():
    return {"message": "Hello from the backend!"}

@router.post("/get-answer/")
async def get_answer(question: str):
    return await ai_service.generate_answer(question)