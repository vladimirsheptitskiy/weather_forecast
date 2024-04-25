from utils.main_utils import *
from config.global_config import *

cities = Cities()
cities.set_cities(['Izhma', 'Ukhta', 'Pechora', 'Syktyvkar'])
# cities.set_conf_yaml()
get_cities = cities.read_conf_yaml()
citi_list = cities.cities_request(get_cities)
citi_lat_lon = cities.parsing_lat_float(citi_list)
print(citi_lat_lon)