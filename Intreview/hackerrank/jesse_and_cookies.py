import heapq
def cookies(k, A):
    heapq.heapify(A)
    loop = 0
    while len(A) >= 2:
        if A[0] >= k:
            return loop
        loop += 1
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        heapq.heappush(A,a + 2*b)
    return loop if A[0] >=k else -1

print(cookies(7,[1, 2, 3, 9, 10, 12]))