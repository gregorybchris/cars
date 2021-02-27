from pathlib import Path

from city import City
from simulation import simulate


city_name = 'city-2'
city_path = Path(__file__).parent / 'cities' / city_name
city = City.from_config(city_path)

# following = [2]
following = None

arrivals = simulate(city, following=following)
print(f"Successful arrivals: {arrivals}/{len(city.cars)}")
