import heapq
from collections import defaultdict
import math
import pandas as pd
import numpy as np

class Rider:
    def __init__(self, location, destination, request_time):
        self.location = location
        self.destination = destination
        self.request_time = request_time

class Driver:
    def __init__(self, location, capacity, rating, vehicle, availability):
        self.location = location
        self.capacity = capacity
        self.rating = rating
        self.vehicle = vehicle
        self.availability = availability
    
    def update_location(self, new_location):
        self.location = new_location
    
    def set_availability(self, availability):
        self.availability = availability

class RideMatchingSystem:
    def __init__(self, riders, drivers):
        self.available_drivers = riders
        self.active_riders = {}
        self.active_drivers = {}
    
    