from collections import deque, defaultdict
import heapq
import math
from passenger import Passenger, Passengers

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.coordinates = {}  # Store coordinates as {'A': (x, y)}
    
    def add_node(self, node, x, y):
        self.coordinates[node] = (x, y)
        
    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)  # Assuming undirected graph
    
    def calculate_distance(self, node1, node2):
        x1, y1 = self.coordinates[node1]
        x2, y2 = self.coordinates[node2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def calculate_shortest_path(self, start, end):
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

        return None

class RideMatchingSystem:
    def __init__(self, graph):
        self.graph = graph
        self.passenger_locations = {}
        self.driver_locations = {}
    
    def add_passenger(self, passenger):
        self.passenger_locations[passenger.passenger_id] = passenger.location
        self.graph.add_node(passenger.passenger_id, passenger.location[0], passenger.location[1])
    
    def add_driver(self, driver):
        self.driver_locations[driver.driver_id] = driver.location
        self.graph.add_node(driver_id, x, y)
    
    def find_closest_driver(self, passenger):
        closest_driver = None
        shortest_distance = float('inf')
        
        for driver_id in self.driver_locations:
            path, distance = self.graph.calculate_shortest_path(passenger.passenger_id, driver.driver_id)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_driver = driver_id
                
        return closest_driver, shortest_distance
'''
def main():
    g = Graph()
    system = RideMatchingSystem(g)

    # Adding passengers and drivers as nodes with coordinates
    system.add_passenger('Passenger1', 0, 0)
    system.add_driver('Driver1', 2, 3)
    system.add_driver('Driver2', 1, 1)
    
    # Adding edges between nodes for graph connectivity
    g.add_edge('Passenger1', 'Driver1')
    g.add_edge('Passenger1', 'Driver2')

    # Finding the closest driver for Passenger1
    closest_driver, distance = system.find_closest_driver('Passenger1')
    print(f"Closest driver to Passenger1: {closest_driver}")
    print(f"Distance: {distance}")

main()
'''

