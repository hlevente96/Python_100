class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        ret = "  " * level + self.value + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def add_children(self, data):
        self.children.append(data)

class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.nodes = {root: self.root}

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, parent, child):
        if parent not in self.nodes:
            raise KeyError
        parent_node = self.nodes[parent]
        child_node = Node(child)
        parent_node.add_children(child_node)
        self.nodes[child] = child_node

# Example usage:
tree = Tree("root")
tree.insert("root", "child1")
tree.insert("root", "child2")
tree.insert("child1", "grandchild1")
tree.insert("child1", "grandchild2")
tree.insert("child1", "grandchild3")
tree.insert("child2", "grandchild4")
tree.insert("grandchild4", "grandgrandchild1")

print(tree)