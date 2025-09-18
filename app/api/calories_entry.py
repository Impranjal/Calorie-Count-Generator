from fastapi import FastAPI ,APIRouter

router = APIRouter(
    prefix="/calorie",
    tags=["calorie"]
)

@router.get('/get_calorie')
async def get_calorie():
    pass