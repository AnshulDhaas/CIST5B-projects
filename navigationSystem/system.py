class System:
    def __init__(self, graph, cars=None):
        self.graph = graph # The road network graph
        self.cars = cars or [] # List of cars in the system

    def simulate_traffic(self):
        """Simulate traffic movement for all cars in the system."""
        print("\nStarting traffic simulation...")
        
        for car in self.cars:
            car.set_path()

        # Use a separate list to track active cars
        active_cars = []
        
        for car in self.cars:
            if car.check_location(): # Check if the car has reached its destination
                print(f"Car {car.id} has reached its destination at {car.current_location}. Removing from system.")
                continue

            current = car.current_location
            #print(f"Car {car.id} at {current}")
            car.update_next_intersection()
            # Update the car's next intersection based on the current location
            if car.next_intersection is None:
                print(f"Car {car.id} has no next intersection (dead end). Removing from system.")
                continue

            next_road = self.graph.roads.get((current, car.next_intersection))
            #Segment implemented by ChatGPT 4o, had trouble debugging
            if next_road:
                self.graph.intersections[current].dequeue_cars(1) # Remove the car from the current intersection
                next_road.update_traffic(cars_added=1) # Add the car to the next road
                next_road.update_weight() # Recalculate the weight of the road

                car.current_location = car.next_intersection # Update the car's current location
                print(f"Car {car.id} moved from {current} to {car.next_intersection}")
                active_cars.append(car)
            else:
                print(f"Car has reached a dead end, removing from system.")

        # Update the cars list to only include active cars
        self.cars = active_cars # Update the list of cars to only include active cars
                
    def find_shortest_path(self, start, end):
        return self.graph.dijkstra(start, end)
