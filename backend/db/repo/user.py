from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models.user import User



class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(User))
        return result.scalars().all()

    async def get_by_username(self, username: str):
        result = await self.session.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()