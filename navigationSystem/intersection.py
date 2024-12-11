from collections import deque

class Intersection:
    """Intersection class to represent an intersection/vertex in the road network."""
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.queue = deque()  # Car queue at the intersection
    
    def enqueue_cars(self, cars):
        """Add cars to an intersection"""
        for _ in range(cars):
            self.queue.append(1)  # Represents a car
    
    def dequeue_cars(self, cars):
        """Remove cars from an intersection"""
        for _ in range(cars):
            if self.queue:
                self.queue.popleft()
