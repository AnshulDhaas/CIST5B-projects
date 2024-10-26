class Node:
    def __init__(self, car=None, next_node=None):
        self.car = car
        self.next_node = next_node

class Cars:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, car):
        if self.size == 0:
            self.head = Node(car)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(car)
        self.size += 1

    def remove(self):
        if self.head is None:
            return None
        car = self.head.car
        self.head = self.head.next_node
        self.size -= 1
        return car

    def is_full(self, capacity):
        return self.size >= capacity

class Car:
    def park(self, parking_lot):
        raise NotImplementedError("Car must implement park method.")

class CompactCar(Car):
    def park(self, parking_lot):
        if parking_lot.park_compact_space(self):
            print("Compact car parked in compact space.")
        elif parking_lot.park_normal_space(self):
            print("Compact car parked in normal-sized space.")
        else:
            print("No parking spaces available for Compact car.")

class FullSizeCar(Car):
    def park(self, parking_lot):
        if parking_lot.park_normal_space(self):
            print("Full-size car parked in normal-sized space.")
        else:
            print("No parking spaces available for Full-size car.")

class ParkingLot:
    def __init__(self, normal_capacity=10, compact_capacity=5):
        self.normal_spaces = Cars()
        self.compact_spaces = Cars()
        self.normal_capacity = normal_capacity
        self.compact_capacity = compact_capacity

    def park_normal_space(self, car):
        if not self.normal_spaces.is_full(self.normal_capacity):
            self.normal_spaces.add(car)
            return True
        return False

    def park_compact_space(self, car):
        if not self.compact_spaces.is_full(self.compact_capacity):
            self.compact_spaces.add(car)
            return True
        return False