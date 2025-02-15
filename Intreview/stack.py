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

my_stack = StackList()
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
my_stack.print()
