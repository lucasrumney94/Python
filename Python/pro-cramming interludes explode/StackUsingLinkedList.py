# PROBLEM
# Discuss the stack data structure. Implement a stack in C (or python) using either
# a linked list or a dynamic array, and justify your decision. Design the interface to
# your stack to be complete, consistent, and easy to use.

class Node:
    """Node for a Singly Linked List."""
    def __init__(self, val):
        self.val = val
        self.next = None # the pointer initially points to nothing

class LinkedList:
    """Linked List."""
    def __init__(self):
        self.head = None

    def __str__(self):
        string_to_print = ''
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                string_to_print += str(current_node.value) + ' '
                current_node = current_node.next
            return string_to_print
        else:
            print('empty list!')

    def insert(self, position, data):

        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            for i in range(0, position):
                if current_node.next is not None:
                    current_node = current_node.next
                

    def delete(self, data):
        pass

    def get_node(self, data):
        pass

# A Stack needs a push and pop
class Stack:
    """A Stack Datatype Implementation using a singly Linked List."""
    def __init__(self):
        self.head = Node()

    def push(data):
        pass

    def pop(data):
        pass


my_linked_list = LinkedList()
my_linked_list.insert(0, 5)
my_linked_list.insert(0, 7)
print(my_linked_list)
