
class my_stack:
    def __init__(self):
        self.stack = []

    def add_to_stack(self, data):
        self.stack.append(data)

    def take_from_stack(self):
        self.stack.pop()

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