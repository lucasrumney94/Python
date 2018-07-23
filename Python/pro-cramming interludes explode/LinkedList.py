"""A LinkedList Implementation in Python."""
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
        node_values = []
        string_to_print = ''
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                node_values.append(current_node.value)
                current_node = current_node.next
            node_values.append(current_node.value)
            return ' '.join(str(node_value) for node_value in node_values)
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
