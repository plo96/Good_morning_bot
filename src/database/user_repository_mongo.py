"""
	Класс для реализации способов взаимодействия с БД для сущности пользователей.
"""

from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.schemas import UserDTO
from src.database.db_helper_mongo import db_helper


class UserRepositoryMongo:
    """Репозиторий на основе mongodb для сущностей пользователей."""

    @classmethod
    async def add_user(
            cls,
            new_user: UserDTO,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
    ) -> None:
        """
        Добавление одного пользователя.
        :param new_user: Новый пользователь класса UserDTO для добавления в БД.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :return: None
        """
        await collection.insert_one(new_user.to_serialised_mongo_dict())

    @classmethod
    async def update_user(
            cls,
            user_id: int,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
            **kwargs,
    ) -> None:
        """
        Изменение параметров пользователя, записанного в базе данных под определённым id.
        :param user_id: Параметр '_id' изменяемого пользователя.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :param kwargs: Перечисление изменяемых параметров и их новых значений.
        :return: None
        """
        await collection.update_one({'_id': user_id}, {"$set": kwargs})

    @classmethod
    async def select_user(
            cls,
            user_id: int,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
    ) -> UserDTO | None:
        """
        Выгрузка данных конкретного пользователя из базы.
        :param user_id: Параметр '_id' нужного пользователя.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :return: UserDTO или None если пользователь не найден в базе данных.
        """
        result = await collection.find_one({'_id': user_id})
        if not result:
            return
        user = UserDTO.from_serialised_mongo_dict(result)
        return user

    @classmethod
    async def select_all_users(
            cls,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
    ) -> list[UserDTO]:
        """
        Выгрузка данных всех пользователей, записанных в базе.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :return: list[UserDTO]
        """
        users = [UserDTO.from_serialised_mongo_dict(user) async for user in collection.find({})]
        return users

    @classmethod
    async def count_users(
            cls,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
    ) -> int:
        """
        Число пользователей, записанных в базе данных.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :return: int
        """
        result = await collection.count_documents({})
        return result

    @classmethod
    async def del_user(
            cls,
            user_id: int,
            collection: AsyncIOMotorCollection = db_helper.get_collection_users(),
    ) -> None:
        """
        Удаление данных конкретного пользователя из базы.
        :param user_id: Параметр '_id' нужного пользователя.
        :param collection: Доступ к коллекции users через асинхронный клиент доступа к БД.
        :return: None
        """
        await collection.delete_one({'_id': user_id})
