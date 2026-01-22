from app.db.models import Book

async def create_book(db, user_id, data):
    book = Book(**data.dict(), user_id=user_id)
    db.add(book)
    await db.commit()
    return book
