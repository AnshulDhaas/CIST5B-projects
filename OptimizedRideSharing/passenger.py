from collections import deque

class Passenger:
    def __init__(self, passenger_id, location, destination, luggage, people):
        self.passenger_id = passenger_id
        self.location = location
        self.destination = destination
        self.luggage = luggage
        self.people = None
        self.driver = None
    
    def request_ride(self, driver):
        pass
        # we will calculate the shortest distance for the driver to reach the passenger

class Passengers:
    passengers = deque()
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        
    def search_passenger(self, passenger_id):
        for passenger in self.passengers:
            if passenger.passenger_id == passenger_id:
                return passenger