import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [{} for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if adj[A].get(B) == None:
        adj[A][B] = C
    else:
        adj[A][B] = min(adj[A][B], C)
    if adj[B].get(A) == None:
        adj[B][A] = C
    else:
        adj[B][A] = min(adj[B][A], C)

q = [(1, 0)]
heapq.heapify(q)
INF = float('inf')
costs = [INF]*(N+1)
costs[1] = 0

while q:
    curr, curr_cost = heapq.heappop(q)

    if curr_cost > costs[curr]:
        continue

    for next, next_cost in adj[curr].items():
        if costs[next] > curr_cost + adj[curr][next]:
            costs[next] = curr_cost + adj[curr][next]
            heapq.heappush(q, (next, costs[next]))

print(costs[N])
