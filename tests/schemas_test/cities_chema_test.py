from src.core.schemas import CityDTO


async def test__cities_from_dict(
		new_city: CityDTO,
):
	city_dict = new_city.__dict__
	city_dict['']
	
