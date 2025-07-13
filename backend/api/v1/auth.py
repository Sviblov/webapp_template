from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta, timezone
from jose import jwt
from db.repo.requests import RequestsRepo
from db.session import get_repo
from core.config import config
from schemas.user import UserLogin
from core.security import verify_password
import logging

router = APIRouter()

@router.post("/login", summary="User Login", response_model=dict)
async def login(
    login_data: UserLogin,
    repo: RequestsRepo = Depends(get_repo)
):
    
    user = await repo.users.get_by_username(login_data.username)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": user.username, "exp": expire}
    token = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}