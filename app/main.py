from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.books.router import router as books_router
from app.stats.router import router as stats_router

app = FastAPI(title="Reading Platform")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])

@app.get("/")
async def health():
    return {"status": "ok"}
