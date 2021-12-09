
class my_stack:
    def __init__(self):
        self.stack = []             # creating the stack for you

    def add_to_stack(self, data):   # this function needs to add an item to the stack
        pass
    def take_from_stack(self):      # this function needs to Take away from the stack
        pass


# Test case to see if Stack worked correctly
the_stack = my_stack()
the_stack.add_to_stack(1)
the_stack.add_to_stack(2)
the_stack.take_from_stack()
the_stack.add_to_stack(3)
the_stack.add_to_stack(4)
the_stack.add_to_stack(5)
the_stack.take_from_stack()
the_stack.add_to_stack(6)
print(the_stack.stack)

# Answer should be [1, 3, 4, 6] IN THIS ORDER