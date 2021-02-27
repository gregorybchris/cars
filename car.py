class Car:
    def __init__(self, id, roads):
        assert isinstance(id, int)

        self.id = id
        self.roads = roads
        self.road_number = 0
        self.road_miles = 0

        self.arrived = False
        self.waiting = False

        self.name = f"C{id}"

    @property
    def road(self):
        return self.roads[self.road_number]

    def at_end_of_road(self, road_length):
        return self.road_miles == road_length

    def on_last_road(self):
        return self.road_number == len(self.roads) - 1

    def next_road(self):
        self.road_number += 1
        self.road_miles = 0
        self.waiting = False

    def drive(self):
        self.road_miles += 1
        return self.road_miles

    def __repr__(self):
        return f"Car(id={self.id}, roads_in={self.roads}"
