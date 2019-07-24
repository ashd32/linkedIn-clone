import requests
from .models import Country, City

class GeoLocationApiClient:

    BASE_URL = "https://api.hh.ru"
    ALL_COUNTRIES_URL = '/areas/countries'
    CITIES_FROM_COUNTRY_URL = '/areas/{0}'

    @classmethod
    def get_all_countries(cls):
        response = requests.get(cls.BASE_URL + cls.ALL_COUNTRIES_URL)
        data = response.json()
        return data
    
    @classmethod
    def get_all_cities_from_country(cls, id):
        response = requests.get(cls.BASE_URL + cls.CITIES_FROM_COUNTRY_URL.format(id))
        data = response.json()
        return data['areas']
        
        
class DataHandler:

    def save_countries_list(self, countries):
        for country in countries:
            Country.objects.get_or_create(
                country_id=country['id'],
                name=country['name'],
            )
            
    def save_cities_list(self, cities):
        for city in cities:
            City.objects.get_or_create(
                city_id=city['id'],
                name=city['name'],
                country_id=city['parent_id']
            )
    

def load_locations():
    g = GeoLocationApiClient()
    data_handler = DataHandler()
    countries = g.get_all_countries()
    data_handler.save_countries_list(countries)
    for country in countries:
        cities = g.get_all_cities_from_country(country['id'])
        data_handler.save_cities_list(cities)

         