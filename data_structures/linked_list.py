"""
implementing a basic data structure: a singly linked list.
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