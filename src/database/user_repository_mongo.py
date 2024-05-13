"""
	Класс для реализации способов взаимодействия с БД для сущности пользователей.
"""

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorClient

from src.core.schemas import UserDTO
from src.database.db_helper_mongo import db_helper


class UserRepositoryMongo:
    """Репозиторий на основе mongodb для сущностей пользователей."""
    database_name: str = 'database'
    collection_name: str = 'users'

    @classmethod
    async def add_user(
            cls,
            new_user: UserDTO,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> None:
        """
        Добавление одного пользователя.
        :param new_user: Новый пользователь класса UserDTO для добавления в БД.
        :param client: Асинхронный клиент для доступа к БД.
        :return: None
        """
        collection = client[cls.database_name][cls.collection_name]
        await collection.insert_one(new_user.to_serialised_mongo_dict())

    @classmethod
    async def update_user(
            cls,
            user_id: int,
            client: AsyncIOMotorClient = db_helper.get_client(),
            **kwargs,
    ) -> None:
        """
        Изменение параметров пользователя, записанного в базе данных под определённым id.
        :param user_id: Параметр '_id' изменяемого пользователя.
        :param client: Асинхронный клиент для доступа к БД.
        :param kwargs: Перечисление изменяемых параметров и их новых значений.
        :return: None
        """
        collection = client[cls.database_name][cls.collection_name]
        await collection.update_one({'_id': user_id}, kwargs)

    @classmethod
    async def select_user(
            cls,
            user_id: int,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> UserDTO | None:
        """
        Выгрузка данных конкретного пользователя из базы.
        :param user_id: Параметр '_id' нужного пользователя.
        :param client: Асинхронный клиент для доступа к БД.
        :return: UserDTO или None если пользователь не найден в базе данных.
        """
        collection = client[cls.database_name][cls.collection_name]
        result = await collection.find_one({'_id': user_id})
        if not result:
            return
        user = UserDTO.from_serialised_mongo_dict(result)
        return user
    
    @classmethod
    async def select_all_users(
            cls,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> list[UserDTO]:
        """
        Выгрузка данных всех пользователей, записанных в базе.
        :param client: Асинхронный клиент для доступа к БД.
        :return: list[UserDTO]
        """
        collection = client[cls.database_name][cls.collection_name]
        result = await collection.find({})
        users = [UserDTO.from_serialised_mongo_dict(user) for user in result]
        return users

    @classmethod
    async def count_users(
            cls,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> int:
        """
        Число пользователей, записанных в базе данных.
        :param client: Асинхронный клиент для доступа к БД.
        :return: int
        """
        collection = client[cls.database_name][cls.collection_name]
        result = await collection.count_documents({})
        return result

    @classmethod
    async def del_user(
            cls,
            user_id: int,
            client: AsyncIOMotorClient = db_helper.get_client(),
    ) -> None:
        """
        Удаление данных конкретного пользователя из базы.
        :param user_id: Параметр '_id' нужного пользователя.
        :param client: Асинхронный клиент для доступа к БД.
        :return: None
        """
        collection = client[cls.database_name][cls.collection_name]
        await collection.delete_one({'_id': user_id})
