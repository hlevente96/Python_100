def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            stack.extend(graph[node] - visited)  # Add unvisited neighbors


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)


