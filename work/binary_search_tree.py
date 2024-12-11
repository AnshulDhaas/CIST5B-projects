class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def search(self, current, target):
        #does current exist, if not return false
        
        if current is None:
            return False
        
        #if it exists, is it my target? If so return true
        if current.data == target:
            return True
        
        #if target < current search the left tree
        
        elif target < current.data:
            return self.search(current.left, target)
        
        #if target > current search the right tree
        
        else:
            return self.search(current.right, target)
    
    