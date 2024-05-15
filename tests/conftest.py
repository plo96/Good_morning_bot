from asyncio import new_event_loop, get_running_loop

from datetime import time

from faker import Faker
import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from src.project import settings
from src.core.schemas import UserDTO, CityDTO

fake = Faker()

NUM_TESTS = 3
NUM_USERS_FOR_TESTS = 5


@pytest.fixture(scope="session")
def get_loop():
	try:
		loop = get_running_loop()
	except RuntimeError:
		loop = new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope="session")
async def fake_client() -> AsyncIOMotorClient:
	fake_client = AsyncIOMotorClient(settings.db_url_mongodb)
	return fake_client
	

@pytest.fixture(scope="session")
def fake_collection_users(
		fake_client: AsyncIOMotorClient,
) -> AsyncIOMotorCollection:
	return fake_client["database"]["users_test"]


# @pytest.fixture(autouse=True, scope='session')
# async def lifespan(
# 		fake_client: AsyncIOMotorClient,
# ):
# 	# await fake_client["database"]["users_test"].delete_many({})
# 	yield
# 	# await fake_client["database"]["users_test"].delete_many({})
# 	fake_client.close()
# 	print('DATABASE CONNECTION CLOSED')


def get_new_city() -> CityDTO:
	return CityDTO(
		name=fake.city(),
		state=fake.state(),
		country=fake.country(),
		lat=float(fake.latitude()),
		lon=float(fake.longitude()),
	)


def get_new_user() -> UserDTO:
	return UserDTO(
		id=fake.random.randint(1, 1000),
		name=fake.first_name(),
		city=get_new_city(),
		sex=fake.passport_gender(),
		wake_up_time=time.fromisoformat(fake.time()),
		job_id=fake.random.randint(1, 1000),
	)
	

@pytest.fixture
async def new_city() -> CityDTO:
	return get_new_city()
	
	
@pytest.fixture
async def new_user() -> UserDTO:
	return get_new_user()
