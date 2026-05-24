from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import timedelta

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, Token
from app.utils.security import hash_password, verify_password, create_access_token
from app.config import get_settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

settings = get_settings()

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email==user_data.email))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Email alread"
        )
    
    #create new user
    hashed_password = hash_password(user_data.password)
    new_user = User(
        email = user_data.email,
        hashed_password = hashed_password,
        full_name = user_data.full_name
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.post("/login", response_model=Token)
async def login(user_data:UserCreate, db:AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(User).where(User.email==user_data.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect email or password",
            headers = {"WWW=Authenticate":"Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub":user.email},
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token":access_token, "token_type":"bearer"}