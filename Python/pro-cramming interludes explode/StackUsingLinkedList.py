# PROBLEM
# Discuss the stack data structure. Implement a stack in C (or python) using either
# a linked list or a dynamic array, and justify your decision. Design the interface to
# your stack to be complete, consistent, and easy to use.

class Node:
    """Node for a Singly Linked List."""
    def __init__(self, value):
        self.value = value
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
            string_to_print += str(current_node.value) + ' '
            return string_to_print
        else:
            return 'empty list!'

    def insert_after(self, index, value):
        if self.head is None:
            self.head = Node(value)
            return True
        else:
            current_node = self.head
            for i in range(0, index):
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    raise IndexError # Should I do this?
            new_node = Node(value)
            new_node.next = current_node.next
            current_node.next = new_node
            return True


    def insert_at_head(self, value):
        if self.head is None:
            self.head = Node(value)
            return True
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head
            return True

    def insert_at_tail(self, value):
        pass

    def delete(self, value):
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                break
            else:
                current_node = current_node.next
        current_node.next = current_node.next.next


    def get_node(self, value):
        pass

    def delete_by_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            current_node = self.head
            for i in range(0, index-1):
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    raise IndexError # Should I do this??
            current_node.next = current_node.next.next
            return True

    def get_node_index(self, value):
        pass



# A Stack needs a push and pop
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
