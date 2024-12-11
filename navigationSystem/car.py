class Car:
    def __init__(self, graph, car_id, current_location, destination):
        self.graph = graph
        self.id = car_id
        self.current_location = current_location
        self.destination = destination
        self.path = []
        self.next_intersection = self.next_intersection()

    def set_path(self):
        """Calculates/sets the shortest path with Dijkstra's algorithm for the car using the graph"""
        distance, path = self.graph.dijkstra(self.current_location, self.destination)
        self.path = path
        self.next_intersection = path[1] if len(path) > 1 else None
        
            
    def check_location(self):
        """Check if the car has reached its destination"""
        if self.current_location == self.destination:
            print(f"Car {self.id} has reached its destination.")
            return True
        return False
    
    def update_next_intersection(self):
        """Update the next intersection based on the current location"""
        if self.path:
            self.path.pop(0)
            self.next_intersection = self.path[0] if self.path else None
        else:
            self.next_intersection = None
            
    def next_intersection(self):
        """Get the next intersection on the path"""
        if self.path == []:
            return None
        index = self.path.index(self.current_location)
        return self.path[index+1]
