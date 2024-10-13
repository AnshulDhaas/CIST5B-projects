def double_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
        new_list.append(None)

def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while last.next:
        last = last.next
    last.next = new_node
    