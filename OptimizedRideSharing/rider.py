import math

class Rider:
    def __init__(self, passenger_id, driver_id, location, destination):
        self.passenger_id = passenger_id
        self.driver_id = driver_id
        self.location = location
        self.destination = destination
        
    def distance(self):
        """Calculate the distance to the rider's destination."""
        return math.sqrt((self.location[0] - self.destination[0]) ** 2 + (self.location[1] - self.destination[1]) ** 2)