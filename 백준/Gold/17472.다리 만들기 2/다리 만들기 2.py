N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

def dfs(x, y, n):
    array[x][y] = n
    visited[x][y] = True

    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0<=xx<N and 0<=yy<M and not visited[xx][yy] and array[xx][yy] == 1:
            dfs(xx,yy,n)

n = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and array[i][j] == 1:
            dfs(i,j,n)
            n += 1

parent = [x for x in range(n)]

def search(x, y):
    res = []
    #right
    i = 1
    while y+i < M:
        if array[x][y+i] == array[x][y]:
            break
        if i <= 2 and array[x][y+i] != 0:
            break
        if array[x][y+i] == 0:
            i += 1
            continue
        if array[x][y] != array[x][y+i]:
            res.append((array[x][y], array[x][y+i], i-1))
            break
    #left
    i = 1
    while y-i >= 0:
        if array[x][y-i] == array[x][y]:
            break
        if i <= 2 and array[x][y-i] != 0:
            break
        if array[x][y-i] == 0:
            i += 1
            continue
        if array[x][y] != array[x][y-i]:
            res.append((array[x][y], array[x][y-i], i-1))
            break
    #up
    i = 1
    while x+i < N:
        if array[x+i][y] == array[x][y]:
            break
        if i <= 2 and array[x+i][y] != 0:
            break
        if array[x+i][y] == 0:
            i += 1
            continue
        if array[x+i][y] != array[x][y]:
            res.append((array[x][y], array[x+i][y], i-1))
            break
    #down
    i = 1
    while x-i >= 0:
        if array[x-i][y] == array[x][y]:
            break
        if i <= 2 and array[x-i][y] != 0:
            break
        if array[x-i][y] == 0:
            i += 1
            continue
        if array[x-i][y] != array[x][y]:
            res.append((array[x][y], array[x-i][y], i-1))
            break
    return res

graph = []

for i in range(N):
    for j in range(M):
        if array[i][j]:
            graph += search(i,j)

ans = 0
graph.sort(key=lambda x:x[2])

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

for item in graph:
    if find(item[0]) != find(item[1]):
        union(item[0], item[1])
        ans += item[2]

for i in range(1,n-1):
    if find(i) != find(i+1):
        print(-1)
        break
else:
    print(ans)