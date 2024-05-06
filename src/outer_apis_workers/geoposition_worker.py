import requests as req

OPENWEATHERMAP_API_KEY = ''
city = 'Kyrlyk'
GEOPOSITION_URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=10&appid={OPENWEATHERMAP_API_KEY}'

response = req.get(url=GEOPOSITION_URL)

result = response.json()

# print(result)
# print(type(result))
for city in result:
    print(city)

    # {'name': 'Ust-Kan', 'local_names': {'de': 'Ust-Kan', 'en': 'Ust-Kan', 'ja': 'ウスチ=カン', 'ascii': 'Ust-Kan',
    #                                     'feature_name': 'Ust-Kan', 'ru': 'Усть-Кан'}, 'lat': 50.932003,
    #  'lon': 84.765213, 'country': 'RU', 'state': 'Altai Republic'}
    # {'name': 'Кононовский сельсовет', 'local_names': {'ru': 'Усть-Кан', 'en': 'Ust-Kan'}, 'lat': 56.5133832,
    #  'lon': 93.8010254, 'country': 'RU', 'state': 'Krasnoyarsk Krai'}


    # {'name': 'Kyrlyk', 'local_names': {'ru': 'Кырлык', 'en': 'Kyrlyk'}, 'lat': 50.8055937, 'lon': 84.9462522, 'country': 'RU', 'state': 'Altai Republic'}
