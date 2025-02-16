from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def print(self):
        print(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


my_queue = MyQueue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.dequeue()
print(my_queue.peek())
my_queue.print()



class MyQueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def print(self):
        print(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


my_queue = MyQueueList()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.dequeue()
print(my_queue.peek())
my_queue.print()



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MyQueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self,data):
        new_data = Node(data)
        if self.is_empty():
            self.head = new_data
            self.tail = new_data
            self.count += 1
            return
        self.tail.next = new_data
        self.tail = new_data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty queue")
            return
        self.head = self.head.next
        self.count -= 1

    def peek(self):
        if self.is_empty():
            print("Empty queue")
            return
        return self.head.data

    def print(self):
        if self.is_empty():
            print("Empty queue")
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

    def is_empty(self):
        return True if not self.head else False

    def size(self):
        return self.count


my_queue = MyQueueLinkedList()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.print()
print(my_queue.peek())
print(my_queue.size())
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()