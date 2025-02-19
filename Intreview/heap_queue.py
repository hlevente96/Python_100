from heapq import heappush, heappop, heapify
heap = [4,12,15,25]
heapify(heap)

heappush(heap, 10)
heappush(heap, 20)
heappush(heap, 5)
print("Heap after inserting elements:", heap)

min_elem = heappop(heap)
print("Popped element:", min_elem)  # 4
print("Heap after pop:", heap)  # [5, 10, 15, 25, 12, 20]

smallest = heap[0]
print("Smallest element without removing:", smallest)  # 5

