"""
Implementing a basic data structure: a singly linked list.
Create two classes:
    1. Node: Node class will represent an individual node within the linked list
    2. LinkedList: LinkedList class will manage the overall list structure.

"""

from typing import Any

class Node:

    def __init__(
        self,
        value: Any,
        ) -> None:
        """
        A constructor initializes:
            1. the value attribute of the node.
            2. the next attribute, initialized to None, will store a reference to the next node in the list.
        """
        self.value = value
        self.next = None
        
class LinkedList:

    def __init__(
        self,
        value : Any,
        ) -> None:

        """
        A constructor creates a new Node using the value arguement, and initializes
            1. the head and tail attributes of the linked list to point to the new node.
            2. length attribute, initialized to 1, which represents the current number of nodes in the list.
        """
        
        self.head = Node(value)
        self.tail = self.head
        
        self.length = 1

    def make_empty(
        self
    ) -> None:
        """
        A function to empty the list.
            1. points the head and tail to None value
            2. re-initialises the list lenght to 0.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(
            self
            )-> None:
        """
        A function that prints the linked list's elements,
        one per line.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(
        self,
        value
    )-> bool :
        
        """
        A function to append value at the end of the list.
            1. Create a new node with give value set to value.
            2. Append the newly created node to the end of the list
        """
        new_node = Node(
            value=value
            )
        
        if self.length == 0:
            self.head = new_node
            
        else:
            self.tail.next =  new_node

        self.tail = new_node
        self.tail.next =  None
        self.length += 1

        return True

"""
[CONSTRUCTOR VALIDATION]
"""

"""
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

"""
"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""


"""

[APPEND VALIDATION]
"""
"""
my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
"""

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""
