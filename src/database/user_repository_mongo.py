from motor.motor_asyncio import AsyncIOMotorClientSession

from src.core.schemas import UserDTO
from src.database.db_helper_mongo import db_helper


class UserRepositoryMongo:
    @staticmethod
    async def add_user(
            new_user: UserDTO,
            session: AsyncIOMotorClientSession = db_helper.get_session(),
    ) -> None:
        async with session.start_transaction():
            client = session.client
            users_collection = client['database']['users']
            await users_collection.insert_one(new_user.__dict__)

    @staticmethod
    async def select_user(
            user_id: int,
            session: AsyncIOMotorClientSession = db_helper.get_session(),
    ) -> UserDTO | None:
        async with session.start_transaction():
            client = session.client
            users_collection = client['database']['users']
            result = await users_collection.find_one({'_id': user_id})
            user = UserDTO(**result)
            return user

    @staticmethod
    async def count_users(
            session: AsyncIOMotorClientSession = db_helper.get_session(),
    ) -> int:
        async with session.start_transaction():
            client = session.client
            users_collection = client['database']['users']
            result = await users_collection.count_documents({})
        return result

    @staticmethod
    async def del_user(
            user_id: int,
            session: AsyncIOMotorClientSession = db_helper.get_session(),
    ) -> None:
        async with session.start_transaction():
            client = session.client
            users_collection = client['database']['users']
            await users_collection.delete_one({'_id': {user_id}})
