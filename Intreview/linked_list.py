class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return "This is a Linked List"

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                if current_node.next.next:
                    current_node.next = current_node.next.next
                else:
                    current_node.next = None
                return
            current_node = current_node.next


    def print(self):
        if not self.head:
            print("There is no data in the Linked List")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def reverse(self):
        current_node = self.head
        previous = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node
        self.head = previous

my_list = LinkedList()
print(my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.prepend(5)
my_list.prepend(1)
my_list.remove(30)
my_list.remove(5)
my_list.print()
my_list.reverse()
my_list.print()
print(my_list.size())

