from collections import deque

K = int(input())
W, H = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(H)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
drr, dcc = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    q = deque([(0, 0, 0, 0)])
    visited = [[[False for j in range(K+1)]
                for i in range(W)] for _ in range(H)]
    for i in range(K):
        visited[0][0][i] = True

    if W == 1 and H == 1:
        print(0)
        exit(0)

    while q:
        r, c, K_cnt, cnt = q.popleft()

        for i in range(8):
            if K_cnt < K:
                rr, cc = r+drr[i], c+dcc[i]
                if 0 <= rr < H and 0 <= cc < W:
                    if not visited[rr][cc][K_cnt+1] and array[rr][cc] != 1:
                        q.append((rr, cc, K_cnt+1, cnt+1))
                        visited[rr][cc][K_cnt+1] = True
                        if rr == H-1 and cc == W-1:
                            print(cnt+1)
                            exit(0)
            else:
                break

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < H and 0 <= cc < W and not visited[rr][cc][K_cnt] and array[rr][cc] != 1:
                q.append((rr, cc, K_cnt, cnt+1))
                visited[rr][cc][K_cnt] = True
                if rr == H-1 and cc == W-1:
                    print(cnt+1)
                    exit(0)


bfs()
print(-1)
