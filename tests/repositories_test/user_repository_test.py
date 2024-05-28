from random import choice, randint

import pytest
from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.schemas import UserDTO
from src.database import UserRepositoryMongo as UserRepository

from tests.conftest import NUM_TESTS, NUM_USERS_FOR_TESTS


@pytest.mark.parametrize("_", range(NUM_TESTS))
async def test_user_repository_add_user(
		_,
		clear_database: None,
		new_user: UserDTO,
		fake_collection_users: AsyncIOMotorCollection,
):
	await UserRepository.add_user(
		new_user=new_user,
		collection=fake_collection_users,
	)
	
	users_in_database = [user async for user in fake_collection_users.find({'_id': new_user.id})]
	assert len(users_in_database) == 1
	user_in_database = users_in_database[0]
	assert UserDTO.from_mongo_dict(user_in_database) == new_user


@pytest.mark.parametrize("param", list(UserDTO.__dict__.keys()))	# TODO: попробовать без 'list'
async def test_user_repository_update_user(
		param: str,
		new_user: UserDTO,
		fake_collection_users: AsyncIOMotorCollection,
		some_users_added: None,
		users_in_database: list[UserDTO],
):
	user = choice(users_in_database)
	param_to_change = {param: new_user.__getattribute__(param)}
	await UserRepository.update_user(
		user_id=user.id,
		collection=fake_collection_users,
		**param_to_change,
	)
	changed_user = UserDTO.from_mongo_dict(await fake_collection_users.find_one({'_id': user.id}))
	for attr in UserDTO.__dict__.keys():
		if attr == param:
			assert changed_user.__getattribute__(attr) == new_user.__getattribute__(attr)
		else:
			assert changed_user.__getattribute__(attr) == user.__getattribute__(attr)


@pytest.mark.parametrize("_", range(NUM_TESTS))
async def test_user_repository_select_all_users(
		_,
		some_users_added: None,
		users_in_database: list[UserDTO],
		fake_collection_users: AsyncIOMotorCollection,
):
	users = await UserRepository.select_all_users(
		collection=fake_collection_users,
	)
	assert set(users_in_database) == set(users)


@pytest.mark.parametrize("num_of_users", [randint(0, NUM_USERS_FOR_TESTS) for _ in range(NUM_TESTS)])
async def test_user_repository_count_users(
		clear_database: None,
		fake_collection_users: AsyncIOMotorCollection,
		num_of_users: int,
):
	await add_users_to_database(
		collection=fake_collection_users,
		num_of_users=num_of_users,
	)
	
	num_of_users_by_user_repository = await UserRepository.count_users(
		collection=fake_collection_users,
	)
	
	assert num_of_users_by_user_repository == num_of_users
	

@pytest.mark.parametrize("_", range(NUM_TESTS))
async def test_user_repository_del_user(
		_,
		fake_collection_users: AsyncIOMotorCollection,
		some_users_added: None,
		users_in_database: list[UserDTO],
):
	user_to_delete = choice(users_in_database)
	
	await UserRepository.del_user(
		user_id=user_to_delete.id,
		collection=fake_collection_users,
	)
	
	deleted_user = await fake_collection_users.find_one({'_id': user_to_delete.id})
	
	assert not deleted_user
	