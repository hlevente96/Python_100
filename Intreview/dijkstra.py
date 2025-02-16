import heapq

def dijkstra(graph, start):
    # Min-heap (priority queue)
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, node = heapq.heappop(pq)
        # If a shorter path has already been found, skip processing
        if current_distance > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

