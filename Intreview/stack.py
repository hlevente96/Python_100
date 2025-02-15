class StackList:
    def __init__(self):
        self.stack = []

    def print(self):
        print(self.stack)

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

"""my_stack = StackList()
my_stack.append(10)
my_stack.append(20)
my_stack.append(30)
my_stack.append(40)
my_stack.print()
print(my_stack.is_empty())
print(my_stack.size())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
my_stack.print()"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class StackLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.head.data

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.count += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.head = self.head.next
        self.count -= 1

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

my_stack_linked_list = StackLinkedList()
my_stack_linked_list.append(10)
my_stack_linked_list.append(20)
my_stack_linked_list.append(30)
my_stack_linked_list.append(40)
my_stack_linked_list.print()
print(my_stack_linked_list.peek())
print(my_stack_linked_list.size())
my_stack_linked_list.pop()
my_stack_linked_list.pop()
my_stack_linked_list.print()
