class Light:
    def __init__(self, id, roads_in, roads_out):
        assert isinstance(id, int)

        self.id = id
        self.roads_in = roads_in
        self.roads_out = roads_out

        self.signals = None

        self.signal_number = 0
        self.signal_time = 0

        self.name = f"L{id}"

    @property
    def signal(self):
        return self.signals[self.signal_number]

    def tick(self):
        self.signal_time += 1
        if self.signal_time == self.signal.length:
            self.signal_time = 0
            self.signal_number = (self.signal_number + 1) % len(self.signals)

    def is_green(self, road):
        return self.signal.road == road

    def __repr__(self):
        return f"Light(id={self.id}, roads_in={self.roads_in}, roads_out={self.roads_out}"
