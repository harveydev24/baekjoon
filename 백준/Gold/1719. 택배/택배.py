N, M = map(int, input().split())

adj = [[0]*(N+1) for _ in range(N+1)]
cost = [[float('inf')]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = b
    adj[b][a] = a
    cost[a][b] = c
    cost[b][a] = c


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                adj[i][j] = adj[i][k]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            print('-', end=' ')
        else:
            print(adj[i][j], end=' ')
    print()
