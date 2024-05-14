from typing import AsyncGenerator

from faker import Faker
import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from src.project import settings
from src.core.schemas import UserDTO, CityDTO

fake = Faker()

NUM_TESTS = 3
NUM_USERS_FOR_TESTS = 5


@pytest.fixture(scope="session")
async def fake_client() -> AsyncGenerator[AsyncIOMotorClient]:
	fake_client = AsyncIOMotorClient(settings.db_url_mongodb)
	yield fake_client
	fake_client.close()
	print('!fake_client CLOSED!')
	

@pytest.fixture
def fake_collection_users(
		fake_client: AsyncIOMotorClient,
) -> AsyncIOMotorCollection:
	return fake_client["database"]["users_test"]


@pytest.fixture(autouse=True, scope='session')
async def lifespan(
		fake_collection_users: AsyncIOMotorCollection,
):
	await fake_collection_users.delete({})
	yield
	await fake_collection_users.delete({})
	# async for fake_collection_users.delete({}) #TODO: когда будет доступ к библиотеке, проверить способ вызова функции
	# print(fake_collection_users.find({}))
	# await fake_client.close() 	# TODO: Проверить закрытие тестового клиента и осуществить здесь если не работает.
	

def get_new_city() -> CityDTO:
	return CityDTO(
		name=fake.city('Ru'),
		state=fake.state('Ru'),
		country=fake.country(),
		lat=fake.lat(),
		lon=fake.lon(),
	)


def get_new_user() -> UserDTO:
	return UserDTO(
		id=fake.random.randint(1, 1000),
		name=fake.first_name(),
		city=get_new_city(),
		sex=fake.sex(),
		wake_up_time=fake.time(),
		job_id=fake.random.randint(1, 1000),
	)
	

@pytest.fixture
async def new_city() -> CityDTO:
	return get_new_city()
	
	
@pytest.fixture
async def new_user() -> UserDTO:
	return get_new_user()
