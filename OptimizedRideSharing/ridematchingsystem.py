import heapq
import math
from passenger import Passenger
from driver import Driver
from hash_table import HashTable
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.coordinates = {}

    def add_node(self, node, x, y):  #add a node with coordinates to the graph
        self.coordinates[node] = (x, y)

    def add_edge(self, start, end):  #make a connection between two nodes
        self.graph[start].append(end)
        self.graph[end].append(start)

    def calculate_distance(self, node1, node2):  #calculate the distance between two nodes
        x1, y1 = self.coordinates[node1]
        x2, y2 = self.coordinates[node2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_shortest_path(self, start, end):  #calculate shortest path with Dijkstra's algorithm (implemented by ChatGPT 4o)
        queue = [(0, start, [start])]  # Priority queue with (cost, node, path)
        visited = set()

        while queue:
            cost, node, path = heapq.heappop(queue)

            if node in visited:
                continue
            visited.add(node)

            if node == end:
                return path, cost

            for adjacent in self.graph.get(node, []):
                if adjacent not in visited:
                    total_cost = cost + self.calculate_distance(node, adjacent)
                    heapq.heappush(queue, (total_cost, adjacent, path + [adjacent]))

        return None, float('inf')  # Return None path if end is unreachable

class RideMatchingSystem:
    def __init__(self, graph):
        self.graph = graph
        self.passenger_locations = HashTable(100) #initialize hash table for passenger locations
        self.available_drivers = HashTable(100) #initialize hash table for available drivers
        self.driver_distances = HashTable(100) #initialize hash table for driver distances

    def add_passenger(self, passenger):  #add a passenger to the system
        self.passenger_locations.put(passenger.passenger_id, passenger.location)
        self.graph.add_node(passenger.passenger_id, passenger.location[0], passenger.location[1])  #add the passenger's location to the graph
        
        #connect the passenger to all available drivers in the graph
        for i in range(len(self.available_drivers.table)):
            driver_entry = self.available_drivers.table[i]
            if driver_entry is not None and driver_entry != self.available_drivers.deleted_marker:
                driver_id, _ = driver_entry
                self.graph.add_edge(passenger.passenger_id, driver_id)  #draw edges between the passenger and the drivers

    def add_driver(self, driver):  #add a driver to the system
        self.available_drivers.put(driver.driver_id, driver)
        self.graph.add_node(driver.driver_id, driver.location[0], driver.location[1])  #add the driver's location to the graph
        
        for i in range(len(self.passenger_locations.table)):
            passenger_entry = self.passenger_locations.table[i]
            if passenger_entry is not None and passenger_entry != self.passenger_locations.deleted_marker:
                passenger_id, _ = passenger_entry
                self.graph.add_edge(passenger_id, driver.driver_id)  #draw edges between the driver and the passengers

    def find_closest_driver(self, passenger_id):  #find the closest driver to a passenger
        closest_driver = None
        shortest_distance = float('inf')

        #iterate through the available drivers in the hash table
        for i in range(len(self.available_drivers.table)):
            entry = self.available_drivers.table[i]
            if entry is not None and entry != self.available_drivers.deleted_marker:  #check for valid driver
                driver_id, driver = entry
                path, distance = self.graph.calculate_shortest_path(passenger_id, driver_id)
                
                if distance < shortest_distance:  #find the driver with the shortest distance to the passenger
                    shortest_distance = distance
                    closest_driver = driver
                    self.driver_distances.put(driver_id, distance)

        if closest_driver:
            self.available_drivers.remove(closest_driver.driver_id)  #remove the closest driver from available drivers
            return closest_driver, shortest_distance  #return the closest driver and the distance to the passenger
        else:
            print(f"No available driver found for passenger {passenger_id}.")
            return None, float('inf')

#for debugging purposes
'''
def main():
    g = Graph()
    system = RideMatchingSystem(g)

    # Adding passengers and drivers as nodes with coordinates
    
    system.add_passenger(Passenger('Passenger1', (0, 0), (1, 1), 2, 1))
    system.add_driver(Driver('Driver1', (2, 2), 4.8, 4))
    system.add_driver(Driver('Driver2', (1, 1), 4.5, 4))
    
    # Adding edges between nodes for graph connectivity
    g.add_edge('Passenger1', 'Driver1')
    g.add_edge('Passenger1', 'Driver2')

    # Finding the closest driver for Passenger1
    closest_driver, distance = system.find_closest_driver('Passenger1')
    print(f"Closest driver to Passenger1: {closest_driver.driver_id}")
    print(f"Distance: {distance}")

main()
'''