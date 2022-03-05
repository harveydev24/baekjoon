N, M = map(int, input().split())

array = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

cnt = 0

def direction(s):
    if s == 'U':
        return -1,0
    elif s == 'D':
        return 1,0
    elif s == 'L':
        return 0,-1
    elif s == 'R':
        return 0,1

def dfs(r,c,k):
    global cnt

    visited[r][c] = k
    dr, dc = direction(array[r][c])
    rr, cc = r+dr, c+dc
    if 0<=rr<N and 0<=cc<M:
        if visited[rr][cc] == k:
            cnt += 1
            return
        elif visited[rr][cc] != 0:
            return
        else:
            dfs(rr,cc,k)
    else:
        cnt += 1
        return
    
k = 1
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            dfs(r,c,k)
            k += 1

print(cnt)
