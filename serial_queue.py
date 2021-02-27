from collections import deque

class SerialQueue(deque):
    def put(self, v):
        self.append(v)

    def get(self):
        return self.popleft()

    def peek(self):
        return self[0] 

    def __repr__(self):
        return f"SerialQueue({[v for v in self]})"
