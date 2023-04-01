from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUD
from app.models.users import User as m_User


class DBUsers(CRUD):
    @staticmethod
    async def create(db: AsyncSession, user: m_User) -> m_User:
        db.add(user)
        await db.flush()
        await db.commit()
        return user
