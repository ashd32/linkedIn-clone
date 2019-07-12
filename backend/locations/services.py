import requests
#from .models import Country, City

class GeoLocation:

    BASE_URL = "https://api.hh.ru"
    ALL_COUNTRIES_URL = '/areas/countries'
    CITIES_FROM_COUNTRY_URL = '/areas/{0}'

    @classmethod
    def get_all_countries(cls):
        response = requests.get(cls.BASE_URL + cls.ALL_COUNTRIES_URL)
        data = response.json()
        for country in data:
            print(country['name'])
        return data
    
    @classmethod
    def get_all_cities_from_country(cls, id):
        response = requests.get(cls.BASE_URL + cls.CITIES_FROM_COUNTRY_URL.format(id))
        data = response.json()
        
        

g = GeoLocation()
g.get_all_countries()

class DataHandler:

    def __init__(self, model):
        self.model = model

    def save_countries_list(self, countries):
        for country in countries:
            if self._is_not_alredy_exist(country):
                # self.model.objects.create(id=country['id], name=country['name])
                pass

    def save_city_list(self, cities):
        for city in cities:
            if self._is_not_already_exist(cities):
                pass
    
    def _is_not_alredy_exist(self, country):
        # if model.objects.get(id=country['id']).exists():
        #   return False
        return True 
    

    