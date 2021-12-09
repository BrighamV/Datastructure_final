class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
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


    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        #create node
        new_node = LinkedList.Node(value)
        # add tail and head if the list is empty
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        #add to the list at the tail if the list is not empty
        else:
            new_node.prev = self.tail #old tail is the new prev
            self.tail.next = new_node # the old tail next is the new node
            self.tail = new_node #the new node is now the tail


    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node


    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list only has one item we need to get rid of the head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None # get rid of the connection with the old tail
            self.tail = self.tail.prev # set the new tail to the tail


    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'


    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # we need to find where value is
        curr = self.head
        while curr is not None:
            if curr.data == value:
                #if we found the value we need to delete it
                if curr == self.tail:             # special case where we need to delete the tail
                    self.remove_tail()
                    return                        # the returns allow us to only delete one node
                elif curr == self.head:           # special case where we need to delete the head
                    self.remove_head()
                    return
                else:                             # remove the node and establish connections
                    curr.next.prev = curr.prev    # the next node has a previous of the previous node
                    curr.prev.next = curr.next    # the previous node had a next of the next node (the code is just as easy to read as the comments.)
                    return
            curr = curr.next


    def replace(self, old_value, new_value):
        """
        Searrch for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        # we need to find where old_value is
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                #if we found the value we need to delete it
                if curr == self.tail:             # special case where we need to replace the tail
                    self.remove_tail()
                    self.insert_tail(new_value)
                elif curr == self.head:           # special case where we need to replace the head
                    self.remove_head()
                    self.insert_head(new_value)
                    
                else:                             
                    self.insert_after(old_value, new_value)    # We already built functions to insert and delete nodes
                    self.remove(old_value)                     # We need to delete after we add so we dont add repeats of the nodes
            curr = curr.next


    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list


    def __str__(self):
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


# Answers!
# Question 1

ll = LinkedList()
ll.insert_tail('bob')
ll.insert_tail('sarah')
ll.insert_head('joe')
ll.insert_head('candice')
ll.insert_head('sally')
ll.insert_head('mike')
ll.insert_head('steven')
ll.insert_head('paul')
ll.insert_head('jane')
ll.insert_head('123')
print(ll)
# linkedlist[123, jane, paul, steven, mike, sally, candice, joe, bob, sarah]

# Question 2

ll.remove_head()
ll.remove_head()
ll.remove_head()
ll.remove_head()
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
print(ll)
# linkedlist[mike, sally, candice]