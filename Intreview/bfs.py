from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            # Add unvisited neighbors to the queue
            queue.extend(graph[node] - visited)



