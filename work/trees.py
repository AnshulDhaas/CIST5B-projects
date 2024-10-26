class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def search(self, current, target):
        if current is None:
            return False
        if current.data == target:
            return True
        if current.data < target:
            return self.search(current.right, target)
        return self.search(current.left, target)
    
    def insert(self, current, data):
        if current is None:
            return Node(data)
        else:
            if data < current.data:
                current.left = self.insert(current.left, data)
            else:
                current.right = self.insert(current.right, data)
    
    def delete(self, current, target):
        if current is None:
            return current
        if target < current.data:
            current.left = self.delete(current.left, target)
        elif target > current.data:
            current.right = self.delete(current.right, target)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            current.data = self.min_value(current.right)
            current.right = self.delete(current.right, current.data)
        return current
        
    def inorder_traversal(self, current):
        if current:
            self.inorder_traversal(current.left)
            print(current.data)
            self.inorder_traversal(current.right)
            
    def preorder_traversal(self, current):
        if current:
            print(current.data)
            self.preorder_traversal(current.left)
            self.preorder_traversal(current.right)
            
    def postorder_traversal(self, current):
        if current:
            self.postorder_traversal(current.left)
            self.postorder_traversal(current.right)
            print(current.data)
