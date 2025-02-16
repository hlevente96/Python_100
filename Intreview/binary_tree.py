class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def pre_order(self, node): # (Root -> Left -> Right)
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node): # (Left -> Root -> Right)
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def post_order(self, node): # (Left -> Right -> Root)
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

# Example usage:
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

print("Pre-order Traversal:")
bt.pre_order(bt.root)  # Output: 1 2 4 5 3

print("\nIn-order Traversal:")
bt.in_order(bt.root)  # Output: 4 2 5 1 3

print("\nPost-order Traversal:")
bt.post_order(bt.root)  # Output: 4 5 2 3 1
