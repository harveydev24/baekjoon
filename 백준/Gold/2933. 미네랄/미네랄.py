from collections import deque
import copy

R, C = map(int, input().split())
total_minerals = 0
arr = []
for _ in range(R):
    row = list(input())
    total_minerals += row.count('x')
    arr.append(row)

N = int(input())
height = [R-x for x in list(map(int, input().split()))]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    cluster = {}
    cluster[(r, c)] = 1
    isBottom = False

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < R and 0 <= cc < C:
                if not visited[rr][cc] and arr[rr][cc] == 'x':
                    q.append((rr, cc))
                    visited[rr][cc] = 1
                    cluster[(rr, cc)] = 1
                    if rr == R-1:
                        isBottom = True

    if isBottom:
        return None
    else:
        return cluster


def throw_left(r):
    cluster_lst = []
    for c in range(C):
        if arr[r][c] == 'x':
            arr[r][c] = '.'
            visited[r][c] = 1
            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]
                if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and arr[rr][cc] == 'x':
                    tmp = bfs(rr, cc)
                    if tmp != None:
                        cluster_lst.append(tmp)
            break

    if cluster_lst:
        return(cluster_lst)


def throw_right(r):
    cluster_lst = []
    for c in range(C-1, -1, -1):
        if arr[r][c] == 'x':
            arr[r][c] = '.'
            visited[r][c] = 1
            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]
                if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and arr[rr][cc] == 'x':
                    tmp = bfs(rr, cc)
                    if tmp != None:
                        cluster_lst.append(tmp)
            break
    if cluster_lst:
        return(cluster_lst)


def check(cluster):
    for r, c in cluster:
        rr, cc = r+1, c
        if rr >= R:
            return False
        if (rr, cc) not in cluster and arr[rr][cc] == 'x':
            return False
    return True


def gravity(cluster):
    while check(cluster):
        next_cluster = {}
        for r, c in cluster:
            arr[r][c] = '.'
            next_cluster[(r+1, c)] = 1
        for r, c in next_cluster:
            arr[r][c] = 'x'
        cluster = copy.deepcopy(next_cluster)


for i in range(N):
    visited = [[0]*C for _ in range(R)]
    cluster_lst = []
    if i % 2:
        cluster_lst = throw_right(height[i])
    else:
        cluster_lst = throw_left(height[i])

    if cluster_lst:
        for cluster in cluster_lst:
            gravity(cluster)

for item in arr:
    print(''.join(item))

