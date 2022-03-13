import sys
sys.setrecursionlimit(100000)

T = int(input())

result = []

def DFS(x, y):
    visited[x][y] = True
    adj = []
    if x - 1 >= 0:
        adj.append((x-1,y))
    if y - 1 >= 0:
        adj.append((x, y-1))
    if x + 1 <= N - 1:
        adj.append((x+1, y))
    if y + 1 <= M - 1:
        adj.append((x, y+1))
    for item in adj:
        if not visited[item[0]][item[1]] and moo[item[0]][item[1]] == 1:
            DFS(item[0], item[1])

for i in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    moo = [[0] * (M) for _ in range(N)]
    visited = [[False] * (M) for _ in range(N)]

    for i in range(K):
        y, x = map(int, input().split())
        moo[x][y] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and moo[i][j] == 1:
                DFS(i, j)
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)