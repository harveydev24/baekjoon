from collections import deque

R, C = map(int, input().split())

v, k = 0, 0
lst = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    cnt_v, cnt_k = 0, 0

    if lst[r][c] == 'v':
        cnt_v += 1
    elif lst[r][c] == 'k':
        cnt_k += 1

    while q:
        nr, nc = q.popleft()
        for i in range(4):
            rr, cc = nr+dr[i], nc+dc[i]
            if lst[rr][cc] == '.' and not visited[rr][cc]:
                visited[rr][cc] = 1
                q.append((rr, cc))
            elif lst[rr][cc] == 'v' and not visited[rr][cc]:
                cnt_v += 1
                visited[rr][cc] = 1
                q.append((rr, cc))
            elif lst[rr][cc] == 'k' and not visited[rr][cc]:
                cnt_k += 1
                visited[rr][cc] = 1
                q.append((rr, cc))

    if cnt_k > cnt_v:
        return cnt_k, 0
    else:
        return 0, cnt_v


for r in range(R):
    for c in range(C):
        if (lst[r][c] == 'v' or lst[r][c] == 'k') and not visited[r][c]:
            dk, dv = bfs(r, c)
            v += dv
            k += dk

print(k, v)
