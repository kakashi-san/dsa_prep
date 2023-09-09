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
        value: Any,
    ) -> None:

        """
        A constructor creates a new Node using the value arguement, and initializes
            1. the head and tail attributes of the linked list to point to the new node.
            2. length attribute, initialized to 1, which represents the current number of nodes in the list.
        """

        self.head = Node(value)
        self.tail = self.head

        self.length = 1

    def make_empty(self) -> None:
        """
        A function to empty the list.
            1. points the head and tail to None value
            2. re-initialises the list lenght to 0.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self) -> None:
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
        value: Any,
    ) -> bool:

        """
        A function to append value at the end of the list.
            1. Create a new node with give value set to value.
            2. Append the newly created node to the end of the list
        """
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node

        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = None
        self.length += 1

        return True

    def pop(self):
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

    def prepend(self, value: Any) -> bool:
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

    def pop_first(self):
        """
        A function to remove the first node (the head)
        update the head attribute and the length attribute accordingly,
        and return the removed node.
        1. handles the cases where the list is empty and where the list has one or more nodes.
        2. saves a reference to the current head node before updating the head attribute.
        3. updates the head attribute to the second node in the list.
        4. disconnects the removed node from the list by setting its next attribute to None.
        5. updates the length attribute of the LinkedList to reflect the removal of the node.
        6. If the list becomes empty after removing the node, set the tail attribute of the LinkedList to None.
        7. return the removed node, or None if the list is empty.
        """

        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            temp.next = None
            return temp
        
    def get(
            self,
            index
            ):
        """
        A function to take an integer index as a parameter
        and return a pointer to the node at the specified index in the linked list.

        1. handles the cases where the index is out of bounds.
        2. start at the head of the list and traverse the list using the next attribute of the nodes.
        3. should stop traversing the list when it reaches the specified index and return the node at that position.
        4. If the index is out of bounds, the method returns None.
        """

        if index > self.length or index < 0:
            return None
        
        temp = self.head
        track = 0
        while track < index:
            temp = temp.next
            track += 1

        return temp
    
    def set_value(
            self,
            index,
            value
            ):
        """
        A function takes an integer index and a value as parameters
        and updates the value of the node at the specified index in the linked list.

        1. update the value of the node if the node is found.
        2. returns True if the value is successfully updated.
        3. If the node is not found (i.e., the index is out of bounds), the method should return False.
        """
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False
    
    def insert(
            self,
            index,
            value
            ):
        """
        A function that takes an integer index and a value as parameters
        and insert a new node with the given value at the specified index in the linked list.

        1. take an integer index and a value as parameters and
        2. insert a new node with the given value at the specified index in the linked list.
        3. create a new node with the given value and insert it at the specified index.
        4. update the next attribute of the previous node to point to the new node.
        5. increment the length attribute of the LinkedList class.
        6. return True if the new node is successfully inserted.
        7. If the index is out of bounds,  return False.




        """
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        
        new_node = Node(value=value)
        
        temp = self.head
        pre = self.head
        track = 0
        while track < index:
            pre = temp
            temp = temp.next
            track += 1

        pre.next = new_node
        new_node.next = temp
        self.length += 1

        return True
    def remove(
            self,
            index
            ):
        """
        A function that takes an integer index as a parameter
        and remove the node at the specified index in the linked list,
        returning the removed node.
        1.  handle edge cases, such as removing a node at the beginning or end of the list.
        2.  utilize the pop_first() and pop() methods for handling these edge cases.
        3. use the get() method to find the node previous to the one to be removed.
        4.  update the next attribute of the previous node to point to the node after the removed one.
        5.  decrement the length attribute of the LinkedList class.
        6. return the removed node if the removal is successful.
        7. If the index is out of bounds, the method should return None.
        """
    
        if index < 0 or index >= self.length:
            return None
            
        if index == 0:
            return self.pop_first()
            
        if index == self.length-1:
            return self.pop()
            
        else:
            track = 0
            temp = self.head
            pre = self.head
            while track < index:
                pre = temp
                temp = temp.next
                track += 1
            
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp


my_linked_list = LinkedList(1)
my_linked_list.append(3)


print('LL before insert():')
my_linked_list.print_list()


my_linked_list.insert(1,2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()


my_linked_list.insert(0,0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()


my_linked_list.insert(4,4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()
            



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

"""
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(3).value)
"""
"""
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)


print('\nLL after set_value():')
my_linked_list.print_list()

"""

