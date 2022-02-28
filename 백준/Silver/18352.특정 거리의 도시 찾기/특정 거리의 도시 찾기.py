from collections import deque

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)

dist = [-1] * (N+1) 

def bfs(X):
    q = deque([(X,0)])
    visited = [False] * (N+1)
    visited[X] = True
    isThere = 0

    while q:
        curr, cost = q.popleft()

        for next in adj[curr]:
            if not visited[next]:
                dist[next] = cost + 1
                visited[next] = True
                q.append((next, cost+1))
    
    for i in range(1,N+1):
        if dist[i] == K:
            print(i)
            isThere = True
    
    if not isThere:
        print(-1)

bfs(X)