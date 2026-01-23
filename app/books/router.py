from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_db
from app.db.models import Book, User
from app.books.schemas import BookCreate
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post("/", status_code=201)
async def add_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    db_book = Book(
        title=book.title,
        author=book.author,
        pages=book.pages,
        user_id=user.id,
    )
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)

    return {
        "id": db_book.id,
        "title": db_book.title,
        "author": db_book.author,
        "pages": db_book.pages,
    }


@router.get("/")
async def list_books(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Book).where(Book.user_id == user.id)
    )
    books = result.scalars().all()

    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "pages": b.pages,
        }
        for b in books
    ]
