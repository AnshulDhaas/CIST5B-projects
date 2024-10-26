from collections import deque

class Driver:
    def __init__(self, driver_id, location, rating, capacity):
        self.driver_id = driver_id
        self.location = location
        self.rating = rating
        self.capacity = capacity
        self.passengers = deque()
    
    def update_location(self, location):
        self.location = location
    
    def setAvailability(self):
        self.available = (self.available != self.available)

class Drivers:
    def __init__(self):
        self.drivers = deque()
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def remove_driver(self, driver):
        self.drivers.remove(driver)
    
    def search_driver(self, driver_id):
        for driver in self.drivers:
            if driver.driver_id == driver_id:
                return driver
        return None