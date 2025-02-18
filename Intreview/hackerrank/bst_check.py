def validate(node, min_, max_):
    if not node:
        return True
    if node.data <= min_ or node.data >= max_:
        return False
    return validate(node.left, min_, node.data) and validate(node.right, node.data, max_)


def check_binary_search_tree_(root):
    if validate(root, float('-inf'), float('inf')):
        return True
    else:
        return False