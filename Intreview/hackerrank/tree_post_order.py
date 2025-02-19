class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(node, val):
    if not node:
        return TreeNode(val)
    if val < node.val:
        node.left = insert_into_bst(node.left, val)  # Insert to the left subtree
    else:
        node.right = insert_into_bst(node.right, val)  # Insert to the right subtree
    return node

def list_to_bst(lst):
    root = TreeNode(lst[0])
    for val in lst[1:]:
        insert_into_bst(root, val)  # Insert elements one by one
    return root

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=" ")

# Example usage
lst = [1, 2, 5, 3, 6, 4]
root = list_to_bst(lst)
post_order_traversal(root)
