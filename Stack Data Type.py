# Stack Data Type

# Import Queue
from collections import deque

# Queue Class
class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# Stack Class
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()
