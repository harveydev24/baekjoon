from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for i in range(8):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < M and 0 <= cc < N:
                if arr[rr][cc] == 1 and not visited[rr][cc]:
                    visited[rr][cc] = True
                    q.append((rr, cc))


cnt = 0
for r in range(M):
    for c in range(N):
        if not visited[r][c] and arr[r][c] == 1:
            bfs(r, c)
            cnt += 1

print(cnt)
