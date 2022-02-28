# Dijstra
from collections import deque

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)

dist = [float('inf')] * (N+1) 

def dijstra(X):
    q = deque([(X, 0)])
    dist[X] = 0 
    isThere = False

    while q:
        curr_node, curr_dist = q.popleft()
        if curr_dist > dist[curr_node]:
            continue

        for next in adj[curr_node]:
            tmp_dist = curr_dist + 1
            if dist[next] > tmp_dist:
                dist[next] = tmp_dist
                q.append((next, tmp_dist))

    for i in range(1, N+1):
        if dist[i] == K:
            print(i)
            isThere = True
    
    if not isThere:
        print(-1)

dijstra(X)