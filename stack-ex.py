import random                                   # This is for the random number

items = []                                      # Create a list that we will use as a stack

def menu():
    print('a: add to stack')
    print('r: remove from stack')
    print('p: print your stack')
    print('')                                   # Menu
    thing = input("Enter a, r or p: ")          # Gather input
    print('')
    stacks(thing)                               # Call stacks function with the input sent in

def stacks(thing):
    if thing == 'a':
        items.append(random.randint(0,9))       # If add then add a random number
    elif thing == 'r':
        items.pop()                             # If r then take away from the stack
    elif thing == 'p':
        for x in range(len(items)):
         print(items[x])                        # Print the stack
         print('')
    else:
        print ('invalid input')
    menu()

menu()



