"""A Singly LinkedList Implementation in Python."""
class Node:
    """Node for a Singly Linked List."""
    def __init__(self, value):
        self.value = value
        self.next = None # the pointer initially points to nothing

class LinkedList:
    """Linked List."""
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            node_values = []
            string_to_print = ''
            current_node = self.head
            while current_node.next is not None:
                node_values.append(current_node.value)
                current_node = current_node.next
            node_values.append(current_node.value)
            return ' '.join(str(node_value) for node_value in node_values)
        else:
            return '~empty list!~'

    def to_list(self):
        if self.head is not None:
            node_values = []
            current_node = self.head
            while current_node.next is not None:
                node_values.append(current_node.value)
                current_node = current_node.next
            node_values.append(current_node.value)
            return node_values
        else:
            return []

    def insert_after(self, index, value):
        print('inserting {} after index {}'.format(value, index))
        if index >= self.length:
            return False

        if self.head is None:
            if index==0:
                self.head = Node(value)
                return True
            else:
                return False
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
            self.length += 1
            return True


    def insert_at_head(self, value):
        print('inserting {} at the head'.format(value))
        if self.head is None:
            self.length += 1
            self.head = Node(value)
            return True
        else:
            self.length += 1
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head
            return True

    def insert_at_tail(self, value):
        print('inserting {} at the tail'.format(value))
        # Find tail
        # Change tail.next
        if self.head == None:
            self.head = Node(value)
            self.length += 1
            return True
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            self.length += 1
            return True


    def delete(self, value):
        if self.head == None:
            return False

        print('deleting the first node with a value of {}'.format(value))
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        found_value = False
        current_node = self.head

        while not found_value:
            if current_node.next is None:
                return False
            elif current_node.next.value == value:
                current_node.next = current_node.next.next
                found_value = True
                self.length -= 1
            else:
                current_node = current_node.next

        return True


    def get_node(self, value): # Do I need this?
        pass

    def delete_by_index(self, index):
        """Delete an item by its index.
            Args:
                index (int): the index to be deleted.

            Returns:
                bool: the success of the deletion, True or False
        """
        if self.head == None:
            return False
        print('deleting the node at index {}'.format(index))
        if index >= self.length:
            return False
        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return True
        else:
            current_node = self.head
            for i in range(0, index-1):
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    raise IndexError # Should I do this??
            current_node.next = current_node.next.next
            self.length -= 1
            return True

    def delete_tail(self):
        return self.delete_by_index(self.length-1)

    def get_node_index(self, value):
        pass




# Test my Linked List Implementation
# TODO: Do real pytest
my_linked_list = LinkedList()

return_value = my_linked_list.insert_at_head(4)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [4])
assert return_value == True
assert my_linked_list.length == 1

return_value = my_linked_list.insert_at_head(9)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [9, 4])
assert return_value == True

return_value = my_linked_list.insert_at_head(2)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 9, 4])
assert return_value == True

return_value = my_linked_list.insert_after(7, 5)    # index error as 7 > length (which is 3)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 9, 4])      # Make sure the list hasn't changed
assert return_value == False

return_value = my_linked_list.insert_after(3, 5)    # index error as 3 == length (which is 3)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 9, 4])      # Make sure the list hasn't changed
assert return_value == False

return_value = my_linked_list.insert_after(1, 5)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 9, 5, 4])
assert return_value == True

return_value = my_linked_list.insert_after(0, 7)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 7, 9, 5, 4])
assert return_value == True

return_value = my_linked_list.insert_after(4, 9)
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 7, 9, 5, 4, 9])
assert return_value == True

return_value = my_linked_list.delete(321)             # Attempt to Delete a value that doesn't exist
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 7, 9, 5, 4, 9])
assert return_value == False

return_value = my_linked_list.delete(9)               # Delete a value that occurs twice
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 7, 5, 4, 9])
assert return_value == True

return_value = my_linked_list.delete(9)               # Delete the last value in the list
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [2, 7, 5, 4])
assert return_value == True

return_value = my_linked_list.delete(2)               # Delete the head
print(return_value, my_linked_list)
assert (my_linked_list.to_list() == [7, 5, 4])
assert return_value == True

# Repopulate the Linked List a bit
my_linked_list.insert_at_head(2)
my_linked_list.insert_at_head(6)
my_linked_list.insert_at_head(8)
my_linked_list.insert_at_head(14)
my_linked_list.insert_at_head(72)
my_linked_list.insert_at_head(32)

return_value = my_linked_list.delete_by_index(12)        # Attempt to Delete the node at index 12
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [32, 72, 14, 8, 6, 2, 7, 5, 4]
assert return_value == False

return_value = my_linked_list.delete_by_index(2)
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [32, 72, 8, 6, 2, 7, 5, 4]
assert return_value == True

return_value = my_linked_list.delete_by_index(0)        # Delete the node at the head
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [72, 8, 6, 2, 7, 5, 4]
assert return_value == True

return_value = my_linked_list.delete_by_index(6)        # Delete the node at the tail
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [72, 8, 6, 2, 7, 5]
assert return_value == True

return_value = my_linked_list.insert_at_tail(14)        # Insert a value at the tail
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [72, 8, 6, 2, 7, 5, 14]
assert return_value == True

return_value = my_linked_list.delete_tail()        # Delete value at the tail
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [72, 8, 6, 2, 7, 5]
assert return_value == True

return_value = my_linked_list.delete_tail()        # Delete value at the tail
print(return_value, my_linked_list)
assert my_linked_list.to_list() == [72, 8, 6, 2, 7]
assert return_value == True


# Empty Linked List Tests
print('Begin Empty List Testing')
empty_linked_list = LinkedList()

return_value = empty_linked_list.delete(3)
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == []
assert return_value == False

return_value = empty_linked_list.delete_tail()
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == []
assert return_value == False

return_value = empty_linked_list.delete_by_index(0)
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == []
assert return_value == False

return_value = empty_linked_list.insert_after(1, 2)
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == []
assert return_value == False

return_value = empty_linked_list.insert_at_tail(1)
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == [1]
assert return_value == True

return_value = empty_linked_list.delete_by_index(0)
print(return_value, empty_linked_list)
assert empty_linked_list.to_list() == []
assert return_value == True
