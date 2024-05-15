import pytest
from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.schemas import UserDTO

from tests.conftest import NUM_TESTS


@pytest.mark.parametrise('_', range(NUM_TESTS))
async def test_users_to_serialised_mongo_dict(
		_,
		new_user: UserDTO,
		fake_collection_users: AsyncIOMotorCollection,
):
	new_user_serialised_dict = new_user.to_serialised_mongo_dict()
	await fake_collection_users.insert_one(new_user_serialised_dict)
	mongodb_dict = await fake_collection_users.find_one({'_id': new_user.id})
	
	user_from_database = UserDTO.from_serialised_mongo_dict(mongodb_dict)
	
	assert user_from_database == new_user
	