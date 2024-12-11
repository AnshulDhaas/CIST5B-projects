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
    
    def add(self, node):
        node = Node(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def remove(self, node):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == node:
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
    
    def search(self, node_id):
        current = self.head
        while current is not None:
            if current.data.node_id == node_id:
                return current.data
            current = current.next
        return None
    
    def __iter__(self): #iterates through the linked list (implemented by ChatGPT 4o, had issues debugging)
        current = self.head
        while current is not None:
            yield current.data
            current = current.next