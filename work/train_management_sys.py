import heapq
import random
#Passenger class modified by Anshul
class Passenger:
    def __init__(self, start_stop, end_stop, request_time):
        self.start = start_stop
        self.destination = end_stop
        self.req_time = request_time
        self.wait_duration = 0
        self.priority = 1000
        self.boarded = False
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def add_wait(self, time_diff):
        self.wait_duration += time_diff
        
    def __str__(self):
        return f"Passenger from stop {self.start} to stop {self.destination}, waited for {self.wait_duration} time units."

#EmergencyStack class modified by Anshul
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class EmergencyStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next_node
        return popped_node.value

    def peek(self):
        return None if self.is_empty() else self.top.value

    def is_empty(self):
        return self.top is None

#Train class modified by Anshul
class Train:
    def __init__(self):
        self.current_stop = 1
        self.passenger_queue = []
        self.emergency_stops = EmergencyStack()
        self.total_wait_time = 0
        self.passenger_count = 0
    
    def refresh_priorities(self):
        temp_queue = []
        has_boarded_passenger = False
        for passenger in self.passenger_queue:
            if passenger.boarded:
                has_boarded_passenger = True

        for passenger in self.passenger_queue:
            if passenger.boarded:
                passenger.priority = abs(self.current_stop - passenger.destination)
            else:
                passenger.priority = abs(self.current_stop - passenger.start) if has_boarded_passenger else 999
            heapq.heappush(temp_queue, passenger)

        self.passenger_queue = temp_queue
        return has_boarded_passenger

    def emergency_request(self, stop):
        self.emergency_stops.push(stop)
    

    def add_passenger(self, passenger):
        heapq.heappush(self.passenger_queue, passenger)
    

    def move(self):
        print(f"Currently at Stop {self.current_stop}")
        self.refresh_priorities()
        if len(self.passenger_queue) == 0:
            print("No passengers at this stop.")
            return
        
        for passenger in self.passenger_queue:
            if passenger.start == self.current_stop:
                print(f"Boarding: {passenger}")
                passenger.boarded = True

        next_stop = None
        next_stop = self.emergency_stops.pop()
        if next_stop is not None:
            print(f"Emergency Detour to Stop {next_stop}!")

        if next_stop is None:
            boarding_status = self.refresh_priorities()
            if len(self.passenger_queue) > 0:
                next_stop = self.passenger_queue[0].destination if not boarding_status else self.passenger_queue[0].start

        if next_stop is None:
            return

        print(f"Heading to Stop {next_stop}")
        time_to_travel = abs(next_stop - self.current_stop)
        self.current_stop = next_stop
        
        for passenger in self.passenger_queue:
            passenger.add_wait(time_to_travel)

        while not self.emergency_stops.is_empty() and self.emergency_stops.peek() == self.current_stop:
            print(f"Emergency resolved at Stop {self.current_stop}.")
            self.emergency_stops.pop()
        
        self.refresh_priorities()
        remaining_passengers = []
        for passenger in self.passenger_queue:
            if passenger.destination == self.current_stop and passenger.boarded:
                print(f"Dropping off: {passenger}")
                self.total_wait_time += passenger.wait_duration
                self.passenger_count += 1
            else:
                remaining_passengers.append(passenger)
        self.passenger_queue = remaining_passengers
        self.display_status()


    def display_status(self):
        average_wait_time = self.total_wait_time / self.passenger_count if self.passenger_count > 0 else 0
        print(f"Average Wait Time: {average_wait_time} time units.")
        print("Passenger Queue:")
        self.refresh_priorities()
        for passenger in self.passenger_queue:
            print(f"\t{passenger}")
        print()

    
# Randomized Testing
train = Train()

# Generate random passengers
for _ in range(5):  # Create 5 random passengers
    start_stop = random.randint(1, 4)
    end_stop = random.randint(1, 4)
    while end_stop == start_stop:  # Ensure start and end stops are different
        end_stop = random.randint(1, 4)
    request_time = random.randint(1, 20)  # Random request time between 1 and 20
    passenger = Passenger(start_stop=start_stop, end_stop=end_stop, request_time=request_time)
    train.add_passenger(passenger)

# Simulate train operations
train.move()
train.move()
train.move()

# Simulate emergencies
for _ in range(2):  # Create 2 random emergency requests
    emergency_stop = random.randint(1, 4)
    train.emergency_request(emergency_stop)

train.move()
train.move()
train.move()
train.move()
train.move()
train.move()

