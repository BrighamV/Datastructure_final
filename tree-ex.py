class BST:                                                  # class for the Binary Search tree


    class Node:                                             # Class for the Node
    

        def __init__(self, data):
         
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
      
        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node):                          # This is where all of the logic for adding to the BST is.
                                                            # Pay close attention to the comments as they explain what is being done.

        if len(data) == len(node.data):                     # This is taking out any repeats, Feel free to take this out to get repeats    
            pass
        elif len(data) < len(node.data):
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __iter__(self):                                  # These next to functions are used to iterate through the tree
        
        yield from self._traverse_forward(self.root)  


    def _traverse_forward(self, node):
      
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
  

print("\n=========== TESTS ===========")
tree = BST()
tree.insert('1')
tree.insert('22')
tree.insert('333')
tree.insert('55555')
tree.insert('4444')
tree.insert('9')  # In our tree we are not allowing repeats. Even though the string is 9 its length is 1 which was already used
for x in tree:
    print(x)  # 1, 22, 333, 4444, 55555
