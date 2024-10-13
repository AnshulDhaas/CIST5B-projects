from collections import deque
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#Doubly linked list
class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def dequeue(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None
        
    def getLength(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (priority, value))
        
    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        else:
            return None
        
    def peek(self):
        if self.queue:
            return self.queue[0][1]
        else:
            return None
        
    def getLength(self):
        return len(self.queue)
    
    def changePriorities(self):
        tempHeap = []
        while not heap.isEmpty():
            item = heap.dequeue()
            tempHeap.append(item)
            
        for item in tempHeap:
            tupleWithUpdate = functionToUpdate(item)
            heapq.heappush(heap, tupleWithUpdate)
    

        
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.popleft()
dq.appendleft(4)

heap = []
heapq.heappush(priority, item)