"""
    Создание и инициализация класса, ответственного за подключение к базе данных (mongodb).
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


class DBConnector:
    """Класс, обеспечивающий подключение к базе данных с определёнными настройками."""
    
    def __init__(
            self,
            url: str,
    ):
        self._client = AsyncIOMotorClient(url)
    
    def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        """Возвращение ссылки на указанную коллекцию для обращения с базой данных"""
        return self._client["database"][collection_name]

    def close(self):
        """Закрытие экзмепляра клиента."""
        self._client.close()
