class Node:
    def __init__(self, data, n = None):
        self.data = data
        self.next = n
        
class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def length(self):
        return self.size
    
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        current = self.root
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.root = current.next
                self.size -= 1
                return True