import pytest

from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.schemas import UserDTO

from tests.conftest import NUM_USERS_FOR_TESTS, get_new_user


async def add_users_to_database(
		collection: AsyncIOMotorCollection,
		num_of_users: int,
) -> None:
	for _ in range(num_of_users):
		await collection.insert_one(get_new_user().to_mongo_dict())


@pytest.fixture
async def clear_database(
		fake_collection_users: AsyncIOMotorCollection,
) -> None:
	await fake_collection_users.delete_many({})


@pytest.fixture
async def some_users_added(
		clear_database: None,
		fake_collection_users: AsyncIOMotorCollection,
) -> None:
	await add_users_to_database(
		collection=fake_collection_users,
		num_of_users=NUM_USERS_FOR_TESTS,
	)
	

@pytest.fixture
async def users_in_database(
		fake_collection_users: AsyncIOMotorCollection,
) -> list[UserDTO]:
	users_in_database: list = []
	async for user in fake_collection_users.find({}):
		users_in_database.append(UserDTO.from_mongo_dict(user))
	return users_in_database
