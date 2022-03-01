import heapq

N = int(input())
q = []
heapq.heapify(q)
lst = []

for _ in range(N):
    d, w = map(int, input().split())
    lst.append((d,w))

lst.sort()

for d, w in lst:
    heapq.heappush(q, w)
    while len(q) > d:
        heapq.heappop(q)
    
print(sum(q))

