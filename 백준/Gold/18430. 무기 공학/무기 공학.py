N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
ans = 0

shape = [[(0, -1), (1, 0)], [(-1, 0), (0, -1)],
         [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]


def solve(r, c, strength):
    global ans
    if r == N-1 and c == M:
        ans = max(ans, strength)
        return

    if c >= M:
        solve(r+1, 0, strength)
        return

    if visited[r][c]:
        solve(r, c+1, strength)
        return

    for i in range(4):
        rr, cc = r+shape[i][0][0], c+shape[i][0][1]
        rrr, ccc = r+shape[i][1][0], c+shape[i][1][1]
        if 0 <= rr < N and 0 <= rrr < N and 0 <= cc < M and 0 <= ccc < M:
            if not visited[rr][cc] and not visited[rrr][ccc]:
                visited[r][c] = True
                visited[rr][cc] = True
                visited[rrr][ccc] = True
                solve(r, c+1, strength+arr[r][c]*2+arr[rr][cc]+arr[rrr][ccc])
                visited[r][c] = False
                visited[rr][cc] = False
                visited[rrr][ccc] = False

    solve(r, c+1, strength)


solve(0, 0, 0)

print(ans)
