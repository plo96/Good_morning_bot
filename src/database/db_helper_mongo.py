from typing import AsyncGenerator, Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from src.project import settings


class DatabaseHelper:
    def __init__(
            self,
            uri: str,
    ):
        self._uri = uri

    async def get_session(self) -> AsyncGenerator[AsyncIOMotorClientSession, Any]:

        client = AsyncIOMotorClient(self._uri)
        try:
            async with await client.start_session() as session:
                yield session
        finally:
            client.close()


db_helper = DatabaseHelper(settings.db_uri_mongodb_asyncio)
