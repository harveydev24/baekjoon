N, M, H = map(int, input().split())
array = [[0]*(N+1) for _ in range(H+1)]
graph = [[0 for _ in range(N+1)] for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[a][b+1] = 1
    graph[a][b] = (a, b+1)
    graph[a][b+1] = (a, b)

k = 0


def check():
    adj = [0]*(N+1)
    for c in range(1, N+1):
        c_ = c
        r = 1
        hor = False
        while r <= H:
            if array[r][c] == 1 and hor == False:
                hor = True
                if graph[r][c]:
                    r, c = graph[r][c][0], graph[r][c][1]
            else:
                r, c = r+1, c
                hor = False
        adj[c_] = c
        if c_ != c:
            return False
    return True


def dfs(cnt):
    if cnt == k:
        if check():
            print(k)
            exit(0)
        return

    for i in range(1, H+1):
        for j in range(1, N):
            if array[i][j] == 0 and array[i][j+1] == 0:
                array[i][j], array[i][j+1] = 1, 1
                graph[i][j], graph[i][j+1] = (i, j+1), (i, j)
                dfs(cnt+1)
                array[i][j], array[i][j+1] = 0, 0
                graph[i][j], graph[i][j+1] = 0, 0


for k in range(4):
    dfs(0)

print(-1)
