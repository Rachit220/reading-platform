from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def stats():
    return {
        "total_books": 0,
        "completed": 0,
        "streak": 0,
        "avg_pages_per_day": 0,
        "top_author": None
    }
