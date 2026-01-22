from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models import User
from app.core.security import hash_password, create_access_token
from app.auth.service import authenticate_user

router = APIRouter()


@router.post("/register", status_code=201)
async def register(
    email: str,
    password: str,
    db: AsyncSession = Depends(get_db),
):
    user = User(email=email, password=hash_password(password))
    db.add(user)
    await db.commit()
    return {"message": "User registered successfully"}


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    user = await authenticate_user(
        db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
