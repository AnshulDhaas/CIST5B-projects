class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, rider):  #adds a rider (Passenger or Driver) to the linked list
        node = Node(rider)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def remove(self, rider):  #removes a rider from the linked list
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == rider:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next
    
    def search(self, rider_id):  #searches for a rider by ID in the linked list
        current = self.head
        while current is not None:
            if current.data.rider_id == rider_id:
                return current.data
            current = current.next
        return None
    
    def __iter__(self): #iterates through the linked list (implemented by ChatGPT 4o, had issues debugging)
        current = self.head
        while current is not None:
            yield current.data
            current = current.next