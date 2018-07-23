# PROBLEM
# Discuss the stack data structure. Implement a stack in C (or python) using either
# a linked list or a dynamic array, and justify your decision. Design the interface to
# your stack to be complete, consistent, and easy to use.
from LinkedList import LinkedList

class Stack:
    """A Stack Datatype Implementation using a singly Linked List."""
    def __init__(self):
        self.top = None
        self.linked_list = LinkedList()

    def __str__(self):
        return self.linked_list.__str__()

    def push(self, value):
        self.linked_list.insert_at_head(value)
        self.top = self.linked_list.head.value

    def pop(self):
        popped_value_to_return = self.linked_list.head.value
        self.linked_list.delete_by_index(0)
        self.top = self.linked_list.head.value
        return popped_value_to_return

    def peek(self):
        return self.top



my_linked_list = LinkedList()

my_linked_list.insert_at_head(4)
print(my_linked_list)
my_linked_list.insert_at_head(9)
print(my_linked_list)
my_linked_list.insert_at_head(2)
print(my_linked_list)
my_linked_list.insert_after(1, 5)
print(my_linked_list)
my_linked_list.insert_after(0, 7)
print(my_linked_list)
my_linked_list.insert_after(2, 9)
print(my_linked_list)
my_linked_list.delete(9)
print(my_linked_list)
my_linked_list.delete_by_index(2)
print(my_linked_list)

print('Start Stack Testing')

my_stack = Stack()
my_stack.push(5)
print(my_stack)
my_stack.push(6)
print(my_stack)
my_stack.push(8)
print(my_stack)
my_stack.push(9)
print(my_stack)
print('Popping {}'.format(my_stack.pop()))
print(my_stack)
