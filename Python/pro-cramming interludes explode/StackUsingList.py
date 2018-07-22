class Stack():
    """The hard way."""
    def __init__(self):
        self.items = []

    def __str__(self):
        stack = ''
        for item in self.items:
            stack += str(item) + ' '
        return stack

    def pop(self):
        value_to_return = self.items[-1]
        del self.items[-1]
        return value_to_return

    def push(self, value):
        self.items.append(value)
        return True


my_stack = Stack()

print(my_stack)
my_stack.push(6)
my_stack.push(5)
my_stack.push(8)

print(my_stack)

what_did_i_pop = my_stack.pop()
print('I popped {}'.format(what_did_i_pop))
print(my_stack)


my_list = list()
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.append(5)
print(my_list)
