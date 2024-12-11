from intersection import Intersection
from roads import Road  # Assuming Road class is in road.py
import heapq
import csv

class Graph:
    def __init__(self):
        self.adj_list = {}  # Adjacency list storing roads
        self.intersections = {}  # Dictionary of intersections
        self.roads = {}  # Dictionary of roads by (start, end)

    def add_intersection(self, name, latitude, longitude):
        """Add an intersection to the Graph"""
        if not isinstance(name, str): #For debugging purposes
            raise TypeError("Intersection name must be a string.")
        if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
            raise TypeError("Latitude and longitude must be numbers.")
        if name not in self.adj_list:
            self.adj_list[name] = []
            self.intersections[name] = Intersection(name, latitude, longitude)


    def add_road(self, start, end, distance, speed_limit, lanes):
        """Add a road to the Graph"""
        
        #Note: Graph is directed, so we only add the road from start to end
        if not isinstance(lanes, (int, float)) or lanes <= 0: #For debugging purposes
            raise ValueError("Lanes must be a positive integer.")
        if not isinstance(speed_limit, (int, float)) or speed_limit <= 0:
            raise ValueError("Speed limit must be a positive number.")
        if not isinstance(distance, (int, float)) or speed_limit <= 0:
            raise ValueError("Distance must be a positive number.")
        if start not in self.intersections or end not in self.intersections:
            raise ValueError(f"One or both intersections ({start}, {end}) do not exist.")

        road = Road(start, end, distance, speed_limit, lanes) #Create a new road
        self.adj_list[start].append(road) #Add the road to the adjacency list
        self.roads[(start, end)] = road 


    def dijkstra(self, start, end):
        """Dijkstra's algorithm to find the shortest path between two intersections"""
        pq = [(0, start)]
        distances = {v: float('inf') for v in self.adj_list}
        previous = {v: None for v in self.adj_list}
        distances[start] = 0

        while pq:
            current_dist, current = heapq.heappop(pq)
            if current == end:
                break
            if current_dist > distances[current]:
                continue
            for road in self.adj_list[current]:
                adjusted_weight = road.calculate_weight()
                distance = current_dist + adjusted_weight
                if distance < distances[road.end]:
                    distances[road.end] = distance
                    previous[road.end] = current
                    heapq.heappush(pq, (distance, road.end))

        path, current = [], end
        while current:
            path.append(current)
            current = previous[current]
        return distances[end], path[::-1]

    def recalculate_weights(self): 
        """Recalculate all weights to update the Graph"""
        for road in self.roads.values():
            road.calculate_traffic_score()

    def log_traffic_data(self):
        print("\nTraffic Data After Simulation:")
        for name, intersection in self.intersections.items():
            print(intersection)

    def export_intersections(self, file_name="intersections.csv"):
        """Export intersections from intersections.csv"""
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "latitude", "longitude", "congestion", "speed", "density", "lanes"])
            for name, intersection in self.intersections.items():
                writer.writerow([
                    name, intersection.latitude, intersection.longitude,
                    intersection.traffic_data["congestion"], intersection.traffic_data["speed"],
                    intersection.traffic_data["density"], intersection.traffic_data["lanes"]
                ])

    def get_intersection(self, name):
        return self.intersections.get(name, None)
