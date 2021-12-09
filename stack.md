# Stacks

## Introduction
The stack is a fun data structure that can be very useful. My favorite way to explain what the stack is, is to think of a pile of plates. When you are washing the dishes you are going to add plates onto a STACK. The First plate that was added is going to be on the bottom of the stack. The last plate that was added will be on the top. Lets say you own 5 plates that are numberd 1-5. When you go to use a plate for lunch you are going to take from the top (plate 5). You now invite your best friend over for tacos. You will take a plate down for you friend (plate 4) and one for yourself(plate 3). To try and prove that you are a clean person you clean up after yourself and wash the dishes right away. You then put the dishes back onto the stack. Lets say you washed the 4 first then 3 then 5. Your stack will now be 1, 2, 4, 3, 5. You never touched the 1 and 2 so they will stay where they are. The 4, 3, and 5 will be in the stack in the order they were put there. The stack follows a rule called LIFO or Last In First Out. 

In python the stack is stored into a list[]. The list will hold the stack information. Using the stack means you are adding and taking away from the list according to the rules of the stack. 

As explained above the stack maintains the order that things are added to it.

The rules of the stack are:

* You cannot take from the bottom of the pile 
* You cannot add to the bottom of the pile
* You have to take from the top of the pile
* You have to add to the top of the pile

## Add to Stack
In Pyton you add to the stack by using the append function. Append will add to the top of the list which is exactly what we want for our stack. 

``` 
list.append(data)

```

## Take away from Stack
Similar to adding to the stack, python has a built in function to take away from the top of the list. Pop is the function that we want here. 

``` 
list.pop(data)

```

## Efficiency
The stack has great performance. Because we are always working with the end of the stack we never need to traverse through the stack to find data. Because of this all of the stacks functions will be done in O(1). O(1) is the most efficient we can get. If the stack works for your data storage needs, it is a great option because of its high efficiency. s

## Example
Here is an example problem to look through. Look at the code and try to understand. Once you have a good understanding of what it is doing, head to the practice problem to try it yourself.

This is for the random number

```
import random 
```

Create a list that we will use as a stack
```
items = []               
```
This is a menu that gathers input and calls the stacks function
```
def menu():
    print('a: add to stack')
    print('r: remove from stack')
    print('p: print your stack')
    print('')                             
    thing = input("Enter a, r or p: ")         
    print('')
    stacks(thing)
```

if a is given then we will add a random number. If r is given then we will take away from the stack.
```
def stacks(thing):
    if thing == 'a':
        items.append(random.randint(0,9))    
    elif thing == 'r':
        items.pop()                   
    elif thing == 'p':
        for x in range(len(items)):
         print(items[x])            
         print('')
    else:
        print ('invalid input')
    menu()

menu()
```


## Practice problem
This problem is ment to let you practice the stack. The code is started and has a test case for you. If everything works well, you will get the same answer as the one provided at the bottom of the file. Compair your code with the solution to see if you found the same solution I did. [practice problem](stack-problem.py)


## Solution
One important thing to remember about code. There are an infiinate number of solutions. Even though your solution might be different than mine, does not mean it is incorrect. Just make sure you are getting your solution as efficient as possible. [practice solution](stack-problem-solution.py)



Back to the [welcome page](welcome.md).