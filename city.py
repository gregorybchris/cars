import json
from pathlib import Path

from car import Car
from light import Light
from road import Road
from signal import Signal


class City:
    LAYOUT_FILE = 'layout.json'
    SCHEDULE_FILE = 'schedule.json'

    def __init__(self, roads, lights, cars, time_allocated):
        self.roads = roads
        self.lights = lights
        self.cars = cars
        self.time_allocated = time_allocated

    @classmethod
    def from_config(cls, city_config_path):
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

        for car_record in layout['cars']:
            id = car_record['id']
            road_ids = car_record['roads']
            cars[id] = Car(id, road_ids)

        time_allocated = layout['time_allocated']

        for light_record in schedule:
            light_id = light_record['light']
            signals = []
            for signal_record in light_record['signals']:
                road_id = signal_record['road']
                length = signal_record['length']
                signal = Signal(road_id, length)
                signals.append(signal)
            lights[light_id].signals = signals

        return cls(roads, lights, cars, time_allocated)
