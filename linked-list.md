# Linked-Lists
## Introduction
The linked list is a very efficient data structure that can be very useful in data storage. The name linked list can give a clue as to what it is. It is a bunch of objects that are linked together by pointing to each other. Because information can be added and taken away anywhere in the linked list it uses pointers to locate the next piece of data. We talked about tacos in the stack so lets try and use tacos to make this a little more clear. You set up a build your own taco bar at your appartment and invite a bunch of people over. You have tortillas, cheese, beef, lettuce, sour cream, and tomatos. You put them all on the counter and invite everyone to dig in. Your roomate really likes lettuce and you run out of lettuce. Now you have tortillas, cheese, beef, sour cream, and tomatos. You suddenly realize you forgot to get the avocados out. You slide the avacodos in after the cheese. Now you have tortillas, cheese, avacado, beef, sour cream and tomatos. Whenever you add or take something away the previous and next items just sit (point) next to each other. 
## Nodes
In our analogy the node would be the plate you are putting the ingreadiets on. Its what holds the data. You can put basically anything in the node that you would like. Even though a shoe is not a taco ingreadient you COULD put it on a plate and place it next to the sour cream. Nodes make the linked list a very versitile data structure because you can store whatever you like. 

The first item in your linked list is called the 'head' the last item in the linked list is called the 'tail'. All of the nodes are found relative to what node you are looking at (we will go deeper into this in the next couple of sections).
## Add Node
While it seems like a simple idea (and it really is). It takes a little bit of thinking to get all of the nodes in the right place. When you want to add a node you need to know what it is sitting against. Different connections need to happen when we are adding a node at the begining, end, or in the middle of the linked list. This example will sho adding a node at the begining or 'head' of the linked list (the practice problem has more inserts for you to look at). Lets check if the linked list is empty.

```
if self.head is None:
    self.head = new_node
    self.tail = new_node
```
If the node is not empty then we need to connect it to the next node (we can't put the tortillas on the couch, it needs to be in front of the cheese).

```
else:
    new_node.next = self.head # Connect new node to the previous head
    self.head.prev = new_node # Connect the previous head to the new node
    self.head = new_node      # Update the head to point to the new node   
```

## Remove Node
Removing a node is a lot like adding a node. Again, we are removing the head in this example. In this case we will see if the head and the tail are the same, in this case just set them to None.

* side note: in python setting a node's next or previous to None will break the connection. When a node has no connection we cannot find it. Python does a great job of taking these broken nodes and cleaning them up for us. Like taking the beef of the counter and letting your dog eat everything off the plate.

```
if self.head == self.tail:
    self.head = None
    self.tail = None
```
We then need to set the current head to None and make the next node the head. 

```
elif self.head is not None:
    self.head.next.prev = None  
    self.head = self.head.next  
```

## Efficiency
The efficiecy of the linked list is dependent on where the data is being edited. When dealing with the head or the tail, the efficiency will always be O(1). This is because we know where the head and tail are we don't need to search throught the data to find them. If we are adding or taking away from the middle of the linked list then the efficiency will be 0(n). A loop is required to find the node the place that we are adding or taking away a node.
## Example
The example goes over a simple linked list that will add to the head each time. Read the comments to better understand what each piece of code does. 
[example](linked-list-ex.py)
## Practice problem
This practice problem gives you the linked list data structure. Your job is to create test cases that will generate the solution outcome. Use the functions inside the Linked List class to complete this [practice problem](linked-list-problem.py).
## link to solution

[Practice solution](linked-list-solution.py)

Back to the [welcome page](welcome.md). 