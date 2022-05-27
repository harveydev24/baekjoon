import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]


for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        adj[a].append((b, c))
        adj[b].append((a, c))


T = set([1])
q = []

heapq.heapify(q)

for next, cost in adj[1]:
    heapq.heappush(q, (cost, next))

ans = 0

while len(T) < N:
    c, n = heapq.heappop(q)
    if n not in T:
        T.add(n)
        ans += c

        for next, cost in adj[n]:
            if next not in T:
                heapq.heappush(q, (cost, next))

print(ans)
