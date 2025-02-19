import heapq

n = int(input())
heap = []
remove = set()
for _ in range(n):
    op, *v = input().split(" ")
    if int(op) == 1:
        heapq.heappush(heap, int(v[0]))
    elif int(op) == 2:
        remove.add(int(v[0]))
    else:
        while heap[0] in remove:
            remove.discard(heap[0])
            heapq.heappop(heap)
        print(heap[0])