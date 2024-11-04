from rider import Rider
from linkedlist import Linkedlist, Node

class Driver(Rider):
    def __init__(self, driver_id, location, rating, capacity): 
        super().__init__(None, driver_id, location, None)
        self.rating = rating
        self.weight_capacity = capacity
        self.passenger_id = None
        self.available = True
    
    def update_location(self, location):
        self.location = location
    
    def set_availability(self):
        self.available = not self.available

class Drivers:
    def __init__(self):
        self.drivers = Linkedlist()  
    
    def add_driver(self, driver):  #add a driver to linkedlist
        self.drivers.add(driver)
    
    def remove_driver(self, driver):  #remove driver from linked list
        self.drivers.remove(driver)
    
    def sort_drivers(self):  #sort drivers by driver_id using merge sort
        def merge_sort(linked_list):
            if linked_list.size <= 1:
                return linked_list
            
            mid = linked_list.size // 2
            left_half = Linkedlist()
            right_half = Linkedlist()
            current = linked_list.head
            index = 0
            
            while current:
                if index < mid:
                    left_half.add(current.data)
                else:
                    right_half.add(current.data)
                current = current.next
                index += 1
            
            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)
            
            return merge(left_sorted, right_sorted)
        
        def merge(left, right):
            sorted_list = Linkedlist()
            left_node = left.head
            right_node = right.head
            
            while left_node and right_node:
                if left_node.data.driver_id < right_node.data.driver_id:
                    sorted_list.add(left_node.data)
                    left_node = left_node.next
                else:
                    sorted_list.add(right_node.data)
                    right_node = right_node.next
            
            while left_node:
                sorted_list.add(left_node.data)
                left_node = left_node.next
            
            while right_node:
                sorted_list.add(right_node.data)
                right_node = right_node.next
            
            return sorted_list
        
        self.drivers = merge_sort(self.drivers)
    
    def search_driver(self, driver_id):
        drivers_list = list(self.drivers) #convert linked list to a list for binary search
        def binary_search(drivers, target_id):
            left, right = 0, len(drivers) - 1
            
            while left <= right:
                mid = (left + right) // 2
                mid_driver_id = drivers[mid].driver_id
                
                if mid_driver_id == target_id:
                    return drivers[mid]
                elif mid_driver_id < target_id:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return None
        
        self.sort_drivers()
        return binary_search(drivers_list, driver_id)
    
    def get_all_drivers(self): #return all drivers in the linked list
        return [self.drivers.get(i) for i in range(self.drivers.size) if self.drivers.table[i] is not None]
    
    def __iter__(self): #make drivers iterable (implemented by ChatGPT 4o)
        current = self.drivers.head
        while current:
            yield current.data
            current = current.next
