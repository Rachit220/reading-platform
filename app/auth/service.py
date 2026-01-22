from sqlalchemy.future import select
from app.db.models import User
from app.core.security import verify_password

async def authenticate_user(db, email, password):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.password):
        return None
    return user
