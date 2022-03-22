V, E = map(int, input().split())
INF = int(1e9)
adj = [[INF]*V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

tmp = min([adj[x][x] for x in range(V)])

if tmp == INF:
    print(-1)
else:
    print(tmp)
