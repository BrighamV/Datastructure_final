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

        if data == node.data:                     # This is taking out any repeats, Feel free to take this out to get repeats    
            pass
        elif data < node.data:
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
 

    def __contains__(self, data):
      
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _contains(self, data, node):
        """
        You will write this _contains function. It's purpose is to return true if the tree contains the passed in data. 
        Reversely, it will return false if the value is not in the tree. 
        """
        if data == node.data:
            # print('it works')
            return True
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)

        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the right sub-tree.
                return self._contains(data, node.right)

    ###################
    # End Problem 1 #
    ###################

    def __iter__(self):
       
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)



tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

print("\n=========== PROBLEM 1 TESTS ===========")
print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False