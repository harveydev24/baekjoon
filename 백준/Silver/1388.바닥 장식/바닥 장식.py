from collections import deque

N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]

dr, dc = [1,-1,0,0], [0,0,1,-1]

def dfs(r,c):
    if array[r][c] == '-':
        for i in range(2,4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and array[rr][cc] == array[r][c]:
                visited[rr][cc] = True
                dfs(rr, cc)
    else:
        for i in range(2):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and array[rr][cc] == array[r][c]:
                visited[rr][cc] = True
                dfs(rr, cc)

cnt = 0
visited = [[False]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            visited[r][c] = True
            dfs(r,c)
            cnt += 1
print(cnt)