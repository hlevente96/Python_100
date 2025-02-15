class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        new_node = Node(data)
        current_node = self.head
        for _ in range(position-1):
            if not current_node.next:
                raise IndexError
            current_node = current_node.next
        previous_node = current_node.prev
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current_node
        current_node.prev = new_node

    def pop(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        previous_node = current_node.prev
        previous_node.next = None

    def drop(self):
        new_first_node = self.head.next
        new_first_node.prev = None
        self.head = new_first_node

    def print(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

    def reverse(self):
        current_node = self.head
        previous = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous
            current_node.prev = next_node
            previous = current_node
            current_node = next_node
        self.head = previous


my_list = DoubleLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(5)
my_list.append(40)
my_list.prepend(1)
my_list.pop()
my_list.insert(25,5)
my_list.pop()
my_list.drop()
my_list.insert(15,3)
my_list.print()
my_list.reverse()
my_list.print()
