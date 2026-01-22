from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from collections import Counter
from datetime import datetime, timedelta
from app.db.models import Book

async def compute_stats(db: AsyncSession, user_id: int):
    result = await db.execute(select(Book).where(Book.user_id == user_id))
    books = result.scalars().all()

    total = len(books)
    completed = sum(1 for b in books if b.pages >= 300)

    authors = Counter(b.author for b in books)
    top_author = authors.most_common(1)[0][0] if authors else None

    streak = sum(
        1 for b in books
        if b.last_read >= datetime.utcnow() - timedelta(days=7)
    )

    avg_pages = sum(b.pages for b in books) // max(total, 1)

    return {
        "total_books": total,
        "completed": completed,
        "streak": streak,
        "avg_pages_per_day": avg_pages,
        "top_author": top_author,
    }
