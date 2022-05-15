from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    indegree = [0]*N
    adj = [[] for _ in range(N)]

    for i in range(K):
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        adj[X].append(Y)
        indegree[Y] += 1

    W = int(input())-1

    visited = [0]*N

    q = deque([])
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)
            visited[i] = D[i]

    while q:
        curr = q.popleft()

        for next in adj[curr]:
            if visited[next] < visited[curr] + D[next]:
                visited[next] = visited[curr] + D[next]

            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(visited[W])
