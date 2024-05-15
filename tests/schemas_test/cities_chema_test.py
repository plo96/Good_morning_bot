import pytest

from src.core.schemas import CityDTO


async def test__cities_from_dict(
		new_city: CityDTO,
):
	city_dict = new_city.__dict__
	city_dict['wrong_attr'] = 'some_value'
	city_from_dict = CityDTO.from_dict(city_dict)
	
	assert city_from_dict == new_city


@pytest.mark.parametrize("wrong_type_attr",
						 [
							 {
								 'attr': 'name',
								 'value': 123,
							 },
							 {
								 'attr': 'state',
								 'value': 123,
							 },
							 {
								 'attr': 'country',
								 'value': 123,
							 },
							 {
								 'attr': 'lat',
								 'value': 'some_string',
							 },
							 {
								 'attr': 'lon',
								 'value': 'some_string',
							 },
						 ])
async def test__cities_from_dict_wrong_type(
		wrong_type_attr: dict,
		new_city: CityDTO,
):
	city_dict = new_city.__dict__
	city_dict[wrong_type_attr['attr']] = wrong_type_attr['value']
	
	with pytest.raises(TypeError):
		CityDTO.from_dict(city_dict)
