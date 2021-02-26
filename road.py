from serial_queue import SerialQueue


class Road:
    def __init__(self, id, length):
        assert isinstance(id, int)

        self.id = id
        self.length = length

        self.light_in = None
        self.light_out = None

        self.cars_waiting = SerialQueue()

        self.name = f"R{id}"

    def is_first_in_line(self, car):
        return self.cars_waiting.peek() == car
