class Node:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.next = None
        
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
    
    def hash_function(self, isbn):
        return int(isbn) % self.size
    
    def insert(self, isbn, title):
        index = self.hash_function(isbn)
        new_node = Node(isbn, title)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, isbn):
        index = self.hash_function(isbn)
        current = self.table[index]
        if current is None:
            return "ISBN not found."
        if current.isbn == isbn:
            self.table[index] = current.next
            return f"Book with ISBN {isbn} deleted."
        prev = current
        current = current.next
        while current:
            if current.isbn == isbn:
                prev.next = current.next
                return f"Book with ISBN {isbn} deleted."
            prev = current
            current = current.next
        return "ISBN not found."

    def lookup(self, isbn):
        index = self.hash_function(isbn)
        current = self.table[index]
        while current:
            if current.isbn == isbn:
                return current.title
            current = current.next
        return "ISBN not found."

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            if current:
                print(f"Index {i}: ", end="")
                while current:
                    print(f"({current.isbn}, {current.title})", end=" -> ")
                    current = current.next
                print("None")
            else:
                print(f"Index {i}: None")