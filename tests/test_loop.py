import pytest

from tests.conftest import NUM_TESTS

@pytest.mark.parametrize("_", range(NUM_TESTS))
async def test_event_loop():
	print('Hi')
	assert 1 == 1
	