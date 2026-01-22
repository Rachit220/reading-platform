from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models import Book, User
from app.books.schemas import BookCreate
from app.auth.dependencies import get_current_user
from app.cache.redis import get_cache, set_cache, invalidate

router = APIRouter()
@router.post("/")
async def add_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    db_book = Book(**book.dict(), user_id=user.id)
    db.add(db_book)
    await db.commit()

    # invalidate cache when data changes
    await invalidate(f"books:{user.id}")

    return db_book
@router.get("/")
async def list_books(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    #define cache key
    cache_key = f"books:{user.id}"

    #try cache first
    cached = await get_cache(cache_key)
    if cached:
        return cached

    #fetch from DB if cache miss
    result = await db.execute(
        select(Book).where(Book.user_id == user.id)
    )
    books = result.scalars().all()

    # convert ORM objects → JSON-serializable
    data = [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "pages": b.pages,
            "last_read": b.last_read.isoformat(),
        }
        for b in books
    ]

    #store in cache
    await set_cache(cache_key, data)

    return data
