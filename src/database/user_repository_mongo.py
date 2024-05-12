from typing import AsyncGenerator, Any, Callable

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorClient

from src.core.schemas import UserDTO
from src.database.db_helper_mongo import db_helper


class UserRepositoryMongo:
    database_name: str = 'database'
    collection_name: str = 'users'

    @classmethod
    async def add_user(
            cls,
            new_user: UserDTO,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> None:
        collection = client[cls.database_name][cls.collection_name]
        await collection.insert_one(new_user.__dict__)

    @classmethod
    async def select_user(
            cls,
            user_id: int,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> UserDTO | None:
        collection = client[cls.database_name][cls.collection_name]
        result = await collection.find_one({'_id': user_id})
        if not result:
            return
        user = UserDTO(**result)
        return user

    @classmethod
    async def count_users(
            cls,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> int:
        collection = client[cls.database_name][cls.collection_name]
        result = await collection.count_documents({})
        return result

    @classmethod
    async def del_user(
            cls,
            user_id: int,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> None:
        collection = client[cls.database_name][cls.collection_name]
        await collection.delete_one({'_id': user_id})
