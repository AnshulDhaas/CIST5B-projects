class Node:
    def __init__(self, data):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    
class AVLTree:
    def __init__(self):
        self.root = None
    
    def getHeight(self, node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rightRotate(self, y):
        newRoot = y.left
        T2 = newRoot.right
        
        newRoot.right = y
        y.left = T2
        
        y.height = max(self.getHeight(y.left), self.getHeight(y.right))+1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))+1
        
        return newRoot
    
    def leftRotate(self, x):
        newRoot = x.right
        T2 = newRoot.left
        
        newRoot.left = x
        x.right = T2
        
        x.height = max(self.getHeight(x.left), self.getHeight(x.right))+1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))+1
        
        return newRoot
    
    def insert(self, current, key):
        #Step 1: Perform normal BST insert
        if not current:
            return Node(key)
        elif key < current.key:
            current.left = self.insert(current.left, key)
        else:
            current.right = self.insert(current.right, key)
            
        #Step 2: Update height of this ancestor node
            
        current.height = max(self.getHeight(current.left), self.getHeight(current.right))+1
        
        #Step 3: Update the balance of this ancestor node
        
        balance = self.getBalance(current)
        
        #Step 4: Balance tree if unbalanced
        #Balance is positive: R, LR
        #Balance is negative: L, RL
        if balance > 1 and key < current.left.key:
            return self.rightRotate(current)
        
        if balance < -1 and key > current.right.key:
            return self.leftRotate(current)
        
        if balance > 1 and key > current.left.key:
            current.left = self.leftRotate(current.left)
            return self.rightRotate(current)