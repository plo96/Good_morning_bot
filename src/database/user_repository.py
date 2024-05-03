from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from src.core.models import User


class UserRepository:

	@staticmethod
	async def add_user(
			session: AsyncSession,
			new_user: dict,
	) -> User:
		new_user = User(**new_user)
		session.add(new_user)
		await session.flush()
		await new_user.refresh()
		return new_user
	
	@staticmethod
	async def select_user(
			session: AsyncSession,
			user_id: UUID,
	) -> User:
		...
	
	@staticmethod
	async def del_user(
			session: AsyncSession,
			user: User,
	) -> None:
		...
	