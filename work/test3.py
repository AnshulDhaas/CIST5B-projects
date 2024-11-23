class AVLTree:
    def __init__(self):
        self.root = None
    
    # Utility function to get the height of a node
    def _get_height(self, node):
        return node.height if node else 0
    
    # Utility function to update the height of a node
    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    # Get balance factor
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    # Right rotation
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    # Left rotation
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    # Insert a word
    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        # Normal BST insertion
        if not node:
            return AVLNode(word)
        elif word < node.word:
            node.left = self._insert(node.left, word)
        else:
            node.right = self._insert(node.right, word)
        
        # Update height
        self._update_height(node)

        # Get the balance factor
        balance = self._get_balance(node)

        # Perform rotations to balance the tree
        # Left Left Case
        if balance > 1 and word < node.left.word:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and word > node.right.word:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and word > node.left.word:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and word < node.right.word:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Search for a word
    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if not node:
            return False
        if word == node.word:
            return True
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    # Inorder traversal to display words and their balance
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            balance = self._get_balance(node)
            result.append((node.word, balance))
            self._inorder(node.right, result)