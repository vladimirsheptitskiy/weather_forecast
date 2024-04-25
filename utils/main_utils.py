import yaml
import sys
import config.global_config as conf
import time
import requests
sys.path.append('..')
class Cities:
    __cities: list
    __citi: str

    def set_cities(self, cities: list):
        self.__cities = cities

    def set_conf_yaml(self):
        with open('cities.yaml', 'w') as file:
            document = yaml.dump(self.__cities, file)

    def read_conf_yaml(self):
        with open('cities.yaml') as file:
            document = yaml.load(file, Loader=yaml.FullLoader)
            return document

    def cities_request(self, cities: list):
        api = conf.API_KEY
        citi_list = list()
        # url = conf.URL
        for citi in cities:
            url = f'http://api.openweathermap.org/geo/1.0/direct?q={str(citi)}&limit=1&appid={str(api)}'
            r = requests.get(url=url)
            citi_list.append(r.json())
            time.sleep(5)
        return citi_list

    def parsing_lat_float(self, data: list):
        name: str
        lat: float
        lon: float
        data_lat_lon = list()
        for i in data:
            for j in i:
                name = j.get('name')
                lat = j.get('lat')
                lon = j.get('lon')
            data_lat_lon.append({name, lat, lon})
        return data_lat_lon




