class LinkedList:
    class Node:
        def __init__(self, data):               
            self.data = data
            self.next = None
            self.prev = None
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):                   #inserting a node at the head
     
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def __iter__(self):                                             # allows us to iterate through our linked list
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    
    def __str__(self):                                              # turns our linked list into a string we can see. 
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output



items = [1,2,3]                                                     #creating a list to insert into our linked list


ll = LinkedList()                                                   
ll.insert_head('String')                                            # a node can hold a string
ll.insert_head(2)                                                   # it can also hold an int
ll.insert_head(items)                                               # it can also hold a list
ll.insert_head(3)                                                   # it can basically hold anything
ll.insert_head('another string')
ll.insert_head(5)
print(ll) # linkedlist[5, another string, 3, [1, 2, 3], 2, String]
