class Node:
    def __init__(self, key):
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
        if balance > 1 and key < current.left.key: #Positive balance
            return self.rightRotate(current)

        if balance < -1 and key > current.right.key:  #Negative balance
            return self.leftRotate(current)

        if balance > 1 and key > current.left.key: #Positive balance
            current.left = self.leftRotate(current.left)
            return self.rightRotate(current)
        
        if balance < -1 and key < current.right.key: #Negative balance
          current.right = self.rightRotate(current.right)
          return self.leftRotate(current)
        return current
      
    def search(self, current, target):
      if current is None:
          return False
      if current.key == target:
          return True
      if current.key < target:
          return self.search(current.right, target)
      return self.search(current.left, target)

    def inorder_traversal(self, current):
      if current:
          self.inorder_traversal(current.left)
          print(current.key)
          self.inorder_traversal(current.right)

def find_words(line):
  words = []
  word = ""
  for char in line:
    if char.isalpha():
      word += char.lower()
    else:
      if word:
          words.append(word)
          word = ""
  if word:
    words.append(word)
  return words

def load_dictionary(file, dictionary):
  with open(file, 'r') as file:
    for line in file:
      word = line.strip().lower()
      dictionary.insert(dictionary.root, word)

def check(file, dictionary, mispelled_words):
  with open(file, 'r') as file:
    for line in file:
      words = find_words(line)
      for word in words:
        if not dictionary.search(dictionary.root, word):
          mispelled_words.add(word)

def results(dictionary, mispelled_words):
  print("DICTIONARY:")
  dictionary.inorder_traversal(dictionary.root)
  print("MISPELLED WORDS:")
  mispelled_words = sorted(mispelled_words)
  for word in mispelled_words:
    print(word)



def main():
  dictionary = AVLTree()
  mispelled_words = set()
  load_dictionary("unique_words.txt", dictionary)
  check("messy_sentence.txt", dictionary, mispelled_words)
  results(dictionary, mispelled_words)

main()