from typing import AsyncGenerator, Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from src.project import settings


class DatabaseHelper:
    def __init__(
            self,
            uri: str,
    ):
        self._uri = uri
        self._client = AsyncIOMotorClient(self._uri)

    def get_client(self) -> AsyncIOMotorClient:
        return self._client


db_helper = DatabaseHelper(settings.db_url_mongodb)
