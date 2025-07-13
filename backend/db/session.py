from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import config
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from db.repo.requests import RequestsRepo

engine = create_async_engine(config.DATABASE_URL, future=True, echo=False)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_repo(session: AsyncSession = Depends(get_db)) -> RequestsRepo:
    return RequestsRepo(session)