from pathlib import Path

from city import City
from simulation import simulate


city_path = Path(__file__).parent / 'cities' / 'city_1'
city = City.from_config(city_path)

completions = simulate(city)
print(f"Completions: {completions}")
