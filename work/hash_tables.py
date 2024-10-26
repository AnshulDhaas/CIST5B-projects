myDict = {
    "key": "value"
}

print(hash('key'))
print(abs(hash('key')) % 10)

'''
class HashTable:
    def __init__(self):
        self.table = {}
        
    def insert(self, key, value):
        self.table[key] = value
        print(f"Inserted {value} at index {key}")
    
    def lookup(self, key):
        if key in self.table:
            print(f"Found {self.table[key]} at index {key}")
'''

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.deleted_marker = "DELETED"
    
    def hashFunction(self, key):
        return abs(hash(key)) % self.size
    
    def put(self, key, value):
        #hash our initial index
        #loop until we find an empty slot or we have looped through the entire list
        #do I have an empty spot?
        #otherwise: probe linearly (look at next index, wrapping around if necessary)
        hashIndex = self.hashFunction(key)
        originalIndex = hashIndex
        while self.table[hashIndex] is not None and self.table[hashIndex] != self.deleted_marker:
            if self.table[hashIndex][0] == key:
                break
            hashIndex = (hashIndex + 1) % self.size
            if hashIndex == originalIndex:
                print("Table is full")
                return
        
        self.table[hashIndex] = (key, value)
        
    def get(self, key):
        #hash our initial index
        #probe through the table until we find our key, or run out of elements
        #if we find a None, we know that it doesn't exist, exit early
        #if we find a key, then return value
        #otherwise if none of these, then linear probe forward
        
        #if while loop ends key doesn't exist
        
        hashIndex = self.hashFunction(key)
        originalIndex = hashIndex
        
        while self.table[hashIndex] is not None:
            if self.table[hashIndex][0] == key:
                return self.table[hashIndex][1]
            hashIndex = (hashIndex + 1) % self.size
            if hashIndex == originalIndex:
                return None
        return None
    
    def remove(self, key):
        #hash our initial index
        #probe through the table until we find our key, or run out of elements
        #if we find a None, we know that it doesn't exist, exit early
        #if we find a key, then remove it
        #otherwise if none of these, then linear probe forward
        
        #if while loop ends key doesn't exist
        
        hashIndex = self.hashFunction(key)
        originalIndex = hashIndex
        
        while self.table[hashIndex] is not None:
            if self.table[hashIndex][0] == key:
                self.table[hashIndex] = self.deleted_marker
                return
            hashIndex = (hashIndex + 1) % self.size
            if hashIndex == originalIndex:
                return
        return
    
        