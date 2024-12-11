import pandas as pd
import random

# Generate intersections
def generate_intersections(num_intersections):
    intersections = []
    for i in range(num_intersections):
        name = chr(65 + (i % 26)) + str(i // 26)  # Generates A-Z, then A1-Z1, A2-Z2, etc.
        latitude = round(random.uniform(37.6, 37.9), 5)
        longitude = round(random.uniform(-122.5, -122.3), 5)
        intersections.append({"name": name, "latitude": latitude, "longitude": longitude})
    return intersections

# Generate roads
def generate_roads(intersections, num_roads):
    roads = []
    intersection_names = [i["name"] for i in intersections]
    for _ in range(num_roads):
        start, end = random.sample(intersection_names, 2)
        distance = round(random.uniform(1, 10), 2)
        speed_limit = random.choice([30, 40, 50, 60, 70])
        lanes = random.randint(1, 4)
        roads.append({"start": start, "end": end, "distance": distance, "speed_limit": speed_limit, "lanes": lanes})
    return roads

# Generate cars
def generate_cars(intersections, num_cars):
    cars = []
    intersection_names = [i["name"] for i in intersections]
    for car_id in range(1, num_cars + 1):
        current_location, destination = random.sample(intersection_names, 2)
        cars.append({"id": car_id, "current_location": current_location, "destination": destination})
    return cars

# Parameters
num_intersections = 50
num_roads = 150
num_cars = 200

# Generate data
intersections = generate_intersections(num_intersections)
roads = generate_roads(intersections, num_roads)
cars = generate_cars(intersections, num_cars)

# Save to CSV
pd.DataFrame(intersections).to_csv("intersections.csv", index=False)
pd.DataFrame(roads).to_csv("roads.csv", index=False)
pd.DataFrame(cars).to_csv("cars.csv", index=False)
