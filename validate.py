from pathlib import Path

from city import City

cities_path = Path(__file__).parent / 'cities'
for city_path in cities_path.iterdir():
    city = City.validate(city_path)

print("Validation successful")
