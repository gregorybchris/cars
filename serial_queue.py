from queue import Queue


class SerialQueue(Queue):
    def peek(self):
        item = self.get()
        self.put(item)
        return item
