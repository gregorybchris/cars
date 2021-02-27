import json
from pathlib import Path

from jsonvl import validate_file

from car import Car
from light import Light
from road import Road
from signal import Signal


class City:
    CARS_FILE = 'cars.json'
    LAYOUT_FILE = 'layout.json'
    SCHEDULE_FILE = 'schedule.json'

    SCHEMAS_DIR = Path(__file__).parent / 'schemas'

    def __init__(self, roads, lights, cars, time_allocated):
        self.roads = roads
        self.lights = lights
        self.cars = cars
        self.time_allocated = time_allocated

    @classmethod
    def validate(cls, city_config_path):
        for filename in [cls.CARS_FILE, cls.LAYOUT_FILE, cls.SCHEDULE_FILE]:
            schema_path = cls.SCHEMAS_DIR / filename
            data_path = Path(city_config_path) / filename
            validate_file(data_path, schema_path)

    @classmethod
    def from_config(cls, city_config_path):
        cars_filepath = Path(city_config_path) / cls.CARS_FILE
        with open(cars_filepath, 'r') as f:
            car_records = json.load(f)

        layout_filepath = Path(city_config_path) / cls.LAYOUT_FILE
        with open(layout_filepath, 'r') as f:
            layout = json.load(f)

        schedule_filepath = Path(city_config_path) / cls.SCHEDULE_FILE
        with open(schedule_filepath, 'r') as f:
            schedule = json.load(f)

        lights = {}
        roads = {}
        cars = {}

        for road_record in layout['roads']:
            id = road_record['id']
            length = road_record['length']
            roads[id] = Road(id, length)

        for light_record in layout['lights']:
            id = light_record['id']
            roads_in_ids = light_record['roads_in']
            roads_out_ids = light_record['roads_out']
            for road_in in roads_in_ids:
                roads[road_in].light_out = id
            for road_out in roads_out_ids:
                roads[road_out].light_in = id
            lights[id] = Light(id, roads_in_ids, roads_out_ids)

        for car_record in car_records:
            id = car_record['id']
            road_ids = car_record['roads']

            # TODO: Check that the order of roads is possible

            cars[id] = Car(id, road_ids)

        time_allocated = layout['time_allocated']

        for light_record in schedule:
            light_id = light_record['light']
            signals = []
            for signal_record in light_record['signals']:
                road_id = signal_record['road']
                time = signal_record['time']
                signal = Signal(road_id, time)
                signals.append(signal)
            lights[light_id].signals = signals

        return cls(roads, lights, cars, time_allocated)