'''
Sample Output:

Currently at Stop 1
Heading to Stop 2
Average Wait Time: 0 time units.
Passenger Queue:
        Passenger from stop 3 to stop 2, waited for 1 time units.
        Passenger from stop 4 to stop 3, waited for 1 time units.
        Passenger from stop 2 to stop 1, waited for 1 time units.
        Passenger from stop 4 to stop 1, waited for 1 time units.
        Passenger from stop 3 to stop 1, waited for 1 time units.

Currently at Stop 2
Boarding: Passenger from stop 2 to stop 1, waited for 1 time units.
Heading to Stop 3
Average Wait Time: 0 time units.
Passenger Queue:
        Passenger from stop 3 to stop 2, waited for 2 time units.
        Passenger from stop 3 to stop 1, waited for 2 time units.
        Passenger from stop 2 to stop 1, waited for 2 time units.
        Passenger from stop 4 to stop 1, waited for 2 time units.
        Passenger from stop 4 to stop 3, waited for 2 time units.

Currently at Stop 3
Boarding: Passenger from stop 3 to stop 2, waited for 2 time units.
Boarding: Passenger from stop 3 to stop 1, waited for 2 time units.
Heading to Stop 3
Average Wait Time: 0 time units.
Passenger Queue:
        Passenger from stop 3 to stop 2, waited for 2 time units.
        Passenger from stop 4 to stop 1, waited for 2 time units.
        Passenger from stop 2 to stop 1, waited for 2 time units.
        Passenger from stop 3 to stop 1, waited for 2 time units.
        Passenger from stop 4 to stop 3, waited for 2 time units.

Currently at Stop 3
Boarding: Passenger from stop 3 to stop 2, waited for 2 time units.
Boarding: Passenger from stop 3 to stop 1, waited for 2 time units.
Emergency Detour to Stop 3!
Heading to Stop 3
Average Wait Time: 0 time units.
Passenger Queue:
        Passenger from stop 3 to stop 2, waited for 2 time units.
        Passenger from stop 4 to stop 1, waited for 2 time units.
        Passenger from stop 2 to stop 1, waited for 2 time units.
        Passenger from stop 3 to stop 1, waited for 2 time units.
        Passenger from stop 4 to stop 3, waited for 2 time units.

Currently at Stop 3
Boarding: Passenger from stop 3 to stop 2, waited for 2 time units.
Boarding: Passenger from stop 3 to stop 1, waited for 2 time units.
Emergency Detour to Stop 2!
Heading to Stop 2
Dropping off: Passenger from stop 3 to stop 2, waited for 3 time units.
Average Wait Time: 3.0 time units.
Passenger Queue:
        Passenger from stop 3 to stop 1, waited for 3 time units.
        Passenger from stop 2 to stop 1, waited for 3 time units.
        Passenger from stop 4 to stop 1, waited for 3 time units.
        Passenger from stop 4 to stop 3, waited for 3 time units.

Currently at Stop 2
Boarding: Passenger from stop 2 to stop 1, waited for 3 time units.
Heading to Stop 3
Average Wait Time: 3.0 time units.
Passenger Queue:
        Passenger from stop 4 to stop 1, waited for 4 time units.
        Passenger from stop 4 to stop 3, waited for 4 time units.
        Passenger from stop 3 to stop 1, waited for 4 time units.
        Passenger from stop 2 to stop 1, waited for 4 time units.

Currently at Stop 3
Boarding: Passenger from stop 3 to stop 1, waited for 4 time units.
Heading to Stop 4
Average Wait Time: 3.0 time units.
Passenger Queue:
        Passenger from stop 4 to stop 1, waited for 5 time units.
        Passenger from stop 4 to stop 3, waited for 5 time units.
        Passenger from stop 3 to stop 1, waited for 5 time units.
        Passenger from stop 2 to stop 1, waited for 5 time units.

Currently at Stop 4
Boarding: Passenger from stop 4 to stop 1, waited for 5 time units.
Boarding: Passenger from stop 4 to stop 3, waited for 5 time units.
Heading to Stop 4
Average Wait Time: 3.0 time units.
Passenger Queue:
        Passenger from stop 4 to stop 3, waited for 5 time units.
        Passenger from stop 4 to stop 1, waited for 5 time units.
        Passenger from stop 3 to stop 1, waited for 5 time units.
        Passenger from stop 2 to stop 1, waited for 5 time units.

Currently at Stop 4
Boarding: Passenger from stop 4 to stop 3, waited for 5 time units.
Boarding: Passenger from stop 4 to stop 1, waited for 5 time units.
Heading to Stop 4
Average Wait Time: 3.0 time units.
Passenger Queue:
        Passenger from stop 4 to stop 3, waited for 5 time units.
        Passenger from stop 4 to stop 1, waited for 5 time units.
        Passenger from stop 3 to stop 1, waited for 5 time units.
        Passenger from stop 2 to stop 1, waited for 5 time units.
'''