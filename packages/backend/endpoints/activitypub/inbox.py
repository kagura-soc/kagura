from fastapi import APIRouter

router = APIRouter()

@router.post("/inbox")
async def inbox():
    pass