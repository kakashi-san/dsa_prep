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
        value : Any,
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
        value : Any,
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
    
    def pop(
        self
        ):
        """
        A function to pop last value in the list.
            1. remove the last node (tail) from the linked list and return the removed node.
            2. If the list is empty, the method should return None. 
        """

        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(
            self,
            value: Any
            ) -> bool:
        """
        A function to add a new node with a given value to the beginning of the linked list, 
            1. handles the cases where the list is empty and non-empty
            2. creates a new node with the given value and add it to the beginning of the list.
            3. update the head and length attributes to reflect the addition of the new node.
            4. return True if the operation is successful.
        """
        new_node = Node(value=value)

        if self.length == 0:
            self.tail = new_node

        else:
            new_node.next = self.head
        
        self.head = new_node
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

"""
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")

"""
"""
my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


my_linked_list.prepend(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()

"""

"""
    EXPECTED OUTPUT:
    
    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Linked List:
    1
    2
    3   

"""