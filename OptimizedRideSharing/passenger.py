from collections import defaultdict
import math
from driver import Driver, Drivers
from rider import Rider
from linkedlist import Linkedlist
from hash_table import HashTable

class Passenger(Rider):
    def __init__(self, passenger_id, location, destination, luggage, people):
        super().__init__(passenger_id, None, location, destination)
        self.luggage = luggage
        self.best_drivers = Linkedlist()
    
    def rank_drivers(self, drivers):  # Returns a list of drivers sorted by distance from the passenger
        def driver_rank(driver):
            distance = math.sqrt((driver.location[0] - self.location[0]) ** 2 + (driver.location[1] - self.location[1]) ** 2)
            print(f"Driver ID: {driver.driver_id}, Distance: {distance:.2f}")
            return distance 

        sorted_drivers = sorted(drivers, key=driver_rank)
        print("Sorted Drivers:", sorted_drivers)

        # Populate best_drivers with sorted drivers
        for driver in sorted_drivers:
            self.best_drivers.add(driver)
        
        return sorted_drivers
        
    def display_drivers(self):  #displays the best drivers for the passenger
        for driver in self.best_drivers:
            print(f"Driver ID: {driver.driver_id}, Distance: {math.sqrt((driver.location[0] - self.location[0]) ** 2 + (driver.location[1] - self.location[1]) ** 2)}, Rating: {driver.rating}, Capacity: {driver.weight_capacity}")

class Passengers:
    def __init__(self):
        self.passengers = Linkedlist()
        self.passengers_hash = HashTable(50)  #initialize hash table for passengers

    def add_passenger(self, passenger):  #add a passenger to the linked list and hash table
        self.passengers.add(passenger)
        self.passengers_hash.put(passenger.passenger_id, passenger)  #store the passenger by ID
    
    def remove_passenger(self, passenger):  #remove a passenger from both linked list and hash table
        self.passengers.remove(passenger)
        self.passengers_hash.remove(passenger.passenger_id)  #remove from the hash table by ID
        
    def search_passenger(self, passenger_id):  #search for a passenger by ID in the hash table
        return self.passengers_hash.get(passenger_id)  #search passenger in hash table by ID
    
    def get_all_passengers(self): #return all passengers in the linked list
        return [self.passengers.get(i) for i in range(self.passengers.size) if self.passengers.table[i] is not None]
    
    def __iter__(self):  # Make Passengers iterable
        current = self.passengers.head
        while current:
            yield current.data 
            current = current.next

'''
def main():
    passengers = Passengers()
    passenger1 = Passenger('Passenger1', (0, 0), (1, 1), 2, 1)
    passengers.add_passenger(passenger1)
    rankings = passenger1.rank_drivers([Driver('Driver1', (2, 2), 4.8, 4), Driver('Driver2', (1, 1), 4.5, 4)])
    print("Rankings:", rankings)
    passenger1.display_drivers()
'''
