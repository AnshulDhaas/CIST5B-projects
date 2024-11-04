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
    
    def driver_distance(self, driver):
        return math.sqrt((driver.location[0] - self.location[0]) ** 2 + (driver.location[1] - self.location[1]) ** 2)
    
    def merge_sort_drivers(self, drivers):
        if len(drivers) <= 1:
            return drivers

        mid = len(drivers) // 2
        left_half = self.merge_sort_drivers(drivers[:mid])
        right_half = self.merge_sort_drivers(drivers[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_list = []
        while left and right:
            if self.driver_distance(left[0]) <= self.driver_distance(right[0]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))

        #append any remaining elements from both halves
        sorted_list.extend(left)
        sorted_list.extend(right)
        return sorted_list

    def rank_drivers(self, drivers):
        sorted_drivers = self.merge_sort_drivers(drivers)
        print("Sorted Drivers:", [(driver.driver_id, self.driver_distance(driver)) for driver in sorted_drivers])

        #populate best_drivers with sorted drivers
        for driver in sorted_drivers:
            self.best_drivers.add(driver)
        
        return sorted_drivers
        
    def display_drivers(self):
        for driver in self.best_drivers:
            print(f"Driver ID: {driver.driver_id}, Distance: {self.driver_distance(driver)}, Rating: {driver.rating}, Capacity: {driver.weight_capacity}")

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
    
    def __iter__(self):  #make Passengers iterable (implemented by ChatGPT 4o)
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
