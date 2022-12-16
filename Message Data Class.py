# Message Data Class

# Import Dataclass
from dataclasses import dataclass

# Message Class
@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

# Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]

# Priority Queue
messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)
