import requests

API_KEY = "7f8ebda4301b488b9a3a299fbe12d0f3"
BASE_URL = "http://geohelper.info/api/v1/"
COUNTRIES_URL = 'countries'
LOCALE_URL = '?locale%5Blang%5D=uk&locale%5BfallbackLang%5D=ru'



class GeoLocation:

    def get_all_counries(self):
        response = requests.get(BASE_URL + COUNTRIES_URL + API_KEY + LOCALE_URL )
        print(response.json())