import heapq
from collections import deque

class Passenger:
    def __init__(self, start_station, destination_station, request_time):
        self.start_station = start_station
        self.destination_station = destination_station
        self.request_time = request_time
        self.priority = abs(ord(self.start_station) - ord(self.destination_station))

    def update_priority(self, current_station):
        self.priority = abs(ord(current_station) - ord(self.destination_station))

