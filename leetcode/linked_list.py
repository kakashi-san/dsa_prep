class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        """
        1. The uses a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
        2. When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
        3.The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.
        4. The method should only traverse the linked list once.  In other words, you can only use one loop.
        """
        self._slow_ptr = self.head
        self._fast_ptr = self.head

        while True:
            if not self._fast_ptr.next:
                return self._slow_ptr

            if not self._fast_ptr.next.next:
                return self._slow_ptr.next

            self._slow_ptr = self._slow_ptr.next
            self._fast_ptr = self._fast_ptr.next.next
        return self._slow_ptr
    
    def has_loop(self):
        """
        1. Create two pointers, slow and fast, both initially pointing to the head of the linked list.
        2. Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
        3.If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
        4.If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.
        """
        slow_ptr = self.head
        fast_ptr = self.head
        
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False


"""
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )
"""


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
    
"""    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False
"""


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
