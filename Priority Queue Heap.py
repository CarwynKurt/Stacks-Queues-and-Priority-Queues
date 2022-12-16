# Priority Queue

# Import Heap
from heapq import heappush

# Heap priority
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

# Import Heap Pop
from heapq import heappop

# Heap Pop
heappop(fruits)
print(fruits)

# Python Version
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)
print(person2 < person3)