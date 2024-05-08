from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import select

from src.core.models import User
from src.database.db_helper import db_helper

session_factory: async_sessionmaker = db_helper.get_session_factory()


class UserRepository:
    @staticmethod
    async def add_user(
            new_user: User,
    ) -> None:
        async with session_factory() as session:
            session.add(new_user)
            await session.flush()
            await session.refresh(new_user)
            await session.commit()
    
    @staticmethod
    async def select_user(
            user_id: int,
    ) -> User | None:
        async with session_factory() as session:
            stmt = select(User).filter_by(id=user_id)
            res = await session.execute(stmt)
            user = res.scalars().one_or_none()
        return user
    
    @staticmethod
    async def count_users(
    ) -> int:
        async with session_factory() as session:
            stmt = select(User)
            res = await session.execute(stmt)
            users = res.scalars().all()
        return len(users)
    
    @staticmethod
    async def del_user(
            user: User,
    ) -> None:
        async with session_factory() as session:
            await session.delete(user)
            await session.flush()
            await session.commit()
