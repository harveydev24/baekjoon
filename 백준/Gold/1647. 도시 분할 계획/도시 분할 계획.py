import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))

q = []
S = set([1])
costs = []


for next, cost in adj[1]:
    heapq.heappush(q, (cost, next))

while len(S) != N:
    curr_cost, curr = heapq.heappop(q)
    if curr not in S:
        S.add(curr)
        heapq.heappush(costs, -curr_cost)

    for next, cost in adj[curr]:
        if next not in S:
            heapq.heappush(q, (cost, next))
heapq.heappop(costs)
print(-sum(costs))