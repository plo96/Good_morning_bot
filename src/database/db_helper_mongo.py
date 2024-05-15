"""
    Создание и инициализация класса, ответственного за подключение к базе данных (mongodb).
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

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
    
    def get_collection_users(self) -> AsyncIOMotorCollection:
        """Возвращение эксземпляра коллекции пользователей для обращения с базой данных"""
        return self._client["database"]["users"]

    def __del__(self):
        """Удаление экзмепляра сессии при удалении экземпляра DatabaseHelper."""
        self._client.close()


db_helper = DatabaseHelper(settings.db_url_mongodb)
