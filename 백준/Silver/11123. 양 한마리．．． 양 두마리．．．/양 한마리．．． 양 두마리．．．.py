from collections import deque

T = int(input())

dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        nr, nc = q.popleft()
        for i in range(4):
            rr, cc = nr+dr[i], nc+dc[i]
            if 0 <= rr < H and 0 <= cc < W:
                if not visited[rr][cc] and lst[rr][cc] == '#':
                    visited[rr][cc] = True
                    q.append((rr, cc))


for _ in range(T):
    H, W = map(int, input().split())
    lst = [list(input()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    cnt = 0

    for r in range(H):
        for c in range(W):
            if not visited[r][c] and lst[r][c] == '#':
                bfs(r, c)
                cnt += 1

    print(cnt)
