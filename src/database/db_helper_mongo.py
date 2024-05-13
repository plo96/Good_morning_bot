"""
	Создание и инициализация класса, ответственного за подключение к базе данных.
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from src.project import settings


class DatabaseHelper:
    """Класс, обеспечивающий подключение к базе данных с определёнными настройками."""
    def __init__(
            self,
            url: str,
    ):
        self._url = url
        self._client = AsyncIOMotorClient(self._url)

    def get_client(self) -> AsyncIOMotorClient:
        """Возвращение экземпляра клиента для подключения к базе данных."""
        return self._client


db_helper = DatabaseHelper(settings.db_url_mongodb)
