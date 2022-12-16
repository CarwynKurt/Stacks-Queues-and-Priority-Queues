# Message Data Class

# Import Dataclass
from dataclasses import dataclass

# Message Class
@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

