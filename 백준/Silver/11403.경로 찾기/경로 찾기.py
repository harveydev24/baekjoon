N = int(input())

edges = []

for n in range(N):
    edges.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if edges[i][k] and edges[k][j]:
                edges[i][j] = 1

for item in edges:
    print(*item)