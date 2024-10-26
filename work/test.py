import heapq
import re

class Man:
    def __init__(self, start_station, destination_station, request_time):
        assert 1 <= start_station <= 4
        assert 1 <= destination_station <= 4
        self.start = start_station
        self.dest = destination_station
        self.btime = request_time
        self.wait_time = 0
        self.p = 999
        self.on_train = False
    
    def __lt__(self, other):
        return self.p < other.p
    
    def upd(self, wt):
        self.wait_time += wt
        
    def __str__(self):
        return f"[{self.start} -> {self.dest}] | {self.wait_time} | {abs(self.p)}"


# Chat GPTs Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        return None if self.is_empty() else self.top.data

    def is_empty(self):
        return self.top is None



class Train:
    def __init__(self):
        self.station = 1
        self.pq = []
        self.axi = Stack()
        self.tot = 0.
        self.cntr = 0
    
    def update_priorities(self):
        tmp = []
        flag = True
        for man in self.pq:
            if man.on_train:
                flag = False

        for man in self.pq:
            if man.on_train:
                man.p = abs(self.station - man.dest)
            else:
                if flag:
                    man.p = abs(self.station - man.start)
                else:
                    man.p = 999

            heapq.heappush(tmp, man)

        self.pq = tmp
        return flag

    def add_emergency(self, dest):
        self.axi.push(dest)
    

    def add_man(self, man):
        heapq.heappush(self.pq, man)
    

    def move(self):
        print('At Station', self.station)
        self.update_priorities()
        if len(self.pq) == 0:
            print('No passengers...')
            return
        #1. pickup passengers
        for man in self.pq:
            if man.start == self.station:
                print('Picked up:', man)
                man.on_train = True

        #2. decide next station
        #option 1 -> emergency
        next_station = None
        next_station = self.axi.pop()
        if next_station != None:
            print(f'Emergency to {next_station}!!!')
        
        if next_station is None: # option2 -> get from pq
            flg = self.update_priorities()
            if len(self.pq) > 0:
                if not flg:
                    next_station = self.pq[0].dest
                else:
                    next_station = self.pq[0].start


        if next_station is None:
            return

        print('Going to', next_station)
        # go to the next station
        time_diff = abs(next_station - self.station)
        self.station = next_station
        
        for man in self.pq:
            man.upd(time_diff)

        while not self.axi.is_empty() and self.axi.peek() == self.station:
            print('Resolved emergency...')
            self.axi.pop()
        
        self.update_priorities()
        tmp = []
        for man in self.pq:
            if man.dest == self.station and man.on_train:
                print('Dropped', man)
                self.tot += man.wait_time
                self.cntr += 1
            else:
                tmp.append(man)
        self.pq = tmp
        self.show()


    def show(self):
        print("Mean Wait Time:", self.tot / self.cntr if self.cntr > 0 else 0.)
        print("PQ:")
        self.update_priorities()
        for man in self.pq:
            print('\t', man)
        print("-" * 60)

    
# testing
train = Train()

man1 = Man(start_station=1, destination_station=4, request_time=10)
man3 = Man(start_station=3, destination_station=1, request_time=10)

train.add_man(man1)
train.add_man(man3)

train.move()
train.move()
train.move()
train.add_emergency(3)
train.add_emergency(4)
man2 = Man(start_station=2, destination_station=3, request_time=10)
train.add_man(man2)
train.move()
train.move()
train.move()
train.move()
train.move()
train.move()