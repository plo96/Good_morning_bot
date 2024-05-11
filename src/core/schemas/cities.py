from dataclasses import dataclass


@dataclass
class CityDTO:
	name: str
	state: str
	country: str
	lat: float
	lon: float

	@classmethod
	def from_dict(cls, some_dict: dict):
		new_dict: dict = {}
		for attr, needed_type in cls.__annotations__.items():
			dict_value = some_dict.__getitem__(attr)
			if str(type(dict_value)) == needed_type:
				raise TypeError(f'Input dict with key "{attr}" is {dict_value}({type(dict_value)}), expected {needed_type}')
			else:
				new_dict.__setitem__(attr, dict_value)
		return CityDTO(**new_dict)
